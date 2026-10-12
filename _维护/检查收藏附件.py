#!/usr/bin/env python3
"""校验实际文件、Git 暂存区或已提交版本；只从 Git 恢复缺失附件。"""
import argparse
from datetime import datetime, timezone
from functools import lru_cache
import html
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args])


def without_code(text):
    return re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1[^\n]*$', '', text)


def embeds(text):
    text = without_code(text)
    # Angle brackets allow spaces/parentheses; bare paths allow balanced parentheses.
    pattern = r'!\[[^\]]*\]\(\s*(?:<([^>]+)>|((?:[^\s()]|\([^()]*\))+))\s*(?:["\'][^\n]*?["\'])?\s*\)'
    result = [(a or b, False) for a, b in re.findall(pattern, text)]
    result += [(x.split('|')[0], True) for x in re.findall(r'!\[\[([^\]]+)\]\]', text)]
    result += [(html.unescape(x), False) for x in re.findall(r'<(?:img|video|audio|source)\b[^>]*\bsrc=["\']([^"\']+)', text, re.I)]
    return result


def normalize(path):
    return os.path.normpath(str(path)).replace(os.sep, '/')


def resolve(note, ref, wiki, files):
    if ref.startswith('//') or urlsplit(ref).scheme:
        return None
    path = unquote(ref.split('#')[0].split('?')[0])
    if not path:
        return None
    local = normalize(PurePosixPath(note).parent / path)
    if local.startswith('../') or local.startswith('/'):
        return ('', '路径越出收藏库：' + ref)
    if not wiki:
        return (local, '')
    candidates = [local, normalize(path)]
    if not PurePosixPath(path).suffix:
        candidates += [x + '.md' for x in candidates[:]]
    for candidate in candidates:
        if candidate in files:
            return (candidate, '')
    matches = [x for x in files if PurePosixPath(x).name in {path, path + '.md'}]
    if len(matches) == 1:
        return (matches[0], '')
    if len(matches) > 1:
        return ('', '同名附件不唯一，请写明路径：' + ref)
    return (local, '')


def valid_media(path, data):
    suffix = PurePosixPath(path).suffix.lower()
    if not data:
        return '文件为空'
    checks = {
        '.png': lambda b: b.startswith(b'\x89PNG\r\n\x1a\n') and b'IEND' in b[-32:],
        '.jpg': lambda b: b.startswith(b'\xff\xd8') and b'\xff\xd9' in b[-16:],
        '.jpeg': lambda b: b.startswith(b'\xff\xd8') and b'\xff\xd9' in b[-16:],
        '.gif': lambda b: b.startswith((b'GIF87a', b'GIF89a')),
        '.webp': lambda b: b.startswith(b'RIFF') and b[8:12] == b'WEBP',
        '.avif': lambda b: b[4:8] == b'ftyp' and b'avif' in b[:64],
        '.mp4': lambda b: b[4:8] == b'ftyp',
        '.pdf': lambda b: b.startswith(b'%PDF'),
    }
    if suffix == '.svg':
        try:
            if ET.fromstring(data).tag.split('}')[-1] != 'svg':
                return '文件不是 SVG'
        except ET.ParseError:
            return 'SVG 无法解析'
    if suffix in checks and not checks[suffix](data):
        return '媒体格式或文件完整性异常'
    return ''


FIELDS = ['标题', '类型', '分类', '来源', '创建时间', '标签', '状态', '价值评分', '可用于', '相关项目']
HEADINGS = ['直观预览', '一句话价值', 'AI 选用指南', '内容摘要', '为什么值得收藏',
            '未来可以怎么用', '原始内容 / 链接', '相关联想', '适合反向调用的场景']
GUIDE_ROWS = ['优先选用条件', '不适合或暂缓条件', '复用方式', '输入与产出',
              '首次读取入口', '同类选择依据', '接入前提与待核实项', '检索词']
INDEXES = ['最近收录', '分类索引', '标签索引', 'AI选材索引']


def collection_problems(note, text, files, read):
    problems = []
    front = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not front:
        return ['缺少 YAML 属性']
    metadata = dict(re.findall(r'^([^:\n]+):[ \t]*(.*)$', front[1], re.M))
    for name in FIELDS:
        if name not in metadata:
            problems.append('缺少属性：' + name)
    category = metadata.get('分类', '').strip('"\'')
    if category != str(PurePosixPath(note).parent):
        problems.append('分类属性与文件目录不一致')
    for name in ['标签', '可用于', '相关项目']:
        try:
            value = json.loads(metadata.get(name, ''))
            if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
                raise ValueError()
        except ValueError:
            problems.append(name + '须按模板填写为带引号的字符串数组')
    if not re.search(r'-\d{4}-\d{2}-\d{2}\.md$', note):
        problems.append('文件名须以收录日期结尾')
    body = without_code(text[front.end():])
    headings = re.findall(r'^## (.+)$', body, re.M)
    for name in HEADINGS:
        if name not in headings:
            problems.append('缺少章节：' + name)
    if len(headings) != len(set(headings)):
        problems.append('存在重复的二级章节')
    if all(name in headings for name in HEADINGS[:3]):
        if not (headings.index(HEADINGS[0]) < headings.index(HEADINGS[1]) < headings.index(HEADINGS[2])):
            problems.append('直观预览、一句话价值和 AI 选用指南的顺序不正确')
    for name in GUIDE_ROWS:
        if not re.search(r'^\| ' + name + r' \| \S.* \|$', body, re.M):
            problems.append('缺少或留空的 AI 选用说明：' + name)
    for index in INDEXES:
        path = '_索引/' + index + '.md'
        try:
            indexed = read(path).decode() if path in files else ''
        except OSError:
            indexed = ''
        if PurePosixPath(note).name not in indexed:
            problems.append('未进入索引：' + index)
    return problems


def audit(root, staged=False, revision=None):
    if revision:
        files = set(git(root, 'ls-tree', '-r', '-z', '--name-only', revision).decode().split('\0'))
        read = lambda p: git(root, 'show', revision + ':' + p)
    elif staged:
        files = set(git(root, 'ls-files', '--cached', '-z').decode().split('\0'))
        read = lambda p: git(root, 'show', ':' + p)
    else:
        files = set(git(root, 'ls-files', '--cached', '-z').decode().split('\0'))
        read = lambda p: (root / p).read_bytes()
    read = lru_cache(maxsize=None)(read)
    files.discard('')
    issues, references, cards, collections, checked = [], 0, 0, 0, set()
    for note in sorted(files):
        if not note.endswith('.md') or not re.match(r'^\d\d-[^/]+/', note):
            continue
        try:
            text = read(note).decode('utf-8')
        except (OSError, UnicodeError, subprocess.CalledProcessError):
            issues.append({'笔记': note, '问题': '笔记不可读取'})
            continue
        cards += 1
        if re.search(r'(?m)^(?:<<<<<<< |=======\s*$|>>>>>>> )|<mark class="conflict ', text):
            issues.append({'笔记': note, '问题': '存在未解决的同步冲突标记'})
        is_collection = bool(re.match(r'^(0\d|1[01])-', note))
        if is_collection:
            collections += 1
            issues += [{'笔记': note, '问题': item} for item in collection_problems(note, text, files, read)]
            preview = re.search(r'(?ms)^## 直观预览\s*\n(.*?)(?=^## |\Z)', text)
            if not preview or not (any(resolve(note, ref, wiki, files) is not None for ref, wiki in embeds(preview[1])) or '```mermaid' in preview[1]):
                issues.append({'笔记': note, '问题': '收藏缺少直观预览中的图像、视频或结构图'})
        for ref, wiki in embeds(text):
            resolved = resolve(note, ref, wiki, files)
            if resolved is None:
                continue
            path, error = resolved
            references += 1
            if error:
                issues.append({'笔记': note, '引用': ref, '问题': error})
                continue
            if path not in files:
                issues.append({'笔记': note, '引用': ref, '文件': path, '问题': '附件未纳入当前 Git 版本'})
                continue
            try:
                data = read(path)
            except (OSError, subprocess.CalledProcessError):
                issues.append({'笔记': note, '引用': ref, '文件': path, '问题': '本地附件缺失或无法读取'})
                continue
            if path not in checked:
                error = valid_media(path, data)
                checked.add(path)
                if error:
                    issues.append({'笔记': note, '引用': ref, '文件': path, '问题': error})
        if is_collection:
            for ref in re.findall(r'(?<!!)\[[^\]]*\]\(([^)\n]+)\)', without_code(text)):
                ref = ref.strip('<>')
                if ref.startswith(('#', '/Users/')) or urlsplit(ref).scheme:
                    continue
                resolved = resolve(note, ref, False, files)
                if resolved is None:
                    continue
                path, error = resolved
                exists = path in files or any(x.startswith(path.rstrip('/') + '/') for x in files)
                if error or not exists:
                    issues.append({'笔记': note, '引用': ref, '问题': error or '库内链接失效'})
    return {'检查笔记数': cards, '收藏卡片数': collections, '本地引用数': references,
            '不同附件数': len(checked), '问题': issues}


def repair_missing(root):
    restored = []
    files = git(root, 'ls-tree', '-r', '-z', '--name-only', 'HEAD').decode().split('\0')
    staged_files = set(git(root, 'ls-files', '--cached', '-z').decode().split('\0'))
    for name in files:
        if not name.startswith(('_附件/', '配图/')) or name not in staged_files:
            continue
        path = root / name
        # Do not overwrite edits or follow symlinks outside the canonical repository.
        if path.exists() or path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            continue
        data = git(root, 'show', 'HEAD:' + name)
        path.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation avoids overwriting a file that a sync client just restored.
        try:
            with path.open('xb') as stream:
                stream.write(data)
        except FileExistsError:
            continue
        restored.append(name)
    return restored


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--staged', action='store_true')
    mode.add_argument('--revision')
    parser.add_argument('--repair-missing', action='store_true')
    parser.add_argument('--status-file', type=Path)
    args = parser.parse_args()
    if args.repair_missing and (args.staged or args.revision):
        parser.error('恢复仅用于实际工作目录，不用于暂存区或历史版本')
    root = args.root.resolve()
    restored = repair_missing(root) if args.repair_missing else []
    result = audit(root, args.staged, args.revision)
    changed = True
    if args.status_file:
        args.status_file.parent.mkdir(parents=True, exist_ok=True)
        if args.status_file.exists():
            previous = json.loads(args.status_file.read_text())
            previous.pop('检查时间', None)
            changed = previous != result
        status = {**result, '检查时间': datetime.now(timezone.utc).isoformat()}
        temporary = args.status_file.with_suffix('.tmp')
        temporary.write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n')
        temporary.replace(args.status_file)
    if changed or restored:
        print(json.dumps({**result, '本次恢复': restored}, ensure_ascii=False, indent=2))
    return 1 if result['问题'] else 0


if __name__ == '__main__':
    sys.exit(main())

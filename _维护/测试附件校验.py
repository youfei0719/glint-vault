#!/usr/bin/env python3
"""用独立临时 Git 仓库验证漏提交、损坏、同步删除与恢复，绝不改真实卡片。"""
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('attachment_audit', Path(__file__).with_name('检查收藏附件.py'))
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

SVG = b'<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"/>'


class AttachmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'user.name', 'Test')
        self.note = '01-界面设计/组件/测试-2026-10-12.md'
        self.image = '_附件/收藏预览/有 空格.svg'
        self.write(self.image, SVG)
        self.card('![](<../../_附件/收藏预览/有 空格.svg>)')
        for name in audit.INDEXES:
            self.write('_索引/' + name + '.md', '[测试](../' + self.note + ')\n')
        self.git('add', '.')

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.root), *args], capture_output=True, check=True)

    def write(self, name, data):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data if isinstance(data, bytes) else data.encode())

    def card(self, preview):
        fields = '\n'.join(x + ': ' + ('[]' if x in ['标签', '可用于', '相关项目'] else
                                      '"01-界面设计/组件"' if x == '分类' else '"测试"')
                           for x in audit.FIELDS)
        body = '# 测试\n\n## 直观预览\n\n' + preview + '\n\n## 一句话价值\n测试\n\n## AI 选用指南\n'
        body += '\n'.join('| ' + x + ' | 测试说明 |' for x in audit.GUIDE_ROWS)
        body += '\n\n' + '\n\n'.join('## ' + x + '\n\n测试内容' for x in audit.HEADINGS[3:])
        self.write(self.note, '---\n' + fields + '\n---\n' + body + '\n')

    def issues(self, **options):
        return audit.audit(self.root, **options)['问题']

    def test_valid_unicode_angle_path_in_index(self):
        self.assertEqual(self.issues(staged=True), [])

    def test_unstaged_image_is_rejected_even_when_visible_locally(self):
        self.git('rm', '--cached', self.image)
        self.assertTrue(self.issues(staged=True))
        self.assertTrue((self.root / self.image).exists())

    def test_staged_blob_is_checked_instead_of_working_copy(self):
        self.write(self.image, b'not an SVG')
        self.git('add', self.image)
        self.write(self.image, SVG)
        self.assertTrue(self.issues(staged=True))

    def test_revision_does_not_depend_on_local_missing_file(self):
        self.git('commit', '-qm', 'fixture')
        (self.root / self.image).unlink()
        self.assertTrue(self.issues())
        self.assertEqual(self.issues(revision='HEAD'), [])

    def test_staged_deletion_is_rejected(self):
        self.git('rm', '-f', self.image)
        self.assertTrue(self.issues(staged=True))

    def test_code_fences_are_not_actual_image_references(self):
        self.card('![](<../../_附件/收藏预览/有 空格.svg>)\n\n```md\n![](missing.png)\n```')
        self.git('add', self.note)
        self.assertEqual(self.issues(staged=True), [])

    def test_wiki_resolves_unique_attachment_and_rejects_ambiguity(self):
        self.card('![[有 空格.svg]]')
        self.git('add', self.note)
        self.assertEqual(self.issues(staged=True), [])
        self.write('_附件/其他/有 空格.svg', SVG)
        self.git('add', '.')
        self.assertTrue(self.issues(staged=True))

    def test_private_outside_file_is_rejected(self):
        self.card('![](/Users/someone/Downloads/private.png)')
        self.git('add', self.note)
        self.assertTrue(self.issues(staged=True))

    def test_placeholder_or_external_only_preview_is_rejected(self):
        for preview in ['截图未保存', '![](https://example.invalid/image.png)']:
            self.card(preview)
            self.git('add', self.note)
            self.assertTrue(self.issues(staged=True))

    def test_conflict_markup_is_rejected(self):
        self.card('![](<../../_附件/收藏预览/有 空格.svg>)\n<mark class="conflict ours">冲突</mark>')
        self.git('add', self.note)
        self.assertTrue(self.issues(staged=True))

    def test_restore_missing_preserves_existing_edits(self):
        self.git('commit', '-qm', 'fixture')
        (self.root / self.image).unlink()
        self.assertEqual(audit.repair_missing(self.root), [self.image])
        self.assertEqual((self.root / self.image).read_bytes(), SVG)
        edited = SVG.replace(b'10', b'20')
        self.write(self.image, edited)
        self.assertEqual(audit.repair_missing(self.root), [])
        self.assertEqual((self.root / self.image).read_bytes(), edited)

    def test_staged_intentional_deletion_is_not_restored(self):
        self.git('commit', '-qm', 'fixture')
        self.git('rm', self.image)
        self.assertEqual(audit.repair_missing(self.root), [])

    def test_missing_index_is_rejected(self):
        self.write('_索引/AI选材索引.md', '# 索引\n')
        self.git('add', '.')
        self.assertTrue(self.issues(staged=True))

    def test_broken_related_card_link_is_rejected(self):
        self.card('![](<../../_附件/收藏预览/有 空格.svg>)\n[其他卡](./missing.md)')
        self.git('add', '.')
        self.assertTrue(self.issues(staged=True))

    def test_pre_commit_hook_blocks_missing_attachment(self):
        scripts = self.root / '_维护'
        scripts.mkdir()
        scripts.joinpath('检查收藏附件.py').write_bytes(Path(__file__).with_name('检查收藏附件.py').read_bytes())
        hook = self.root / '.git/hooks/pre-commit'
        hook.write_bytes(Path(__file__).with_name('git钩子').joinpath('pre-commit').read_bytes())
        hook.chmod(0o755)
        self.git('rm', '--cached', self.image)
        result = subprocess.run(['git', '-C', str(self.root), 'commit', '-qm', 'must fail'], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('附件未纳入'.encode(), result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()

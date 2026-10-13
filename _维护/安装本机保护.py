#!/usr/bin/env python3
"""安装 Git 附件校验钩子和由 Obsidian 执行的预览附件恢复插件。"""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
for name in ['pre-commit', 'pre-push']:
    (root / '_维护/git钩子' / name).chmod(0o755)
subprocess.run(['git', '-C', str(root), 'config', '--local', 'core.hooksPath', '_维护/git钩子'], check=True)
if sys.platform != 'darwin':
    print('已安装本仓库 Git 钩子；预览附件同步插件仅适用于桌面版 Obsidian。')
    sys.exit(0)

# launchd 默认没有“文稿”目录授权，会静默失败；插件在已获授权的 Obsidian 进程中运行。
label = 'com.youfei.glint-vault-attachments'
launch = Path.home() / 'Library/LaunchAgents' / (label + '.plist')
subprocess.run(['launchctl', 'bootout', 'gui/' + str(os.getuid()), str(launch)], capture_output=True)
if launch.exists():
    launch.unlink()

plugin_id = 'glint-vault-preview-sync'
source = root / '_维护/Obsidian插件/附件预览同步'
registry = Path.home() / 'Library/Application Support/obsidian/obsidian.json'
vault_root = root
try:
    registered = json.loads(registry.read_text()).get('vaults', {}).values()
    candidates = [Path(item['path']).resolve() for item in registered
                  if 'path' in item and root.is_relative_to(Path(item['path']).resolve())]
    if candidates:
        vault_root = max(candidates, key=lambda item: len(item.parts))
except (OSError, json.JSONDecodeError, KeyError):
    pass
relative_root = root.relative_to(vault_root).as_posix()
destination = vault_root / '.obsidian/plugins' / plugin_id
destination.mkdir(parents=True, exist_ok=True)
for name in ['manifest.json', 'main.js']:
    shutil.copy2(source / name, destination / name)
enabled = vault_root / '.obsidian/community-plugins.json'
try:
    plugins = json.loads(enabled.read_text()) if enabled.exists() else []
except json.JSONDecodeError:
    plugins = []
if plugin_id not in plugins:
    plugins.append(plugin_id)
enabled.write_text(json.dumps(plugins, ensure_ascii=False, indent=2) + '\n')
data = destination / 'data.json'
try:
    settings = json.loads(data.read_text()) if data.exists() else {}
except json.JSONDecodeError:
    settings = {}
settings['collectionRoot'] = '' if relative_root == '.' else relative_root
data.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + '\n')
print(f'Git 提交与推送校验已启用；已为 Vault {vault_root} 安装收藏预览同步，请重启或重新加载 Obsidian。')

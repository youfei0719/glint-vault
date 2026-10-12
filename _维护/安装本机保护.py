#!/usr/bin/env python3
"""安装 Git 附件校验钩子，以及 macOS 每分钟的缺失附件恢复任务。"""
from pathlib import Path
import os
import plistlib
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
for name in ['pre-commit', 'pre-push']:
    (root / '_维护/git钩子' / name).chmod(0o755)
subprocess.run(['git', '-C', str(root), 'config', '--local', 'core.hooksPath', '_维护/git钩子'], check=True)
if sys.platform != 'darwin':
    print('已安装本仓库 Git 钩子；定时恢复任务仅适用于 macOS。')
    sys.exit(0)

home = Path.home()
state = home / 'Library/Application Support/GlintVault'
state.mkdir(parents=True, exist_ok=True)
label = 'com.youfei.glint-vault-attachments'
launch = home / 'Library/LaunchAgents' / (label + '.plist')
launch.parent.mkdir(parents=True, exist_ok=True)
definition = {
    'Label': label,
    'ProgramArguments': ['/usr/bin/python3', str(root / '_维护/检查收藏附件.py'),
                         '--root', str(root), '--repair-missing',
                         '--status-file', str(state / '附件健康状态.json')],
    'WorkingDirectory': str(root),
    'RunAtLoad': True,
    'StartInterval': 60,
    'EnvironmentVariables': {'PATH': '/usr/bin:/bin:/usr/sbin:/sbin'},
    'StandardOutPath': str(state / '附件检查.log'),
    'StandardErrorPath': str(state / '附件检查错误.log'),
}
domain = 'gui/' + str(os.getuid())
if launch.exists():
    subprocess.run(['launchctl', 'bootout', domain, str(launch)], capture_output=True)
launch.write_bytes(plistlib.dumps(definition))
subprocess.run(['launchctl', 'bootstrap', domain, str(launch)], check=True)
print('Git 提交与推送校验已启用；每分钟检查并恢复 Git 已备份的缺失附件。')

# -*- encoding: utf-8 -*-
"""
@Time: 2024-03-31 19:27
@Auth: xjjxhxgg
@File: release.py
@IDE: PyCharm
@Motto: xhxgg
"""
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', help='the version of the package to release', default=None)
parser.add_argument('-r', '--repository', help='the command to release the package', default='pypi')
args = parser.parse_args()
if args.version:
    version = args.version
else:
    raise ValueError('the version of the package to release must be specified')

repository = args.repository
cmds =['python -m pip install --upgrade build',
       'python -m build',
       'python -m pip install --upgrade twine',
       f'python -m twine upload --repository {repository} dist/pyzyj-{version}.tar.gz',
       ]
for cmd in cmds:
    os.system(cmd)







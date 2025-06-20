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
parser.add_argument('-r', '--repository', help='the pypi repository to release the package, in (pypi, testpypi)', default='pypi')
args = parser.parse_args()
if args.version:
    version = args.version
else:
    found = False
    try:
        with open('setup.py', 'r') as f:
            for line in f:
                if 'version' in line:
                    version = line.split('=')[1].strip().replace("'",'').replace('"','').replace(',','')
                    found = True
                    break
    except:
        raise ValueError('the version of the package to release must be specified or setup.py must be in the current directory')
    finally:
        if not found:
            raise ValueError('the version of the package to release must be specified or setup.py must be in the current directory')

repository = args.repository
cmds =['python -m pip install --upgrade build',
       'python -m pip install --upgrade twine',
       'python -m pip install --upgrade packaging',
       'python -m build',
       f'python -m twine upload --repository {repository} dist/pyzyj-{version}.tar.gz',
       f'python -m twine upload --repository {repository} dist/pyzyj-{version}-py3-none-any.whl',
       ]
for cmd in cmds:
    os.system(cmd)







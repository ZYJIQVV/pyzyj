# -*- encoding: utf-8 -*-
"""
@Time: 2024-03-12 17:24
@Auth: xjjxhxgg
@File: update.py
@IDE: PyCharm
@Motto: xhxgg

Used to replace the old code in the python interpreters with the new code
"""
import os
import re
import shutil
import argparse
pyzyj_root = os.path.join(os.getcwd(),'pyzyj')
def replace_pip(python_root=r'C:\Users\lenovo\AppData\Roaming\Python'):
    python_interpreters = [d for d in os.listdir(python_root) if re.match(r'Python\d+', d)]
    for pi in python_interpreters:
        pi_path = fr'{python_root}\{pi}\site-packages'
        print(pi_path)
        # replace the old pyzyj code with the new one
        old_pyzyj = fr'{pi_path}\pyzyj'
        if os.path.exists(old_pyzyj):
            backup_pyzyj = fr'{pi_path}\pyzyj_backup'
            if os.path.exists(backup_pyzyj):
                shutil.rmtree(backup_pyzyj)
                print(f'remove {backup_pyzyj}')
            shutil.move(old_pyzyj, backup_pyzyj)
        shutil.copytree(pyzyj_root, old_pyzyj)

def replace_conda(conda_root=r'F:\D\ProgramData\Anaconda3'):
    envs = [d for d in os.listdir(os.path.join(conda_root, 'envs')) if os.path.isdir(os.path.join(conda_root, 'envs', d))]
    for env in envs:
        env_path = fr'{conda_root}\envs\{env}\Lib\site-packages'
        print(env_path)
        # replace the old pyzyj code with the new one
        old_pyzyj = fr'{env_path}\pyzyj'
        if os.path.exists(old_pyzyj):
            backup_pyzyj = fr'{env_path}\pyzyj_backup'
            if os.path.exists(backup_pyzyj):
                shutil.rmtree(backup_pyzyj)
                print(f'remove {backup_pyzyj}')
            shutil.move(old_pyzyj, backup_pyzyj)
        shutil.copytree(pyzyj_root, old_pyzyj)

if __name__ == '__main__':
    # if this script is called from the command line, then parse the arguments
    # python update.py -p pip_root means call the function replace_pip
    # python update.py -c conda_root means call the function replace_conda
    # it must be called as python update.py -p pip_root or python update.py -c conda_root
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pip_root', help='the root of pip', default=r'C:\Users\lenovo\AppData\Roaming\Python')
    parser.add_argument('-c', '--conda_root', help='the root of conda', default=r'F:\D\ProgramData\Anaconda3')
    args = parser.parse_args()
    if args.pip_root:
        replace_pip(args.pip_root)
    if args.conda_root:
        replace_conda(args.conda_root)

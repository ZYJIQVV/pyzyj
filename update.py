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
pyzyj_root = os.path.join(os.getcwd(),'pyzyj')
def replace_pip(python_root=r'C:\Users\lenovo\AppData\Roaming\Python'):
    python_interpreters = [d for d in os.listdir(python_root) if re.match(r'Python\d+', d)]
    for pi in python_interpreters:
        pi_path = fr'{python_root}\{pi}\site-packages'
        # print(pi_path)
        # replace the old pyzyj code with the new one
        old_pyzyj = fr'{pi_path}\pyzyj'
        if os.path.exists(old_pyzyj):
            backup_pyzyj = fr'{pi_path}\pyzyj_backup'
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
            shutil.move(old_pyzyj, backup_pyzyj)
        shutil.copytree(pyzyj_root, old_pyzyj)

replace_conda()
# -*- encoding: utf-8 -*-
"""
@Time: 2024-03-11 18:46
@Auth: xjjxhxgg
@File: setup.py
@IDE: PyCharm
@Motto: xhxgg
"""
from setuptools import setup, find_packages

setup(
    name='pyzyj',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list your project dependencies here
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

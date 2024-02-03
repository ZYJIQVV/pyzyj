# -*- coding: utf-8 -*-
"""
@Time: 2024-02-03 17:54
@Auth: xjjxhxgg
@File: download.py
@IDE: PyCharm
@Motto: xhxgg
"""

import requests


def get(url, file, mode):
    response = requests.get(url)
    if mode == 'wb':
        with open(file, mode) as f:
            f.write(response.content)
    else:
        with open(file, mode, encoding='utf-8') as f:
            f.write(response.text)

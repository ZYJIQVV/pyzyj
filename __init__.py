# -*- coding: utf-8 -*-
"""
@Time: 2024-01-23 20:30
@Auth: xjjxhxgg
@File: __init__.py
@IDE: PyCharm
@Motto: xhxgg
"""
from .format import coco_to_yolo, yolo_to_coco
from .visualize import visualize

compenents = {
    'coco_to_yolo': coco_to_yolo,
    'yolo_to_coco': yolo_to_coco,
    'visualize': visualize
}

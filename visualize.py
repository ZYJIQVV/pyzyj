# -*- coding: utf-8 -*-
"""
@Time: 2024-01-29 13:30
@Auth: xjjxhxgg
@File: visualize.py
@IDE: PyCharm
@Motto: xhxgg
"""
from typing import Union

import cv2
import os
import json
import numpy as np
from .format import xml_parser


def visualize(img_path: str, ann_path: str, save_path: str = None, color: tuple = None, parser: callable = None, format: str='yolo') -> None:
    """
    visualize the image with annotations, at present only support object detection with bbox
    :param img_path: the path of image
    :param ann_path: the path of annotation file
    :param save_path: if not None, save the image with bbox to save_path else show the image with bbox
    :param color: the color of bbox or mask
    :param parser: if ann_path is xml, parser is required, which is a callable function and returns a list of bbox
     like [{'name':name, 'bbox':[xmin,ymin,xmax,ymax]},...] or [[xmin,ymin,xmax,ymax],...].
     A simple parser is provided in format.py
    :param format: the format of annotation file which should be in ['custom', 'yolo'].
     If format is 'custom', a  parser is needed which returns the same format as above.
    :return:
    """
    img = None
    if color is None:
        color = (0, 0, 255)
    if ann_path.endswith('.json'):  # coco
        ann = json.load(open(ann_path, 'r'))
        img = cv2.imread(img_path)
        filename = os.path.basename(img_path)
        img_id = None
        for ann_img in ann['images']:
            if ann_img['file_name'] == filename:
                img_id = ann_img['id']
                break
        if img_id is None:
            raise Exception('Image not found in ann file')
        for ann_ann in ann['annotations']:
            if ann_ann['image_id'] == img_id:
                bbox = ann_ann['bbox']
                cx = bbox[0]
                cy = bbox[1]
                w = bbox[2]
                h = bbox[3]
                xmin = int(cx - w / 2)
                ymin = int(cy - h / 2)
                xmax = int(cx + w / 2)
                ymax = int(cy + h / 2)
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 2)
    elif ann_path.endswith('.xml'):  # voc
        if parser is None:
            raise Exception('parser is None')
        img = cv2.imread(img_path)
        bboxes = parser(ann_path)
        for bbox in bboxes:
            if isinstance(bbox, dict):
                bbox = bbox['bbox']
            x = bbox[0]
            y = bbox[1]
            w = bbox[2]
            h = bbox[3]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    elif ann_path.endswith('.txt'):
        if format == 'yolo':  # yolo
            img = cv2.imread(img_path)
            with open(ann_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip().split(' ')
                    x_center = float(line[1])
                    y_center = float(line[2])
                    w = float(line[3])
                    h = float(line[4])
                    img_h, img_w, _ = img.shape
                    x = int((x_center - w / 2) * img_w)
                    y = int((y_center - h / 2) * img_h)
                    x2 = int((x_center + w / 2) * img_w)
                    y2 = int((y_center + h / 2) * img_h)
                    cv2.rectangle(img, (x, y), (x2, y2), color, 2)
        elif format == 'custom':
            if parser is None:
                raise Exception('parser is None')
            img = cv2.imread(img_path)
            bboxes = parser(ann_path)
            for bbox in bboxes:
                if isinstance(bbox, dict):
                    bbox = bbox['bbox']
                x = bbox[0]
                y = bbox[1]
                w = bbox[2]
                h = bbox[3]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    else:
        raise Exception('Annotation file not supported')
    if img is not None:
        if save_path is not None:
            if os.path.isdir(save_path):
                save_path = os.path.join(save_path, 'vis.jpg')
            cv2.imwrite(save_path, img)
        else:
            cv2.imshow('vis', img)
            cv2.waitKey(0)
    else:
        raise Exception('Image not found')

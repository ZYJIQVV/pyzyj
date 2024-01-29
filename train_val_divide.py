# -*- coding: utf-8 -*-
"""
@Time: 2024-01-29 14:45
@Auth: xjjxhxgg
@File: train_val_divide.py
@IDE: PyCharm
@Motto: xhxgg
"""
import random


def coco_divide(coco_json, train_json, val_json, train_ratio=0.8):
    import json
    import random
    coco_json = json.load(open(coco_json, 'r'))
    images = coco_json['images']
    annotations = coco_json['annotations']
    categories = coco_json['categories']
    train_images = []
    val_images = []
    train_annotations = []
    val_annotations = []
    train_categories = []
    val_categories = []
    train_img_ids = []
    val_img_ids = []
    for img in images:
        if random.random() < train_ratio:
            train_images.append(img)
            train_img_ids.append(img['id'])
        else:
            val_images.append(img)
            val_img_ids.append(img['id'])
    for ann in annotations:
        if ann['image_id'] in train_img_ids:
            train_annotations.append(ann)
        else:
            val_annotations.append(ann)
    for cat in categories:
        if cat['id'] in [ann['category_id'] for ann in train_annotations]:
            train_categories.append(cat)
        else:
            val_categories.append(cat)
    train = {
        'images': train_images,
        'annotations': train_annotations,
        'categories': train_categories,
        'info':[],
        'license':[]
    }
    val = {
        'images': val_images,
        'annotations': val_annotations,
        'categories': val_categories,
        'info':[],
        'license':[]
    }
    json.dump(train, open(train_json, 'w'))
    json.dump(val, open(val_json, 'w'))


def yolo_divide(total_lbl_root, total_img_root, yolo_root, train_ratio=0.8):
    import os
    import shutil
    for root, dirs, files in os.walk(total_lbl_root):
        for file in files:
            if file.endswith('.txt'):
                if random.random() < train_ratio:
                    shutil.copy(str(os.path.join(total_lbl_root, file)), str(os.path.join(yolo_root,'labels','train', file)))
                    shutil.copy(str(os.path.join(total_img_root, file.replace('.txt', '.jpg'))), str(os.path.join(yolo_root,'images','train', file.replace('.txt', '.jpg'))))
                else:
                    shutil.copy(str(os.path.join(total_lbl_root, file)), str(os.path.join(yolo_root,'labels','val', file)))
                    shutil.copy(str(os.path.join(total_img_root, file.replace('.txt', '.jpg'))),str(os.path.join(yolo_root,'images','val', file.replace('.txt', '.jpg'))))
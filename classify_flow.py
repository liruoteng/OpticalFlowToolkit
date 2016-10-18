#!/usr/bin/python
"""
classify_flow.py
This file convert flow file (.flo) into into flow class file according to the direction of the flow
Author: Li Ruoteng
Date: 16 Oct 2016
"""

import numpy as np
import os
from PIL import Image

full = 196608
input_dir = '../../../data/FC/data'
output_dir = '../SegNet/CamVid/trainflowannot'

'''
for file_name in os.listdir(input_dir):
    if file_name.find('.flo') != -1:
        flow = fl.read_flow(os.path.join(input_dir, file_name))
        seg = fl.flow_to_segment(flow)
        seg_img = Image.fromarray(seg.astype(np.uint8))
        seg_img.save(os.path.join(output_dir, file_name[0:file_name.find('.flo')] + '.png'))


'''
files = os.listdir(output_dir)
files.sort()
stats = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for j in range(22276):
    file_name = files[j]
    img = Image.open(os.path.join(output_dir, file_name))
    data = np.array(img)
    for i in range(9):
        idx = (data == i)
        stats[i] += float(np.sum(idx)) / full


for i in range(len(stats)):
    stats[i] /= 22276
    print stats[i]

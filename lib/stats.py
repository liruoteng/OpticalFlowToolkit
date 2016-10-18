#!/usr/bin/python
"""
stats.py
This file generates data statistics
Author : Ruoteng Li
Date 16 Oct 2016
"""

import numpy as np
import os
from PIL import Image

full = 196608
input_dir = '../../../data/FC/data'
output_dir = '../SegNet/CamVid/trainflowannot'

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
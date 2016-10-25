#!/usr/bin/python
"""
crop_flow.py
This file crops flow file (.flo) and image pairs into into patches according to the given locations
Author: Li Ruoteng
Date: 16 Oct 2016
"""

import os
import argparse
import numpy as np
from PIL import Image
from lib import flowlib as fl

canvas_height = 540
canvas_width = 960
patch_height = 256
patch_width = 256

f1 = open('data/cleaninput/img1_list.txt', 'r')
f2 = open('data/cleaninput/img2_list.txt', 'r')
f = open('data/cleaninput/flo_list.txt', 'r')
g1 = open('img1_list.txt', 'wb')
g2 = open('img2_list.txt', 'wb')
g = open('flo_list.txt', 'wb')
output_dir = 'out'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
img1_input = f1.readlines()
img2_input = f2.readlines()
flow_input = f.readlines()
length = len(flow_input)

for i in range(600):
    x_locations = np.random.randint(0, canvas_width - patch_width, size=10)
    y_locations = np.random.randint(0, canvas_height - patch_height, size=10)
    img1 = Image.open(img1_input[i].strip())
    img2 = Image.open(img2_input[i].strip())
    flow = fl.read_flow(flow_input[i].strip())
    for (x, y) in zip(x_locations, y_locations):
        patch_img1 = img1.crop((x, y, x+patch_width, y+patch_height))
        patch_img2 = img2.crop((x,y,x+patch_width, y+patch_height))
        patch_flow = flow[y:y+patch_height, x:x+patch_width]
        filename = str.format('%05d_' % i) + str(x) + '_' + str(y)
        path1 = os.path.join(output_dir, filename + '_img1.png')
        path2 = os.path.join(output_dir, filename + '_img2.png')
        flow_path = os.path.join(output_dir, filename + '.flo')
        patch_img1.save(path1)
        patch_img2.save(path2)
        fl.write_flow(patch_flow, flow_path)
        g1.write(path1 + '\n')
        g2.write(path2 + '\n')
        g.write(flow_path + '\n')

f1.close()
f2.close()
f.close()
g1.close()
g2.close()
g.close()




'''

file_list = []
in_dir = os.path.abspath(args.input_dir)
out_dir = os.path.abspath(args.output_dir)
flow_count = 0
image_count = 0
for root, dirs, files in os.walk(in_dir):
    if files:
        for filename in files:
            file_path = os.path.join(in_dir, root + '/' + filename)
            if filename.find(args.flow_format) != -1:
                # this is flow file
                image_count += 1
                print 'image count: ', image_count
                flow = fl.read_flow(file_path)
                new_flow = flow[args.y-1:args.y+args.h-1, args.x-1:args.x-1+args.w, :]
                out_path = os.path.join(out_dir, root[root.find('drive/')+6:])
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                fl.write_flow(new_flow, os.path.join(out_path, filename))
            elif filename.find(args.image_format) != -1:
                # this is an image file
                flow_count += 1
                print 'flow count: ', flow_count
                img = Image.open(file_path)
                new_img = img.crop((args.x-1, args.y-1, args.x+args.h-1, args.y+args.w-1))
                out_path = os.path.join(out_dir, root[root.find('drive/')+6:])
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                new_img.save(os.path.join(out_path, filename))

'''
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
from lib import kittitool
from lib import flowlib as fl

# hard code
yellow_page = {'clean': 'drive_clean', 'haze': 'drive_haze',
               'rain': 'drive_rain', 'kitti2012': 'KITTI2012',
               'kitti2015': 'KITTI2015', 'sintel': 'Sintel'}
patch_width = 512
patch_height = 384
length = 600
# Parse Input
parser = argparse.ArgumentParser(description="Image Crop Tool")
parser.add_argument("dataset", type=str, help="image list of the data set to crop")
parser.add_argument("length", type=int, help="the number of output crops to generate")
parser.add_argument("--height", type=int, help="the height of the output patch")
parser.add_argument("--width", type=int, help="the width of the output patch")
args = parser.parse_args()

# Read input
if args.height:
    patch_height = args.height
if args.width:
    patch_width = args.width

folder_name = yellow_page[args.dataset]
f1 = open('data/crop/' + folder_name + '/img1_list.txt', 'r')
f2 = open('data/crop/' + folder_name + '/img2_list.txt', 'r')
f = open('data/crop/' + folder_name + '/flo_list.txt', 'r')
params1 = f1.readline()
params2 = f2.readline()
params3 = f.readline()

# sanity check
if params1 == params2 == params3:
    words = params1.split()
    canvas_height = int(words[0])
    canvas_width = int(words[1])
    maximum_length = int(words[2])
else:
    print 'input files do not match!'
    raise

if args.length <= maximum_length:
    length = args.length
else:
    print "exceed size of the dataset!"
    raise

# Prepare Output
g1 = open('img1_list.txt', 'wb')
g2 = open('img2_list.txt', 'wb')
g = open('flo_list.txt', 'wb')
output_dir = 'out'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
img1_input = f1.readlines()
img2_input = f2.readlines()
flow_input = f.readlines()

# Generate
for i in range(length):
    x_locations = np.random.randint(0, canvas_width - patch_width, size=10)
    y_locations = np.random.randint(0, canvas_height - patch_height, size=10)
    img1 = Image.open(img1_input[i].strip())
    img2 = Image.open(img2_input[i].strip())
    if flow_input[i].strip().find('.png') != -1:
        flow = kittitool.flow_read(flow_input[i].strip())
    else:
        flow = fl.read_flow(flow_input[i].strip())
    for (x, y) in zip(x_locations, y_locations):
        patch_img1 = img1.crop((x, y, x+patch_width, y+patch_height))
        patch_img2 = img2.crop((x, y, x+patch_width, y+patch_height))
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

# close the program
f1.close()
f2.close()
f.close()
g1.close()
g2.close()
g.close()

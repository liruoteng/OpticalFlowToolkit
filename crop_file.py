#!/usr/bin/python
"""
crop_file.py
This file crops flow file (.flo) and image pairs into into patches according to the given locations
Author: Li Ruoteng
Date: 16 Oct 2016
"""

import os
import argparse
import numpy as np
from PIL import Image
from lib import flowlib as fl

parser = argparse.ArgumentParser(description='Crop optical flow and image pairs according to locations')
parser.add_argument('input_dir', type=str, help="The directory to search for flow files")
parser.add_argument('output_dir', type=str, help='the output directory')
parser.add_argument('x', type=int, help='the top left point on the image to start the crop')
parser.add_argument('y', type=int, help='the top left point on the image to start the crop')
parser.add_argument('h', type=int, help='crop size')
parser.add_argument('w', type=int, help='crop size')
parser.add_argument('--image_format', type=str, help="The format of the image files")
parser.add_argument('--flow_format', type=str, help="The format of the flow files")
args = parser.parse_args()

if not args.image_format:
    args.image_format = '.png'

if not args.flow_format:
    args.flow_format = '.flo'
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

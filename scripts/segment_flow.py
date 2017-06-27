#!/usr/bin/python
"""
segment_flow.py
This file convert flow file (.flo) into into flow class file according to the direction of the flow
Author: Li Ruoteng
Date: 16 Oct 2016
"""

import os
import argparse
import numpy as np
from PIL import Image
from lib import flowlib as fl

parser = argparse.ArgumentParser(description='Segment optical flow by orientation')
parser.add_argument('flow_format', type=str, help="The format of the files you want to search for")
parser.add_argument('input_dir', type=str, help="The directory to search for flow files")
parser.add_argument('--output_dir', type=str, help='the output directory')
args = parser.parse_args()

if args.output_dir:
    args.output_dir = './segment_flow/'

if not os.path.exists(args.output_dir):
    os.mkdir(args.output_dir)

for file_name in os.listdir(args.input_dir):
    if file_name.find(args.flow_format) != -1:
        flow = fl.read_flow(os.path.join(args.input_dir, file_name))
        seg = fl.segment_flow(flow)
        seg_img = Image.fromarray(seg.astype(np.uint8))
        seg_img.save(os.path.join(args.output_dir, file_name[0:file_name.find(args.flow_format)] + '.png'))

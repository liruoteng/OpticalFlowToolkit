#!/usr/bin/python
"""
# create_flow_list.py
# This file creates a list of flow file paths in ascending order for CNN to read in
#  the output will be a single file: filelist.txt
# Author: Li Ruoteng
# Date: 16 Oct 2016
"""

import os
import argparse

parser = argparse.ArgumentParser(description='Generate a file containing a list of flow files for CNN to read')
parser.add_argument('format', type=str, help="The format of the files you want to search for")
parser.add_argument("--input_dir", type=str, help="The directory to search for flow files")
parser.add_argument('--output_dir', type=str, help='the output directory')
args = parser.parse_args()

file_list = []
if not args.input_dir:
    in_dir = os.path.abspath('./')
else:
    in_dir = os.path.abspath(args.input_dir)

if args.output_dir:
    output_file_path = os.path.join(args.output_dir, 'filelist.txt')
else:
    output_file_path = 'filelist.txt'
f = open(output_file_path, 'wb')

for root, dirs, files in os.walk(in_dir):
    if files:
        for file_name in files:
            if file_name.find(args.format) != -1:
                file_list.append(os.path.join(in_dir, root) + '/' + file_name)

file_list.sort()
for name in file_list:
    f.write(name)
    f.write('\n')

f.close()

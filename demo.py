#! /usr/bin/python
# Author: Ruoteng Li
# Date: 6th Aug 2016
"""
Demo.py
This file demonstrates how to use kittitool module to read
 and visualize flow file saved in kitti format .png
"""
from lib import kittitool

flow_file = 'devkit/matlab/data/flow_gt.png'
flow = kittitool.flow_read(flow_file)
kittitool.flow_visualize(flow, 'Y')


#! /usr/bin/python
# Author: Ruoteng Li
# Date: 6th Aug 2016
"""
Demo.py
This file demonstrates how to use kittitool module to read
 and visualize flow file saved in kitti format .png
"""
from lib import flowlib as fl

flow_file = 'data/example/flow_gt.png'
flow = fl.read_flow_png(flow_file)
fl.visualize_flow(flow, 'RGB')

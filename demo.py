#! /usr/bin/python
# Author: Ruoteng Li
# Date: 6th Aug 2016
"""
Demo.py
This file demonstrates how to use kittitool module to read
 and visualize flow file saved in kitti format .png
"""
from lib import flowlib as fl

# read kitti format optical flow file (.png)
print "Visualizing KITTI flow example ..."
flow_file_KITTI = 'data/example/KITTI/flow_gt.png'
flow_KITTI = fl.read_flow(flow_file_KITTI)
fl.visualize_flow(flow_KITTI) 

# read Middlebury format optical flow file (.flo)
print "Visualizing Middlebury flow example ..."
flow_file_Middlebury = 'data/example/Middlebury/flow_gt.flo'
flow_Middlebury = fl.read_flow(flow_file_Middlebury)
fl.visualize_flow(flow_Middlebury)

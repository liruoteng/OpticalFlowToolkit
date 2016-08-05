#! /usr/bin/python
# Author: Ruoteng Li
# Date: 6th Aug 2016

import kittitool


flow_file = 'devkit/matlab/data/flow_gt.png'
flow = kittitool.flow_read(flow_file)
kittitool.flow_visualize(flow, 'Y')

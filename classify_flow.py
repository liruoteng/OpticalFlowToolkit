#!/usr/bin/python
"""
classify_flow.py
This file convert flow file (.flo) into into flow class file according to the direction of the flow
"""

import flowlib as fl
import numpy as np
from sys import argv
import matplotlib.pyplot as plt

SMALLFLOW = 0.0
LARGEFLOW = 1e8


flow_file = 'data/flow10.flo'

flow = fl.read_flow(flow_file)
h = flow.shape[0]
w = flow.shape[1]
u = flow[:, :, 0]
v = flow[:, :, 1]

idx = ((abs(u) > LARGEFLOW) | (abs(v) > LARGEFLOW))
idx2 = (abs(u) == SMALLFLOW)
u[idx2] = 0.0001
tan_value = v / u

class1 = (tan_value < 1) & (tan_value >= 0) & (u > 0) & (v >= 0)
class2 = (tan_value >= 1) & (u >= 0) & (v >= 0)
class3 = (tan_value < -1) & (u <= 0) & (v >= 0)
class4 = (tan_value < 0) & (tan_value >= -1) & (u <0) & (v >=0)
class8 = (tan_value >= -1) & (tan_value < 0) & (u > 0) & (v <= 0)
class7 = (tan_value < -1) & (u >= 0) & (v <= 0)
class6 = (tan_value >= 1) & (u <= 0) & (v <= 0)
class5 = (tan_value >= 0) & (tan_value < 1) & (u < 0) & (v <= 0)

seg = np.zeros((h,w))

seg[class1] = 1
seg[class2] = 2
seg[class3] = 3
seg[class4] = 4
seg[class5] = 5
seg[class6] = 6
seg[class7] = 7
seg[class8] = 8
seg[idx] = 0


img = fl.flow_to_image(flow)
plt.figure()
plt.imshow(seg)
plt.figure()
plt.imshow(img)
plt.show()


#! /usr/bin/python
"""
# ==============================
# kittitool.py
# this file provides read/write and visualize functions of optical flow files in kitti format
# Author: Ruoteng Li
# Date: 6th Aug 2016
# ==============================
"""


import png
import numpy as np
import matplotlib.colors as cl
import matplotlib.pyplot as plt
from lib import flowlib as fl





def read_disp_png(disp_file):
    """
    Read kitti disp from .png file
    :param disp_file:
    :return:
    """
    image_object = png.Reader(filename=disp_file)
    image_direct = image_object.asDirect()
    image_data = list(image_direct[2])
    (w, h) = image_direct[3]['size']
    channel = len(image_data[0]) / w
    disp = np.zeros((h, w, channel), dtype=np.uint16)
    for i in range(len(image_data)):
        for j in range(channel):
            disp[i, :, j] = image_data[i][j::channel]
    return disp[:, :, 0] / 256

# TODO: function flow_write(flow_file)

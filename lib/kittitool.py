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

def write_disp_png(disp, fpath):
    """
    Write KITTI disparity in png
    """
    
    d = d.astype('float64')
    
    I = d*256
    I[np.where(d==0)] = 1
    I[np.where(I<0)] = 0
    I[np.where(I>65535)] = 0
    I = I.astype('uint16')

    W = png.Writer(width=disp.shape[1],
                   height=disp.shape[0],
                   bitdepth=16, 
                   planes=1)
       
    with open(fpath, 'wb') as disp_fil:
        W.write(disp_fil, I.reshape((-1, disp.shape[1])))

#!/usr/bin/python
"""
render_dataset.py
Run haze/rain rendering on the background image with default settings.
Author: Li Ruoteng
Date: 16 Oct 2016
"""
import os
import sys
import argparse
from lib import haze


class Dataset(object):

    def __init__(self, dataset_name='example'):
        self.dataset_path = os.path.join('data/render', dataset_name)
        self.left_image_files = open(self.dataset_path + '/left.txt', 'r').readlines()
        self.right_image_files = open(self.dataset_path + '/right.txt', 'r').readlines()
        self.left_disp_files = open(self.dataset_path + '/left_disp.txt', 'r').readlines()
        self.right_disp_files = open(self.dataset_path + '/right_disp.txt', 'r').readlines()
        self.left_rain_files = open(self.dataset_path + '/left_rain.txt', 'r').readlines()
        self.right_rain_files = open(self.dataset_path + '/right_rain.txt', 'r').readlines()
        self.image_num = len(self.left_image_files)

    def set_dataset(self, dataset_name):
        self.dataset_path = os.path.join('data/render', dataset_name)
        self.left_image_files = open(self.dataset_path + '/left.txt', 'r').readlines()
        self.right_image_files = open(self.dataset_path + '/right.txt', 'r').readlines()
        self.left_disp_files = open(self.dataset_path + '/left_disp.txt', 'r').readlines()
        self.right_disp_files = open(self.dataset_path + '/right_disp.txt', 'r').readlines()
        self.left_rain_files = open(self.dataset_path + '/left_rain.txt', 'r').readlines()
        self.right_rain_files = open(self.dataset_path + '/right_rain.txt', 'r').readlines()
        self.image_num = len(self.left_image_files)


def setup_haze_model(h, beta, contrast, intensity):
    h.set_beta(beta)
    h.set_haze_intensity(contrast)
    h.set_rain_intensity(intensity)


def render_dataset(h, d):
    for i in range(d.image_num):
        # set output file name
        left_bg_file = d.left_image_files[i]
        right_bg_file = d.right_image_files[i]
        left_out_file = left_bg_file[0: left_bg_file.find('.png')] + '_rain_haze.png'
        right_out_file = right_bg_file[0:right_bg_file.find('.png')] + '_rain_haze.png'
        # Set up haze model
        h.set_background(d.left_image_files[i].strip(), d.right_image_files[i])
        h.set_disparity_map(d.left_disp_files[i].strip(), d.right_disp_files[i].strip())
        h.set_rain_file(d.left_rain_files[i].strip(), d.right_rain_files[i].strip())
        h.set_all_output(left_out_file, right_out_file)
        # synthesize
        h.synthesize_all()


def render_drive_dataset(intensity=220, beta=5, contrast=130):
    d = Dataset('drive')
    h = haze.Haze()
    setup_haze_model(h, beta, contrast, intensity)
    render_dataset(h, d)


def render_kitti2012_dataset(intensity=220, beta=5, contrast=130):
    d = Dataset('kitti2012')
    h = haze.Haze()
    setup_haze_model(h, beta, contrast, intensity)
    render_dataset(h, d)


if __name__ == 'main':
    if len(sys.argv) <= 1:
        print "insufficient arguments"
        raise
    else:
        if sys.argv[1].lower() == 'kitti2012':
            render_kitti2012_dataset()
        elif sys.argv[1].lower() == 'drive':
            render_drive_dataset()





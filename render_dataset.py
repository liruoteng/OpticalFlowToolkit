#!/usr/bin/python
"""
render_dataset.py
Run haze/rain rendering on the background image with default settings.
Author: Li Ruoteng
Date: 16 Oct 2016
"""
from lib import haze


def render_drive_dataset():
    h = haze.Haze()
    intensity = 220
    beta = 5
    contrast = 130
    h.set_beta(beta)
    h.set_haze_intensity(contrast)
    h.set_rain_intensity(intensity)
    left_imagefile = open('data/left.txt', 'r')
    right_imagefile = open('data/right.txt', 'r')
    left_dispfile = open('data/left_disp.txt', 'r')
    right_dispfile = open('data/right_disp.txt', 'r')
    left_rainfiles = open('data/left_rain.txt', 'r')
    right_rainfiles = open('data/right_rain.txt', 'r')
    left_images = left_imagefile.readlines()
    right_images = right_imagefile.readlines()
    left_disp = left_dispfile.readlines()
    right_disp = right_dispfile.readlines()
    left_rain = left_rainfiles.readlines()
    right_rain = right_rainfiles.readlines()
    image_num = len(left_images)

    for i in range(image_num):
        left_bg_file = left_images[i]
        right_bg_file = right_images[i]
        h.set_background(left_bg_file.strip(), right_bg_file.strip())
        left_disp_file = left_disp[i]
        right_disp_file = right_disp[i]
        h.set_disparity_map(left_disp_file.strip(), right_disp_file.strip())
        left_rain_file = left_rain[i]
        right_rain_file = right_rain[i]
        h.set_rain_file(left_rain_file.strip(), right_rain_file.strip())
        left_out_file = left_bg_file[0: left_bg_file.find('.png')] + '_rain_haze.png'
        right_out_file = right_bg_file[0:right_bg_file.find('.png')] + '_rain_haze.png'
        h.set_all_output(left_out_file, right_out_file)
        h.synthesize_all()
        print left_bg_file, ':', right_bg_file
        print left_out_file, ':', right_out_file


def render_kitti_dataset():
    

    

# Initialize haze model object
haze_object = haze.Haze()
# Parameter set up as followed
# haze_object.set_beta(65)
# haze_object.set_noise_param(0, 10)
# Generate haze rendered output
haze_object.synthesize_haze()
# Generate rain rendered output
haze_object.synthesize_rain()
# Generate rain and haze both rendered output
haze_object.synthesize_all()
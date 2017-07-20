# OPTICAL FLOW TOOLKIT v0.1
#### RUOTENG LI                                  
#### 20 July 2016                                 


This toolkit is a python implementation for read, write, calculate, and visualize
KITTI 2012 Optical Flow, which contains
200 training and 200 test image pairs each. Ground truth has been aquired by 
accumulating 3D point clouds from a 360 degree Velodyne HDL-64 Laserscanner 
according to Andreas Geiger []. 

### File description:
=================

- lib/kittitool.py     : toolkit for KITTI optical flow dataset
- demo.py          : demonstration on read and visualize KITTI optical flow data
- lib/flowlib.py       : library for manipulate optical flow
...


### 1. Pre-Requisite:

1. Python2.7
2. Numpy and Scipy
3. Matplotlib
4. pypng package


### 2. Installation:
#### 2.1 Installing Python and Pip
You may want to get started on a Unix environment such as Ubuntu, or Linux OS, and use pip to manage python package installation. [pip installation guide](https://pip.pypa.io/en/stable/installing/)
Briefly for Linux user:
```
python get-pip.py
```
#### 2.2 Install Scipy Numpy

```
sudo pip install scipy
sudo pip install numpy
```

#### 2.3 Install Matplotlib
```
pip install matplotlib
```

#### 2.4 Install PyPng
```
sudo pip install pypng
```

### 3. Usage
```
python demo.py
```

### 4. Scripts for Training Loss Visualization
In your terminal, locate the root directory of this repository,  type the following 
```
cd scripts/
python plot_loss.py <YOUR TRAINING LOG FILE>
```
The plot will be saved with the same name of your logfile in .png format.

### 5. Scripts for Data Manipulation

#### 5.1 random_crop.py
This program crops the original image data set into small patches specified by the input, by default the size is 384x512 (px). Please make sure that your input image is larger than the patches you want to get. The cropping distribution is uniform across the entire image.

```
python random_crop.py <name_of_dataset> <number_of_patches> --height <height_of_output_patch> --width <width_of_output_patch>
```
The patches will be generated at <out> folder and the following files will be generated for CNN training:
- flo_list.txt
- img1_list.txt
- img2_list.txt

#### 5.2 create_filelist
This program create three file lists that containing all the paths of the images/flow files from a dataset. The output of this program will be one single file "filelist.txt" that contains the file path you want to search in the dataset.

```
python create_filelist.py <file_format> --input_dir <path_of_dataset> --output_dir <output_path>
```

#### 5.3 crop_flow.py
This program crops the image files and flow files from a dataset at a specific location. 

``` 
python crop_flow.py <input_dir> <output_dir> <x> <y> <height_of_patch> <width_of_patch> --image_format <format_of_image> --flow_format <format_of_flow>

```
#### 5.4 segment_flow.py
This script segment the flow into 9 classes according to the flow orientation. Each 45 degree will be recognized into one class starting from 0 degree on x axis.

```
python segment_flow.py <format_of_flowfile> <input_directory> --output_dir <output_directory>
```



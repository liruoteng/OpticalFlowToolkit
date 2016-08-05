# THE KITTI VISION BENCHMARK SUITE: STEREO AND OPTICAL FLOW BENCHMARK
#### RUOTENG LI                                  
#### 6th Aug 2016                                 


This toolkit is a python implementation for read, write, calculate, and visualize
KITTI 2012 Optical Flow, which contains
200 training and 200 test image pairs each. Ground truth has been aquired by 
accumulating 3D point clouds from a 360 degree Velodyne HDL-64 Laserscanner 
according to Andreas Geiger []. 

### File description:
=================

- flow_read.py     : read flow .png file 
- flow_write.py    : write flow into .png file, same format as KITTI benchmark
- flow_visual.py   : visualize optical flow into YCbCr mode or RGB mode.
- flow_error.py    : calculate estimated flow error according to ground truth
...


### 1. Pre-Requisite:

1. Python2.7
2. Numpy and Scipy
3. pypng package


### 2. Installation:
####2.1 Installing Python and Pip
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

#### 2.3 Install PyPng
```
sudo pip install pypng
```

### 3. Usage
```
python demo.py
```



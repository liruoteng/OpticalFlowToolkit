# OPTICAL FLOW TOOLKIT v0.1
#### RUOTENG LI                                  
#### 6th Aug 2016                                 


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



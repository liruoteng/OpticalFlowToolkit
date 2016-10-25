#! /usr/bin/python
"""
Collect drive data set files
"""
import os


f = open('left_flow.txt', 'wb')
g = open('right_flow.txt', 'wb')
left = []
right = []

for root, dirs, files in os.walk('../../../data/drive/drive_flow'):
    for dirname in dirs:
        if dirname == 'left':
            files = os.listdir(root + '/left')
            for filename in files:
                if filename.find('flo') != -1:
                    left.append(os.path.join(root + '/left', filename))
        elif dirname == 'right':
            files = os.listdir(root + '/right')
            for filename in files:
                if filename.find('flo') != -1:
                    right.append(os.path.join(root + '/right', filename))

left.sort()
right.sort()

for line in left:
    f.write(line + '\n')
for line in right:
    g.write(line + '\n')

f.close()
g.close()






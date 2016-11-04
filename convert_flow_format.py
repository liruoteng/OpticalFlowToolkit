from lib import flowlib as fl
from lib import pfm
import numpy as np
"""
Massively convert pfm flow file into flo type
Author : Ruoteng LI
Data 6 Oct 2016
"""

f = open('data/left_flow.txt', 'r')
lines = f.readlines()
i = 0

for line in lines:
    print i
    fl.pfm_to_flo(line.strip())
    i += 1

f.close()

f = open('data/right_flow.txt', 'r')
lines = f.readlines()
i = 0

for line in lines:
    print i
    fl.pfm_to_flo(line.strip())
    i += 1

f.close()


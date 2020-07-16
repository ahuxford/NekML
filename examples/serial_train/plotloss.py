#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plots the ModelLoss .h5 file over timesteps
"""

import numpy as np
import h5py
import matplotlib.pyplot as plt

# set variables
path_loss = './ModelLoss.h5'

h5f  = h5py.File(path_loss, 'r')
for key in h5f:
    if key=='0':
        loss = h5f[key][:]
    else:
        loss = np.append(loss,h5f[key][:])
        
h5f.close()

N = len(loss)

plt.semilogy(np.linspace(1,N,N),loss,label='train on-the-fly')
plt.xlabel('Epoch')
plt.ylabel('MSE loss')
plt.title('Loss versus epoch for 1000 epochs each timestep')
plt.show()

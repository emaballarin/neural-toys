#!/usr/bin/python
# -*- coding: utf-8 -*-

# CircleGen - Circular multivariate data generator (gaussian + uniform noise) for scatter-plot
# Copyright (c) 2016 Emanuele Ballarin
# Software released under the terms of the MIT License

import random  # For random number generation on a system-wide level
import math  # For the use of mathematical functions
import matplotlib.pyplot as plt  # For data plotting

# The purpose of the script is to generate couples of real-valued numbers to be
# used as Cartesian planar coordinates. The points are scattered with a Gaussian
# PDF, peaked on a circumference of given radius, and disturbed by uniform noise
# in the whole plane.

# OUTPUT OF THE PROGRAM
datarray = []  # Initialized as empty

# Constants
radius = 100.0
gmu = 0.0
gsigma = (25.0/3.0)
pi = math.pi

# Number of points
Ndata = 1000
Nnoise = 0

# Randomness stuff
random.SystemRandom()  # initializes system-wide RNG

# Data generation (significant data)
for i in range(0, Ndata):
    angle = 0.0  # Radians
    rbias = 0.0
    rfinal = 0.0
    rbias = random.gauss(gmu, gsigma)  # Gaussian bias as defined above
    rfinal = rbias + radius
    angle = random.uniform(0.0, 2.0*pi)  # Random angle
    point = [rfinal*math.cos(angle), rfinal*math.sin(angle)]
    datarray.append(point)

# Data generation (noise)
for j in range(0, Nnoise):
    point = [random.uniform(-150.0, 150.0), random.uniform(-150.0, 150.0)]
    datarray.append(point)

# Writing to file
file = open('datagen.txt', 'w')

for k in range(0, len(datarray)):
    file.write(str(datarray[k][0]) + " " + str(datarray[k][1]) + "\n")

file.close()

# Plotting
for k in range(0, len(datarray)):
    plt.scatter(datarray[k][0], datarray[k][1])

plt.axes().set_aspect('equal')
plt.show()

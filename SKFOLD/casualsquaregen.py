#!/usr/bin/python
# -*- coding: utf-8 -*-

# GausSquareGem - Squared multinormal (2D) data generator for scatter-plot
# Copyright (c) 2016 Emanuele Ballarin
# Software released under the terms of the MIT License

import random  # For random number generation on a system-wide level
import math  # For the use of mathematical functions
import matplotlib.pyplot as plt  # For data plotting

# The purpose of the script is to generate couples of real-valued numbers to be
# used as Cartesian planar coordinates.

# OUTPUT OF THE PROGRAM
datarray = []  # Initialized as empty

# Constants
sqside = 300  # Side of the square

# Number of points per square
Nsteps = 200
Npoints = 10

# Randomness stuff
random.SystemRandom()  # initializes system-wide RNG

# Data generation (significant data)

for i in range(0, Nsteps):

    diag_stop = random.gauss(0.0, 2*math.sqrt(2)*sqside/3.0)

    for j in range(0, Npoints):
        x_axis = random.gauss(0, 2*sqside/3.0)
        y_axis = diag_stop/math.sqrt(2.0)
        point = [x_axis, y_axis]
        datarray.append(point)

        x_axis = diag_stop/math.sqrt(2.0)
        y_axis = random.gauss(0, 2*sqside/3.0)
        point = [x_axis, y_axis]
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

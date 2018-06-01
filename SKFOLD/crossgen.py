#!/usr/bin/python
# -*- coding: utf-8 -*-

# CrossGen - Cross-shaped multivariate data generator (uniform) for scatter-plot
# Copyright (c) 2016 Emanuele Ballarin
# Software released under the terms of the MIT License

import random  # For random number generation on a system-wide level
import math  # For the use of mathematical functions
import matplotlib.pyplot as plt  # For data plotting

# The purpose of the script is to generate couples of real-valued numbers to be
# used as Cartesian planar coordinates. The points are scattered with a cross-shaped
# spatial distribution.

# OUTPUT OF THE PROGRAM
datarray = []  # Initialized as empty

# Constants
sqside = 100  # Side of the 1/5 cross square

# Number of points per square
Ndata = 600

# Randomness stuff
random.SystemRandom()  # initializes system-wide RNG

# Data generation (significant data)
iteration = 1

while iteration <= 5:

    if iteration == 1:
        x_start = -sqside/2.0
        x_stop = sqside/2.0
        y_start = 3.0*sqside/2.0
        y_stop = sqside/2.0

    elif iteration == 2:
        x_start = -sqside/2.0
        x_stop = sqside/2.0
        y_start = -sqside/2.0
        y_stop = -3.0*sqside/2.0

    elif iteration == 3:
        y_start = sqside/2.0
        y_stop = -sqside/2.0
        x_start = -3.0*sqside/2.0
        x_stop = -sqside/2.0

    elif iteration == 4:
        y_start = sqside/2.0
        y_stop = -sqside/2.0
        x_start = sqside/2.0
        x_stop = 3.0*sqside/2.0

    elif iteration == 5:
        x_start = -sqside/2.0
        x_stop = sqside/2.0
        y_start = sqside/2.0
        y_stop = -sqside/2.0

    for i in range(0, Ndata):

        x_axis = random.uniform(x_start, x_stop)
        y_axis = random.uniform(y_start, y_stop)
        point = [x_axis, y_axis]
        datarray.append(point)

    iteration = iteration + 1

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

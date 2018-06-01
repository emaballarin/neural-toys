#!/usr/bin/python
# -*- coding: utf-8 -*-

# SKFOLD - Self-organizing Kohonen principal-mainFOLD-approximation map
# Copyright (c) 2016 Emanuele Ballarin <emanuele@ballarin.cc>
# Software released under the terms of the MIT License

# MODULES IMPORT

import random
import math
import sys
import matplotlib.pyplot as plt

# The purpose of the script is to build and drive a Self-Organizing Map (SOM)
# which generalizes the Principal Component Analysis (PCA) approach in the
# elaboration of data points, arbitrarily distributed in 2 dimensions.
# The net is bidimensional, and at the end of the self-training process it
# displaces itself so as it lies on the principal plane that best explains
# the overall dataset variance.
# The net has a fixed structure and evolves following Teuvo Kohonen's
# algorithm, in an exponentially-decaying time- and learning-rate- adaptive
# fashion.

# BEGINNING OF CODE

# TWEAKABLES
Nrow = 4  # Number of rows in the map
Ncol = 50  # Number of columns in the map

epsilon = 0.2  # Normalized learning rate (starting)
sigma = 18  # Gaussian spread index (starting)

epsdecay = 0.999  # N.L.R. (epsilon) exponential decay factor
sigdecay = 0.96  # G.S.I. (sigma) exponential decay factor

thresh = 500  # Iterations before decay enactment
effzero = 0.1  # 0.05  # Learning ends when N.L.R. is equal (or less) to it

# OUTPUT OF THE PROGRAM
neurmap = []  # List of couple-listed neurons' coordinates (in the xy plane)

# PRELIMINARIES
# Functions
def eudist(a, b):
    """ The function calculates the Euclidean Distance in two dimensions """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def mhdistsq(a, b):
    """ The function computes the 'Squared Manhattan Distance' in two dimensions """
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)

def vecsum(a, b):
    """ The function computes the vector sum in two dimensions """
    return [a[0] + b[0], a[1] + b[1]]

def vecdiff(a, b):
    """ The function computes the vector difference in two dimensions """
    return [a[0] - b[0], a[1] - b[1]]

# Data acquisition
dataset = []  # Initialized empty

with open('datagen.txt', 'r') as source:
    for line in source:
        buff = list(map(float, line.split()))  # Maps each line into couple...
        dataset.append(buff)  # ...and appends the list (couple) to dataset

Npoints = len(dataset)  # Computes the dataset lenght

# NEURAL DRIVE
# Randomness stuff
random.SystemRandom()  # initializes system-wide RNG

# Neuron Array Initialization
neurons = []

for row in range(0, Nrow):  # Array builder
    neurons.append([])
    for col in range(0, Ncol):
        neurons[row].append([])

# Random Neuron Placing
for row in range(0, Nrow):
    for col in range(0, Ncol):
        neurons[row][col] = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]

# Distance Matrix Initialization
distmatrix = []
for row in range(0, Nrow):  # Array builder
    distmatrix.append([])
    for col in range(0, Ncol):
        distmatrix[row].append([])

# Manhattan Matrix Initialization
manhattan = []
for row in range(0, Nrow):  # Array builder
    manhattan.append([])
    for col in range(0, Ncol):
        manhattan[row].append([])

# F-Matrix Initialization
fmat = []
for row in range(0, Nrow):  # Array builder
    fmat.append([])
    for col in range(0, Ncol):
        fmat[row].append([])

# Additive Weight Matrix Building
wm = []
for row in range(0, Nrow):  # Array builder
    wm.append([])
    for col in range(0, Ncol):
        wm[row].append([])

# Iterative Evolution

iteration = 0
threshold = thresh
RunAgain = True

while RunAgain:

    while iteration < threshold:
        # Random Example Extraction
        draw = random.randrange(0, Npoints)
        example = dataset[draw]

        # Distance Matrix Building
        for row in range(0, Nrow):
            for col in range(0, Ncol):
                distmatrix[row][col] = eudist(example, neurons[row][col])

        # Winner Neuron Challenge
        nearest = sys.float_info.max
        for row in range(0, Nrow):
            for col in range(0, Ncol):
                if distmatrix[row][col] < nearest:
                    nearest = distmatrix[row][col]
                    winner = [row, col]

        # Manhattan Matrix Building (to winner neuron)
        for row in range(0, Nrow):
            for col in range(0, Ncol):
                pholder = [row, col]
                manhattan[row][col] = mhdistsq(winner, pholder)

        # F-Matrix Building (to winner neuron)
        for row in range(0, Nrow):
            for col in range(0, Ncol):
                fmat[row][col] = math.exp(((-1.0)*(manhattan[row][col]))/(2*(sigma**2)))

        # Additive Weight Matrix Building
        for row in range(0, Nrow):
            for col in range(0, Ncol):
                wm[row][col] = (vecdiff(example, neurons[row][col]))
                wm[row][col][0] = (wm[row][col][0])*(epsilon)*(fmat[row][col])
                wm[row][col][1] = (wm[row][col][1])*(epsilon)*(fmat[row][col])

        # Weight update
        for row in range(0, Nrow):
            for col in range(0, Ncol):
                neurons[row][col] = vecsum(neurons[row][col], wm[row][col])

        # Counter update
        iteration = iteration + 1

    # Outer cycle follows here
    print("Completed " + str(iteration) + " iterations")
    if epsilon <= effzero:  # Check if epsilon is almost zero
        RunAgain = False

    epsilon = epsilon*epsdecay  # Update parameters
    sigma = sigma*sigdecay

    threshold = threshold + thresh

# FINALIZATION
# Outputting
neurmap = neurons

# Re-outputting the dimensionally-reduced dataset to file
file = open('reduced_dataset.txt', 'w')

for row in range(0, Nrow):
    for col in range(0, Ncol):
        file.write(str(neurmap[row][col][0]) + " " + str(neurmap[row][col][1]) + "\n")

file.close()

# Printing to show the job done
for iterable in range(0, len(dataset)):
    plt.scatter(dataset[iterable][0], dataset[iterable][1], color='red')  # Original dataset

for row in range(0, Nrow):
    for col in range(0, Ncol):
        plt.scatter(neurmap[row][col][0], neurmap[row][col][1], color='black')  # Reduced dataset

plt.axes().set_aspect('equal')
plt.show()

# END OF CODE

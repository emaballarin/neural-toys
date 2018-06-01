#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# START OF CODE

dataset = []  # Initialized empty
reduced_dataset = []  # Initialized empty

with open('datagen.txt', 'r') as source:
    for line in source:
        buff = list(map(float, line.split()))  # Maps each line into couple...
        dataset.append(buff)  # ...and appends the list (couple) to dataset

Npoints_ods = len(dataset)  # Computes the dataset lenght

with open('reduced_dataset.txt', 'r') as source:
    for line in source:
        buff = list(map(float, line.split()))  # Maps each line into couple...
        reduced_dataset.append(buff)  # ...and appends the list (couple) to dataset

Npoints_rds = len(dataset)  # Computes the dataset lenght

# Printing to show the job done
for iterable in range(0, len(dataset)):
    plt.scatter(dataset[iterable][0], dataset[iterable][1], color='red')  # Original dataset

# Printing to show the job done
for iterable in range(0, len(reduced_dataset)):
    plt.scatter(reduced_dataset[iterable][0], reduced_dataset[iterable][1], color='black')  # Reduced dataset

plt.axes().set_aspect('equal')
plt.show()

# END OF CODE

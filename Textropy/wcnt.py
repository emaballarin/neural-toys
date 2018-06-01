#!/usr/bin/python
# -*- coding: utf-8 -*-

# wcnt - A spartan word counter
# (C) 2016 - Emanuele Ballarin <emanuele@ballarin.cc>

words = 0

with open('file.txt', 'r') as text:  # File opening is already I/O buffered ;-)
    for line in text:
        words = words + len(line)

print(" ")  # This empty lines are just typesetting-sugar
print("Number of Words: ", words)

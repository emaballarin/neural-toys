#!/usr/bin/python
# -*- coding: utf-8 -*-

# textropy - An efficient word entropy calculator
# (C) 2016 - Emanuele Ballarin <emanuele@ballarin.cc>

import math  # Necessary to invoke logarithmic functions
import re   # Necessary to use regular expressions in word parsing

wordlist = list()
wordcount = list()
probability = list()
entropy = 0.0  # Trivial message (no message) entropy must be zero

with open('file.txt', 'r') as text:  # File opening is already I/O buffered ;-)
    for line in text:
        line = line.lower()  # Uppercase or lowercase words must be the same
        # Following line contains a RegExp - Contracted words must count as one
        for word in re.findall(r"[\w']+", line):
            if word in wordlist:
                wordcount[wordlist.index(word)] = wordcount[wordlist.index(word)] + 1
            else:
                wordlist.append(word)
                wordcount.append(1)

wordlist.sort()  # The wordlist must be alphabetically-ordered to proceed

if wordlist[0] == "'":  # If the wordlist contains the word "'"...
    del wordlist[0]  # ...it should be removed...
    del wordcount[0]  # ...like its counter.

textlenght = sum(wordcount)
for step1 in wordcount:
    probability.append(step1/textlenght)
for step2 in probability:
    entropy = entropy + (step2 * math.log((1.0 / step2), 2))

print(" ")  # This empty lines are just typesetting-sugar
print("WORDLIST USED: ")
print(" ")
print(wordlist)
print(" ")
print(" ")
print("Source single-word entropy (Shannon): ", entropy)

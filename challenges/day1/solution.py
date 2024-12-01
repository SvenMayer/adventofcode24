#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:27:00 2024

@author: sven
"""
import numpy as np


data = np.genfromtxt("../../inputs/day1/input", delimiter="   ", dtype=int)
l1 = data[:,0]
l2 = data[:,1]
l1.sort()
l2.sort()
d = np.cumsum(abs(l1-l2))[-1]
print(d)


l2 = [itm for itm in l2]
s1 = set(l1)
s = 0
for itm in s1:
    s += itm * l2.count(itm)
print(s)
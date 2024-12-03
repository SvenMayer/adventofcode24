#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:39:01 2024

@author: sven
"""
import re


ex = re.compile("mul\((\d+),(\d+)\)")

with open("../../inputs/day3/input", "r") as fid:
    data = fid.read()

idx1 = 0
idx2 = 0
res = 0
while (idx2 != -1 and idx1 != -1):
    try:
        idx2 = data.index("don't()", idx1)
    except ValueError:
        idx2 = -1
    for x1, x2 in ex.findall(data[idx1:idx2]):
        res += int(x1)*int(x2)
    try:
        idx1 = data.index("do()", idx2)
    except ValueError:
        idx1 = -1
print(res)


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

res = 0
for x1, x2 in ex.findall(data):
    res += int(x1)*int(x2)
print(res)


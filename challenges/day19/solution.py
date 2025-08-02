#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 22:30:22 2025

@author: sven
"""
import functools

with open("../../inputs/day19/input", "r") as fid:
    data = fid.read()

towels, combinations = data.split("\n\n")
towels = [itm.strip() for itm in towels.split(",")]


@functools.lru_cache
def apply_towels(pattern):
    global towels
    if len(pattern) == 0:
        return 1
    res = 0
    for t in towels:
        if pattern.startswith(t):
            new_pattern = pattern[len(t):]
            res += apply_towels(new_pattern)
    return res


res1 = 0
res2 = 0
for idx, comb in enumerate(combinations.split("\n")):
    if len(comb) == 0:
        continue
    r = apply_towels(comb)
    if r:
        res1 += 1
        res2 += r


print("Solution 1")
print(res1)

print("Solution 2")
print(res2)

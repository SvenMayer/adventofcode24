#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:17:32 2024

@author: sven
"""
TEST_DATA = """2333133121414131402
"""

with open("../../inputs/day9/input", "r") as fid:
    raw_data = fid.read()

# raw_data = TEST_DATA

sz = 0
for n in raw_data:
    if n == "\n":
        continue
    sz += int(n)

memory = sz * [None]
ptr = 0
i = 0
fctr = 0
while ptr < sz:
    if i % 2 == 1:
        ptr += int(raw_data[i])
    else:
        for j in range(int(raw_data[i])):
            memory[ptr] = fctr
            ptr += 1
        fctr += 1
    i += 1


i = 0
j = len(memory) - 1
while True:
    while memory[i] is not None:
        i += 1
    while memory[j] is None:
        j -= 1
    if i >= j:
        break
    memory[i] = memory[j]
    memory[j] = None


res = 0
for i, v in enumerate(memory):
    if memory[i] is None:
        break
    res += i * v
print(res)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:25:16 2024

@author: sven
"""
import functools
import numpy as np


TEST_DATA = """125 17
"""

with open("../../inputs/day11/input", "r") as fid:
    raw_data = fid.read()

# raw_data = TEST_DATA

N10 = np.log(10)


@functools.cache
def handle_stone(stone):
    if stone == 0:
        return [1]
    ndigits = int(np.log(stone) / N10) + 1
    if ndigits % 2 == 0:
        cmp = 10 ** (ndigits // 2)
        return [stone // cmp, stone % cmp]
    return [stone * 2024]


@functools.cache
def resolve2(stone, N):
    if N == 0:
        return 1
    res = 0
    for s in handle_stone(stone):
        res += resolve2(s, N-1)
    return res


def parse_data(raw_data):
    return [int(itm) for itm in raw_data.strip().split(" ")]


res = 0
for s in parse_data(raw_data):
    res += resolve2(s, 75)
print(res)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:52:25 2024

@author: sven
"""
import numpy as np


TEST_DATA = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


N10 = np.log(10)

with open("../../inputs/day7/input", "r") as fid:
    raw_data = fid.read()


# raw_data = TEST_DATA


def solve(cmp, list):
    if len(list) == 1:
        return list[0] == cmp
    if list[0] > cmp:
        return False
    newlistmult =  [list[0] * list[1]] + list[2:]
    newlistadd = [list[0] + list[1]] + list[2:]
    o = int(np.log(list[1])/N10) + 1
    newlistconc = [list[0] * 10**o + list[1]] + list[2:]
    return solve(cmp, newlistmult) or solve(cmp, newlistadd) or solve(cmp, newlistconc)


def parse_input(inp):
    res = []
    for ln in inp.split("\n"):
        if len(ln) == 0:
            continue
        cmp_str, values_str = ln.split(":")
        res.append((int(cmp_str), [int(itm) for itm in values_str.strip().split(" ")]))
    return res


data = parse_input(raw_data)
res = 0
for itm in data:
    if solve(itm[0], itm[1]):
        res += itm[0]


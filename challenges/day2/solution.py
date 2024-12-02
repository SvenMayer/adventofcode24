#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:28:37 2024

@author: sven
"""
import numpy as np

with open("../../inputs/day2/input", "r") as fid:
    data = fid.read()



def check_report(report):
    d_level = np.diff(report)
    if 0 in d_level:
        # one step does change: unsafe
        return False
    dmax = np.max(d_level)
    dmin = np.min(d_level)
    if dmax * dmin < 0:
        # increasing and decreasing: unsafe
        return False
    if dmax > 3 or dmin < -3:
        #step size more than 3: unsafe
        return False
    # made it here: safe
    return True


def solution1(data):
    safe_ct = 0
    for ln in data.split("\n"):
        if len(ln) == 0:
            continue
        if check_report(np.fromstring(ln, int, -1, " ")):
            safe_ct += 1
    return safe_ct


def solution2(data):
    safe_ct = 0
    for ln in data.split("\n"):
        if len(ln) == 0:
            continue
        report = np.fromstring(ln, int, -1, " ")
        rpts = [report] + [np.r_[report[:i], report[i+1:]] for i in range(len(report))]
        for r in rpts:
            if check_report(r) is True:
                safe_ct += 1
                break
    return safe_ct


print(solution1(data))
print(solution2(data))

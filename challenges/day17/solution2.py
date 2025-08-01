#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 22:24:52 2025

@author: sven
"""
A = 0
B = 0
C = 0

instptr = 0
outstr = ""


with open("../../inputs/day17/input", "r") as fid:
    data = fid.read()
for ln in data.split("\n"):
    if len(ln.strip()) == 0:
        continue
    name, value = ln.split(":")
    if name.startswith("Register"):
        if name.endswith("A"):
            A = int(value.strip())
        elif name.endswith("B"):
            B = int(value.strip())
        elif name.endswith("C"):
            C = int(value.strip())
    elif name.startswith("Program"):
        inst = [int(itm) for itm in value.strip().split(",")]

res = []


def add_v(i, A, mask):
    global inst
    if i == -1:
        global res
        res.append(A)
        return
    v = inst[i]
    for C in range(8):
        B3 = v ^ 7 ^ C
        B1 = B3 ^ 2
        A = (A << 3) + B1
        mask = (mask << 3) + 7
        if (mask & (7<<B3) & A) == (mask & (C<<B3)):
            mask |= (7<<B3)
            A |= (C<<B3)
            add_v(i-1, A, mask)
        A = A >> 3
        mask = mask >> 3


add_v(len(inst)-1, 0, 7)
print(sorted(res)[0])

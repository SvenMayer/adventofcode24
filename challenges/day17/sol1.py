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


inst = []


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


def combo(v):
    global A, B, C
    if v < 4:
        return v
    elif v == 4:
        return A
    elif v == 5:
        return B
    elif v == 6:
        return C
    raise TypeError("Invalid combo operator type")


def adv(op):
    global A, B, C, instptr
    A = A // 2**combo(op)


def bxl(op):
    global A, B, C, instptr
    B = B^op


def bst(op):
    global A, B, C, instptr
    B = combo(op) % 8


def jnz(op):
    global A, B, C, instptr
    if A != 0:
        instptr = op - 2


def bxc(op):
    global A, B, C, instptr
    B = B^C


def out(op):
    global outstr
    outstr += str(combo(op) % 8) + ","


def bdv(op):
    global A, B, C, instptr
    B = A // 2**combo(op)


def cdv(op):
    global A, B, C, instptr
    C = A // 2**combo(op)


INSTLIST = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


if __name__ == "__main__":
    while True:
        if instptr >= len(inst):
            break
        INSTLIST[inst[instptr]](inst[instptr+1])
        instptr += 2
    print(outstr[:-1])
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:04:18 2024

@author: sven
"""
TEST_DATA = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

with open("../../inputs/day4/input", "r") as fid:
    data = fid.read()

# data = TEST_DATA


LINE_LEN = data.index("\n") + 1

data = LINE_LEN * " " + data + LINE_LEN * " "


def nextpos(pos):
    return [
        [pos-i*(LINE_LEN + 1) for i in range(4)],
        [pos-i*(LINE_LEN) for i in range(4)],
        [pos-i*(LINE_LEN - 1) for i in range(4)],
        [pos-i for i in range(4)],
        [pos+i for i in range(4)],
        [pos+i*(LINE_LEN - 1) for i in range(4)],
        [pos+i*(LINE_LEN) for i in range(4)],
        [pos+i*(LINE_LEN + 1) for i in range(4)],
        ]


def diag(pos):
    p0 = pos - LINE_LEN - 1
    p1 = pos - LINE_LEN + 1
    p2 = pos + LINE_LEN + 1
    p3 = pos + LINE_LEN - 1
    return data[p0] + data[p2], data[p1] + data[p3]


def isxmas(pos):
    for i, letter in enumerate("XMAS"):
        if data[pos[i]] != letter:
            return False
    return True



xmasct = 0
for i in range(len(data)):
    for wd in nextpos(i):
        if isxmas(wd):
            xmasct += 1


masxct = 0
for pos in range(len(data)):
    if data[pos] == "A":
        diag1, diag2 = diag(pos)
        if ("MS" == diag1 or "SM" == diag1) and ("MS" == diag2 or "SM" == diag2):
            masxct += 1


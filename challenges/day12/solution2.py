#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:59:36 2024

@author: sven
"""
TEST_DATA = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

TEST_DATA2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

TEST_DATA3 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""


with open("../../inputs/day12/input", "r") as fid:
    raw_data = fid.read()


#raw_data = TEST_DATA3

LINE_LEN = raw_data.index("\n") + 1
COL_LEN = raw_data.count("\n")
ORIENTATION = [-LINE_LEN, -1, LINE_LEN, 1]

raw_data = LINE_LEN * "\n" + raw_data + LINE_LEN * "\n"


SEEN = []


def count_corners(data, pos):
    f = data[pos]
    c = 0
    if data[pos-LINE_LEN] != f:
        if data[pos+1] != f:
            c += 1
        if data[pos-1] != f:
            c += 1
    if data[pos+LINE_LEN] != f:
        if data[pos+1] != f:
            c += 1
        if data[pos-1] != f:
            c += 1
    if data[pos+LINE_LEN] == f and data[pos+1] == f and data[pos+LINE_LEN+1] != f:
            c += 1
    if data[pos-LINE_LEN] == f and data[pos-1] == f and data[pos-LINE_LEN-1] != f:
            c += 1
    if data[pos+LINE_LEN] == f and data[pos-1] == f and data[pos+LINE_LEN-1] != f:
            c += 1
    if data[pos-LINE_LEN] == f and data[pos+1] == f and data[pos-LINE_LEN+1] != f:
            c += 1
    return c


def walk_field(data, pos, field=""):
    if field == "":
        field = data[pos]
    if data[pos] != field:
        return 0, 0
    global SEEN
    if pos in SEEN:
        return 0, 0
    SEEN.append(pos)
    res = 1, count_corners(data, pos)
    for orient in ORIENTATION:
        r = walk_field(data, pos+orient, field)
        res = res[0] + r[0], res[1] + r[1]
    return res


def solution2(data):
    price = 0
    for pos in range(LINE_LEN, len(data)-LINE_LEN):
        if data[pos] == "\n":
            continue
        size, corners = walk_field(data, pos)
        if size == 0:
            continue
        price += size * corners
        print(f"{data[pos]:s} {size:d} {corners:d}")
    return price


if __name__ == "__main__":
    print("Solution 2: {:d}".format(solution2(raw_data)))

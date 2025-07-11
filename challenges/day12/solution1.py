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

with open("../../inputs/day12/input", "r") as fid:
    raw_data = fid.read()

raw_data = TEST_DATA


LINEWIDTH = raw_data.index("\n")  + 1
data = LINEWIDTH * "\n" + raw_data + LINEWIDTH * "\n"
SEEN = len(data) * [False]
SEEN_SIDE = len(data) * [False]

OTHER_SIDE = [-LINEWIDTH, 1, LINEWIDTH, -1]
NEXT_POS = [1, LINEWIDTH, -1, -LINEWIDTH]


def handle_pos(pos):
    if SEEN[pos]:
        return 0, 0
    else:
        SEEN[pos] = True
    pU = pos - LINEWIDTH
    pB = pos + LINEWIDTH
    pL = pos - 1
    pR = pos + 1
    perimeter = 0
    area = 1
    garden = data[pos]
    for p in [pU, pB, pL, pR]:
        if data[p] != garden:
            perimeter += 1
    for p in [pU, pB, pL, pR]:
        if data[p] == garden:
            np, na = handle_pos(p)
            perimeter += np
            area += na
    return perimeter, area


def isedge(pos, garden, dir):
    return data[pos] == garden and data[pos+OTHER_SIDE[dir]] != garden


def count_sides(pos):
    if SEEN_SIDE[pos]:
        return 0
    else:
        SEEN_SIDE[pos] = True
    if not isedge(pos, data[pos], 0):
        return 0
    startpos = pos
    dir = 0
    garden = data[pos]
    side = 0
    while True:
        SEEN_SIDE[pos] = True
        if not isedge(pos + NEXT_POS[dir], garden, dir):
            side += 1
        while not isedge(pos + NEXT_POS[dir], garden, dir):
            print(data[pos] + str(startpos) + " " + str(pos) + " " + str(dir))
            dir = (dir + 1) % 4
        pos += NEXT_POS[dir]
        if pos == startpos and dir == 0:
            return side

res1 = 0
res2 = 0
for pos in range(len(data)):
    if data[pos] == "\n":
        continue
    p, a = handle_pos(pos)
    s = count_sides(pos)
    if p != 0:
        print(f"{data[pos]:s}\t{a:d}\t{s:d}")
    res1 += p * a
    res2 += s * a
print(res1)
print(res2)

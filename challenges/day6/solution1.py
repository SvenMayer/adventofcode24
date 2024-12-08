#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:32:25 2024

@author: sven
"""
TEST_DATA = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

with open("../../inputs/day6/input", "r") as fid:
    data = fid.read()

# data = TEST_DATA

LINE_LEN = data.index("\n") + 1
data = (LINE_LEN + 1) * "\n" + data + (LINE_LEN + 1) * "\n"

visited = set()
steps = 0
path = []
pos = data.index("^")

MOVEMENT = -LINE_LEN, 1, LINE_LEN, -1
direction = 0


while data[pos] != "\n":
    if data[pos] != "#":
        visited.add(pos)
    else:
        pos -= MOVEMENT[direction]
        direction = (direction + 1) % 4
        steps -= 1
    pos += MOVEMENT[direction]
    steps += 1

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
path = []
startpos = pos = data.index("^")

MOVEMENT = -LINE_LEN, 1, LINE_LEN, -1
direction = 0
loop = 0
looppos = []
path = []


def check_loop(pos, direction):
    newO = pos + MOVEMENT[direction]
    posseen = []
    while data[pos] != "\n":
        if data[pos] == "#" or pos == newO:
            pos -= MOVEMENT[direction]
            if (pos, direction) in posseen:
                return True
            posseen.append((pos, direction))
            direction = (direction + 1) % 4
        pos += MOVEMENT[direction]
    return False



while data[pos] != "\n":
    if data[pos] != "#":
        visited.add(pos)
        nextpos = pos + MOVEMENT[direction]
        path.append((pos, direction))
        if data[nextpos] != "#" and nextpos not in visited and check_loop(pos, direction):
            loop += 1
            looppos.append(pos + MOVEMENT[direction])
    else:
        pos -= MOVEMENT[direction]
        direction = (direction + 1) % 4
    pos += MOVEMENT[direction]


def move_loop(startpos, startdir, data, obstacle):
    path = []
    corners = set()
    pos = startpos
    direction = startdir
    while data[pos] != "\n":
        if data[pos] != "#" and pos != obstacle:
            path.append((pos, direction))
        else:
            pos -= MOVEMENT[direction]
            if (pos, direction) in corners:
                return []
            corners.add((pos, direction))
            direction = (direction + 1) % 4
        pos += MOVEMENT[direction]
    return path


startpos = data.index("^")
path = move_loop(startpos, 0, data, None)
obstacles = set([itm[0] for itm in path])
obstacles.remove(startpos)
loops = 0
for ob in obstacles:
    if len(move_loop(startpos, 0, data, ob)) == 0:
        loops += 1

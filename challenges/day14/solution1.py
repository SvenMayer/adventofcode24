#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 11:58:49 2025

@author: sven
"""
import os
from PIL import Image


WIDTH = 101
HEIGHT = 103

# WIDTH = 11
# HEIGHT = 7

CENTER_X = (WIDTH - 1) // 2
CENTER_Y = (HEIGHT - 1) // 2


TEST_DATA = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


with open("../../inputs/day14/input", "r") as fid:
    raw_data = fid.read()


# raw_data = TEST_DATA


def parse_robot(ln):
    def parse_xy(chunk):
        xy = chunk.split("=")[1].split(",")
        return int(xy[0].strip()), int(xy[1].strip())
    posstr, velostr = ln.split(" ")
    return parse_xy(posstr), parse_xy(velostr)


def move_robot(r, n):
    pos, velo = r
    newpos = (pos[0] + velo[0] * n) % WIDTH, (pos[1] + velo[1] * n) % HEIGHT
    return newpos, velo


def in_quarter(r):
    pos, velo = r
    x, y = pos
    if y < CENTER_Y:
        if x > CENTER_X:
            return 0
        elif x < CENTER_X:
            return 1
    elif y > CENTER_Y:
        if x > CENTER_X:
            return 3
        elif x < CENTER_X:
            return 2
    return 4


def solution1(data):
    quarters = [[] for i in range(5)]
    for ln in data.split("\n"):
        if len(ln) == 0:
            continue
        r = parse_robot(ln)
        new_r = move_robot(r, 100)
        quarters[in_quarter(new_r)].append(new_r)
    res = 1
    for q in quarters[:4]:
        res *= len(q)
    return res


def print_output(prefix, robots):
    img = Image.new('RGB', (WIDTH,HEIGHT), "white")
    pixels = img.load()
    for r in robots:    # For every pixel:
        pos, velo = r
        pixels[pos[0], pos[1]] = (1, 1, 1)
    img.save(os.path.dirname(__file__) + f"/img{prefix}.png")


def solution2(data):
    r = [parse_robot(ln) for ln in data.split("\n") if len(ln) > 0]
    t = 33
    r = [move_robot(itm, t) for itm in r]
    for i in range(200):
        print_output(t, r)
        t += 103
        r = [move_robot(itm, 103) for itm in r]
    r = [parse_robot(ln) for ln in data.split("\n") if len(ln) > 0]
    t = 68
    r = [move_robot(itm, t) for itm in r]
    for i in range(200):
        print_output(t, r)
        t += 101
        r = [move_robot(itm, 101) for itm in r]


print(solution1(raw_data))
solution2(raw_data)

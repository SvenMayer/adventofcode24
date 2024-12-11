#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:48:57 2024

@author: sven
"""
TEST_DATA = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

with open("../../inputs/day10/input", "r") as fid:
    raw_data = fid.read()

# raw_data = TEST_DATA


def parse_data(raw_data):
    LL = raw_data.index("\n") + 1
    data = (LL*2 + len(raw_data)) * [-1]
    for i, c in enumerate(raw_data):
        data[i+LL] = int(c) if c != "\n" else -1
    return data, LL


def walk(data, LL, i):
    res = set()
    if data[i] == 9:
        res.add(i)
    if data[i-LL] == data[i] + 1:
        res.update(walk(data, LL, i-LL))
    if data[i-1] == data[i] + 1:
        res.update(walk(data, LL, i-1))
    if data[i+LL] == data[i] + 1:
        res.update(walk(data, LL, i+LL))
    if data[i+1] == data[i] + 1:
        res.update(walk(data, LL, i+1))
    return res


def walk2(data, LL, path):
    res = []
    i = path[-1]
    if data[i] == 9:
        res.append(path)
    if data[i-LL] == data[i] + 1:
        res.extend(walk2(data, LL, path + [i-LL]))
    if data[i-1] == data[i] + 1:
        res.extend(walk2(data, LL, path + [i-1]))
    if data[i+LL] == data[i] + 1:
        res.extend(walk2(data, LL, path + [i+LL]))
    if data[i+1] == data[i] + 1:
        res.extend(walk2(data, LL, path + [i+1]))
    return res


def solution1(raw_data):
    data, LL = parse_data(raw_data)
    res = 0
    idx = 0
    while True:
        try:
            idx = data.index(0, idx)
        except ValueError:
            break
        res += len(walk(data, LL, idx))
        idx += 1
    return res



def solution2(raw_data):
    data, LL = parse_data(raw_data)
    res = 0
    idx = 0
    while True:
        try:
            idx = data.index(0, idx)
        except ValueError:
            break
        res += len(walk2(data, LL, [idx]))
        idx += 1
    return res


res1 = solution1(raw_data)
res2 = solution2(raw_data)

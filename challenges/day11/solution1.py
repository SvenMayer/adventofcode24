#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:25:16 2024

@author: sven
"""
import functools
import numpy as np


TEST_DATA = """125 17
"""

with open("../../inputs/day11/input", "r") as fid:
    raw_data = fid.read()

# raw_data = TEST_DATA

N10 = np.log(10)


@functools.cache
def handle_stone(stone):
    if stone == 0:
        return [1]
    ndigits = int(np.log(stone) / N10) + 1
    if ndigits % 2 == 0:
        cmp = 10 ** (ndigits // 2)
        return [stone // cmp, stone % cmp]
    return [stone * 2024]


def resolve(data, N):
    old_list = data
    new_list = []
    for i in range(N):
        for s in old_list:
            new_list.extend(handle_stone(s))
        old_list = new_list
        new_list = []
    return old_list


def solution1(raw_data):
    return len(resolve(parse_data(raw_data), 25))


def solution2(raw_data):
    One_ten = resolve([1], 10)
    zero_ten = resolve([0], 10)
    data = parse_data(raw_data)
    l = resolve(data, 10)
    l.count(1)




def parse_data(raw_data):
    return [int(itm) for itm in raw_data.strip().split(" ")]


res = solution1(raw_data)




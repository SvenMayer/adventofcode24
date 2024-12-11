#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:17:32 2024

@author: sven
"""
TEST_DATA = """2333133121414131402
"""

with open("../../inputs/day9/input", "r") as fid:
    raw_data = fid.read()

# raw_data = TEST_DATA


def parse_data(raw_data):
    raw_data = raw_data.strip()
    lst = [int(c) for c in raw_data]
    filesize = lst[::2]
    empty = lst[1::2]
    empty.append(0)
    return filesize, empty


def move_files(filesize, empty):
    filelist = [idx for idx in range(len(filesize))]
    for fid in range(len(empty)-1, -1, -1):
        sz = filesize[fid]
        for emptyidx, emptysize in enumerate(empty):
            if emptysize >= sz:
                fileidx = filelist.index(fid)
                if fileidx <= emptyidx:
                    break
                empty[fileidx-1] = empty[fileidx-1] + sz + empty[fileidx]
                empty[emptyidx] = empty[emptyidx] - sz
                filelist.pop(fileidx)
                empty.pop(fileidx)
                empty.insert(emptyidx, 0)
                filelist.insert(emptyidx+1, fid)
    return filelist, filesize, empty


def calc_value(filelist, filesize, empty):
    idx = 0
    res = 0
    for i in range(len(filelist)):
        for j in range(filesize[filelist[i]]):
            res += idx * filelist[i]
            idx += 1
        for j in range(empty[i]):
            idx += 1
    return res


filesize, empty = parse_data(raw_data)
filelist, filesize, empty = move_files(filesize, empty)
res = calc_value(filelist, filesize, empty)

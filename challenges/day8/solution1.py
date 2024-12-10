#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:16:50 2024

@author: sven
"""
TEST_DATA = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


with open("../../inputs/day8/input", "r") as fid:
    raw_data = fid.read()

# raw_data = TEST_DATA

def parse_board(raw_data):
    W = raw_data.index("\n")
    H = raw_data.count("\n")
    linelen = raw_data.index("\n") + 1
    res = {}
    for i, c in enumerate(raw_data):
        if c in ".\n":
            continue
        x =  i % linelen
        y = i // linelen
        if c not in res:
            res[c] = []
        res[c].append((x, y))
    return W, H, res


def get_nodes(p0, p1):
    mx = p1[0] - p0[0]
    my = p1[1] - p0[1]
    n0 = p0[0] - mx, p0[1] - my
    n1 = p1[0] + mx, p1[1] + my
    return n0, n1


def get_line(p0, p1, W, H):
    mx = p1[0] - p0[0]
    my = p1[1] - p0[1]
    gcf = sorted([i for i in range(1, my+1) if my%i==0 and mx%i==0], reverse=True)[0]
    mx = mx // gcf
    my = my // gcf
    n = []
    i = 0
    while True:
        n_ = p0[0] - i * mx, p0[1] - i * my
        if not in_board(n_, W, H):
            break
        n.append(n_)
        i += 1
    i = 0
    while True:
        n_ = p1[0] + i * mx, p1[1] + i * my
        if not in_board(n_, W, H):
            break
        n.append(n_)
        i += 1
    return n


def in_board(n, W, H):
    return n[0] >= 0 and n[0] < W and n[1] >= 0 and n[1] < H

def print_board(W, H, data, nodes):
    ll = W + 1
    for n_ in nodes:
        p = n_[0] + n_[1] * ll
        if data[p] == ".":
            data = data[:p] + "#" + data[p+1:]
    print(data)


def solution1(W, H, res):
    nodes = set()
    for node_pos in res.values():
        for i0 in range(len(node_pos) - 1):
            for i1 in range(i0 + 1, len(node_pos)):
                p0 = node_pos[i0]
                p1 = node_pos[i1]
                n0, n1 = get_nodes(p0, p1)
                if in_board(n0, W, H):
                    nodes.add(n0)
                if in_board(n1, W, H):
                    nodes.add(n1)
    return len(nodes)


def solution2(W, H, data):
    nodes = set()
    for node_pos in data.values():
        for i0 in range(len(node_pos) - 1):
            for i1 in range(i0 + 1, len(node_pos)):
                p0 = node_pos[i0]
                p1 = node_pos[i1]
                n = get_line(p0, p1, W, H)
                for n_ in n:
                    nodes.add(n_)
    return nodes


W, H, data = parse_board(raw_data)
res = solution1(W, H, data)
print(res)

res = solution2(W, H, data)
print(len(res))

# print_board(W, H, raw_data, res)
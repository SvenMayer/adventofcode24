#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open("../../inputs/day18/input", "r") as fid:
    data = fid.read()


WIDTH = 71
HEIGHT = 71


def get_adjacent_pos(pos):
    res = []
    for d_ in [1, -1]:
        p_ = pos + d_
        if p_ // WIDTH == pos // WIDTH:
            res.append(p_)
    for d_ in [-WIDTH, WIDTH]:
        p_ = pos + d_
        if p_ > 0 and p_ < WIDTH * HEIGHT:
            res.append(p_)
    return res


def no_laps(data, ct):
    board = WIDTH*HEIGHT*[False]

    for ln in data.split("\n")[:ct]:
        if len(ln) == 0:
            continue
        x_, y_ = ln.split(",")
        x = int(x_)
        y = int(y_)
        board[x+y*WIDTH] = True


    POS = set([0])
    SEEN = set()
    lap = 0
    no_laps = None

    while len(POS):
        new_pos = set()
        for p_ in POS:
            if p_ == WIDTH*HEIGHT-1:
                no_laps = lap
                break
            for neighbor in get_adjacent_pos(p_):
                if board[neighbor] or neighbor in SEEN:
                    continue
                SEEN.add(neighbor)
                new_pos.add(neighbor)
        lap += 1
        POS = new_pos
    return no_laps


print("solution1")
print(no_laps(data, 1024))

print("solution2")
last_bad = data.count("\n")
last_good = 0
res = None
while True:
    if last_good +1 == last_bad:
        res = last_bad - 1
        break
    test = (last_bad + last_good + 1) // 2
    if no_laps(data, test) is None:
        last_bad = test
    else:
        last_good = test
print(data.split("\n")[res])


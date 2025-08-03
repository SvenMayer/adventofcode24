#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 08:50:14 2025

@author: sven
"""
with open("../../inputs/day22/input", "r") as fid:
    secrets = [int(ln) for ln in fid.read().split("\n") if len(ln)]

# secrets = [1, 10, 100, 2024]
# secrets = [1, 2, 3, 2024]


_19POW0 = 19**0
_19POW1 = 19**1
_19POW2 = 19**2
_19POW3 = 19**3



def next_secret(secret):
    s_ = ((secret * 64) ^ secret) % 16777216
    s_ = ((s_ // 32) ^ s_) % 16777216
    s_ = ((s_ * 2048) ^ s_) % 16777216
    return s_


def get_price(secret):
    return secret % 10


def instructions_to_id(diff):
    return ((diff[-4] + 9) * _19POW0) + ((diff[-3] + 9) * _19POW1) + ((diff[-2] + 9) * _19POW2) + ((diff[-1] + 9) * _19POW3)


def monkey_instructions(secret, no_steps=2000):
    inst = 19**4*[None]
    diff = []
    p0 = get_price(secret)
    s_ = secret
    for i in range(no_steps):
        s_ = next_secret(s_)
        p1 = get_price(s_)
        diff.append(p1 - p0)
        diff = diff[-4:]
        if len(diff) == 4:
            id_ = instructions_to_id(diff)
            if inst[id_] is None:
                inst[id_] = p1
        p0 = p1
    return inst


def solution1(no_steps=2000):
    res = dict()
    solution1 = 0
    for s_ in secrets:
        k = s_
        for i in range(no_steps):
            s_ = next_secret(s_)
        res[k] = s_
        solution1 += s_
    return solution1


def solution2():
    inst = 19**4 * [0]
    for s_ in secrets:
        inst_monkey = monkey_instructions(s_)
        for i in range(len(inst)):
            if inst_monkey[i] is not None:
                inst[i] += inst_monkey[i]
    return max(inst)


print("Solution1")
print(solution1())

print("Solution2")
print(solution2())

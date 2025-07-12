#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 11:18:07 2025

@author: sven
"""
PART2 = True

PRICE_A = 3
PRICE_B = 1


TEST_DATA = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


with open("../../inputs/day13/input", "r") as fid:
    raw_data = fid.read()


def parse_machine(m):
    lines = m.split("\n")
    AB = []
    for ln in lines[:2]:
        xy = ln.split(":")[1].split(",")
        x = int(xy[0].strip()[1:])
        y = int(xy[1].strip()[1:])
        AB.append((x, y))
    xy = lines[2].split(":")[1].split(",")
    PRIZE = int(xy[0].strip()[2:]), int(xy[1].strip()[2:])
    if PART2:
        PRIZE = PRIZE[0] + 10000000000000, PRIZE[1] + 10000000000000
    return AB[0], AB[1], PRIZE


def solve_machine(A, B, P):
    xa, ya = A
    xb, yb = B
    xp, yp = P
    numb = xp*ya - yp*xa
    denb = xb*ya - yb*xa
    numa = xp*yb - yp*xb
    dena = xa*yb - ya*xb
    if numb % denb == 0 and numa % dena == 0:
        solvable = True
    else:
        solvable = False
    if solvable:
        b = numb // denb
        a = numa // dena
        p = a * PRICE_A + b * PRICE_B
    else:
        p = 0
    return solvable, p


def solution1(data):
    cumcost = 0
    for m in data.split("\n\n"):
        a, b, p = parse_machine(m)
        solvable, cost = solve_machine(a, b, p)
        cumcost += cost
    return cumcost


print(solution1(raw_data))



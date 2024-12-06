#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:49:26 2024

@author: sven
"""
TEST_DATA = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

with open("../../inputs/day5/input", "r") as fid:
    data = fid.read()

# data = TEST_DATA


def parse_rules(rules):
    page_rules = [[] for i in range(100)]
    for ln in rules.split("\n"):
        p1 = int(ln[:2])
        p2 = int(ln[3:])
        page_rules[p2].append(p1)
    return page_rules


def parse_plan(plan):
    res = []
    for ln in plan.split("\n"):
        if len(ln) == 0:
            continue
        res.append([int(no) for no in ln.split(",")])
    return res


def parse_board(data):
    rules, plan = data.split("\n\n")
    return parse_rules(rules), parse_plan(plan)



def isvalid(rules, inst):
    for i in range(len(inst)):
        remainder = inst[i:]
        for v in rules[inst[i]]:
            if v in remainder:
                return False
    return True


def order_inst(rules, inst):
    for i in range(len(inst)):
        remainder = inst[i:]
        for v in rules[inst[i]]:
            if v in remainder:
                j = inst.index(v)
                new_inst = [x for x in inst]
                new_inst[i] = inst[j]
                new_inst[j] = inst[i]
                return order_inst(rules, new_inst)
    return inst


def get_center(inst):
    return inst[len(inst)//2]


rules, plan = parse_board(data)
ct = 0
res = 0
res2 = 0
for inst in plan:
    if isvalid(rules, inst):
        ct += 1
        res += get_center(inst)
    else:
        new_inst = order_inst(rules, inst)
        res2 += get_center(new_inst)

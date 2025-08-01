#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 17:11:49 2025

@author: sven
"""
with open("../../inputs/day15/input", "r") as fid:
    raw_data = fid.read()


def get_boxes_array(field):
    boxes = []
    for itm in field:
        if itm == "O":
            boxes.append(True)
        else:
            boxes.append(False)
    return boxes


def parse_instructions(instructions, WIDTH, HEIGHT):
    res = []
    for itm in instructions:
        if itm == "^":
            res.append(-WIDTH)
        elif itm == ">":
            res.append(1)
        elif itm == "v":
            res.append(WIDTH)
        elif itm == "<":
            res.append(-1)
        elif itm == "\n":
            pass
        else:
            raise TypeError(f"unknown insturction '{itm:s}'")
    return res


def move_impossible(field, boxes, pos, direction):
    return field[pos] == "#" or (boxes[pos] is True and move_box(field, boxes, pos, direction) is False)


def move_box(field, boxes, pos, direction):
    newpos = pos + direction
    if move_impossible(field, boxes, newpos, direction):
        return False
    boxes[pos] = False
    boxes[pos+direction] = True
    return True


def solution1(data):
    field, instructions = data.split("\n\n")
    WIDTH = field.index("\n") + 1
    HEIGHT = field.count("\n") + 1
    boxes = get_boxes_array(field)
    directions = parse_instructions(instructions, WIDTH, HEIGHT)
    pos_robot = field.index("@")
    for dir_ in directions:
        newpos = pos_robot + dir_
        if not move_impossible(field, boxes, newpos, dir_):
            pos_robot = newpos
    res = 0
    for i, itm in enumerate(boxes):
        if itm:
            res += i % WIDTH + 100 * (i // WIDTH)
    return res


if __name__ == "__main__":
    print(solution1(raw_data))

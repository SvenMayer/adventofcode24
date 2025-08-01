#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 17:11:49 2025

@author: sven
"""
TEST_DATA = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


TEST_DATA2 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

with open("../../inputs/day15/input", "r") as fid:
    raw_data = fid.read()
# raw_data = TEST_DATA


def get_boxes_array(field):
    boxes = []
    i = 1
    for itm in field:
        if itm == "O":
            boxes.extend([i,i])
            i += 1
        else:
            boxes.extend([0,0])
    return boxes


def parse_instructions(instructions, WIDTH, HEIGHT):
    res = []
    for itm in instructions:
        if itm == "^":
            res.append((vertical_move_impossible, -WIDTH))
        elif itm == ">":
            res.append((horizontal_move_impossible, 1))
        elif itm == "v":
            res.append((vertical_move_impossible, WIDTH))
        elif itm == "<":
            res.append((horizontal_move_impossible, -1))
        elif itm == "\n":
            pass
        else:
            raise TypeError(f"unknown insturction '{itm:s}'")
    return res


def get_box_extend(boxes, pos):
    if boxes[pos+1] == boxes[pos]:
        return pos, pos+1
    return pos-1, pos


def vertical_move_box_impossible(field, boxes, pos, direction):
    pos1, pos2 = get_box_extend(boxes, pos)
    newpos1 = pos1 + direction
    newpos2 = pos2 + direction
    if field[newpos1//2] == "#" or field[newpos2//2] == "#":
        return True
    box1 = boxes[newpos1]
    box2 = boxes[newpos2]
    if box1 == 0 and box2 == 0:
        return False
    res = False
    if box1 != 0:
        res |= vertical_move_box_impossible(field, boxes, newpos1, direction)
    if box2 != 0 and box2 != box1:
        res |= vertical_move_box_impossible(field, boxes, newpos2, direction)
    return res


def vertical_move_box(field, boxes, pos, direction):
    pos1, pos2 = get_box_extend(boxes, pos)
    newpos1 = pos1 + direction
    newpos2 = pos2 + direction
    box1 = boxes[newpos1]
    box2 = boxes[newpos2]
    if box1 != 0:
        vertical_move_box(field, boxes, newpos1, direction)
    if box2 != 0 and box2 != box1:
        vertical_move_box(field, boxes, newpos2, direction)
    if boxes[newpos1] == 0 and boxes[newpos2] == 0:
        boxes[newpos1] = boxes[pos1]
        boxes[newpos2] = boxes[pos2]
        boxes[pos1] = 0
        boxes[pos2] = 0
        return


def vertical_move_impossible(field, boxes, pos, direction):
    if field[pos//2] == "#" or (boxes[pos] != 0 and vertical_move_box_impossible(field, boxes, pos, direction)):
        return True
    if boxes[pos] == 0:
        return False
    vertical_move_box(field, boxes, pos, direction)
    return False


def horizontal_move_impossible(field, boxes, pos, direction):
    return field[pos//2] == "#" or (boxes[pos] != 0 and horizontal_move_box(field, boxes, pos, direction) is False)


def horizontal_move_box(field, boxes, pos, direction):
    newpos = pos + direction
    if horizontal_move_impossible(field, boxes, newpos, direction):
        return False
    boxes[pos+direction] = boxes[pos]
    boxes[pos] = 0
    return True


def show_field(field, boxes, robot):
    res = ""
    i = 0
    while i < len(field)*2:
    # for i in range(len(field)*2):
        if field[i//2] == "#":
            res += "#"
        elif field[i//2] == "\n":
            res += "\n"
        elif boxes[i] != 0:
            res += "[]"
            i += 1
        else:
            res += "."
        i += 1
    res = res[:robot] + "@" + res[robot+1:]
    res = res.replace("\n\n", "\n")
    print(res)


if __name__ == "__main__":
    data = raw_data
    field, instructions = data.split("\n\n")
    instructions = instructions.replace("\n", "")
    WIDTH = (field.index("\n") + 1)*2
    HEIGHT = (field.count("\n") + 1)*2
    boxes = get_boxes_array(field)
    directions = parse_instructions(instructions, WIDTH, HEIGHT)
    pos_robot = field.index("@") * 2
    # show_field(field, boxes, pos_robot)
    for i, ((foo, dir_), inst) in enumerate(zip(directions, instructions)):
        newpos = pos_robot + dir_
        # if i == 6:
        #     import pdb;pdb.set_trace()
        if not foo(field, boxes, newpos, dir_):
            pos_robot = newpos
            # print(str(i) + " " + inst + " True")
        # else:
        #     print(str(i) + " " + inst + " False")
        # show_field(field, boxes, pos_robot)
    res = 0
    i = 0
    while i < len(boxes):
        itm = boxes[i]
        if itm != 0:
            res += i % WIDTH + 100 * (i // WIDTH)
            i += 1
        i += 1
    # return res


# if __name__ == "__main__":
    # print(solution2(raw_data))

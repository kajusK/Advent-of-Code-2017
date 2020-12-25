#!/usr/bin/python3

import fileinput
import re

for line in fileinput.input():
    line = re.sub(r'\s*$', '', line)
    directions = line.split(',')

    pos_x = 0
    pos_y = 0

    maxd = 0
    for dir in directions:
        if dir == 'n':
            pos_y += 1
        elif dir == 's':
            pos_y -= 1
        elif dir == 'e':
            pos_x += 1
        elif dir == 'w':
            pos_x -= 1
        elif dir == 'ne':
            pos_y += 1
            pos_x += 1
        elif dir == 'se':
            pos_y -= 1
            pos_x += 1
        elif dir == 'sw':
            pos_y -= 1
            pos_x -= 1
        elif dir == 'nw':
            pos_y += 1
            pos_x -= 1
        if abs(pos_y) > maxd:
            maxd = abs(pos_y)
        if abs(pos_x) > maxd:
            maxd = abs(pos_x)

    print(pos_x,pos_y)
    print(maxd)
    print(max(abs(pos_x),abs(pos_y)))

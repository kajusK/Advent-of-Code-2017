#!/usr/bin/python3

import fileinput
import re
from hashlib import getHash

string = ""
for line in fileinput.input():
    string = re.sub(r'\s*$', '', line)

map = []

for i in range(128):
    hash = getHash(string+"-"+str(i))
    line = []
    for c in hash:
        binary = bin(int(c, 16))[2:].zfill(4)
        line += binary
    map.append(line)

expand = [[0,1],[0,-1],[1,0],[-1,0]]

segments = 0
stack = []

print(len(map), len(map[0]))
for x in range(128):
    for y in range(128):
        if map[x][y] != '1':
            continue

        segments -= 1
        stack.append([x,y])

        while len(stack):
            position = stack.pop()
            map[position[0]][position[1]] = segments

            for dir in expand:
                new_x = dir[0] + position[0]
                new_y = dir[1] + position[1]
                if new_x < 0 or new_y < 0 or new_x > 127 or new_y > 127:
                    continue

                if map[new_x][new_y] == '1':
                    stack.append([new_x, new_y])

print(segments)

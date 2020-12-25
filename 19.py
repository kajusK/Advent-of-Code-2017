#!/usr/bin/python3

import fileinput
import string

map = []

for line in fileinput.input():
    map.append(list(line))

print(map)

pos = [0,0]
direction = [1, 0]

for i in range(len(map[0])):
    if map[0][i] == "|":
        pos = [0, i]

retezec = ""
steps = 0

while 1:
    steps += 1
    new_pos = [pos[0] + direction[0], pos[1] + direction[1]]

    if map[pos[0]][pos[1]] in string.ascii_lowercase+string.ascii_uppercase:
        retezec += map[pos[0]][pos[1]]
        pos = new_pos
        continue

    if map[pos[0]][pos[1]] == "|" or map[pos[0]][pos[1]] == "-":
        pos = new_pos
        continue

    paths = [[0,-1], [0,1], [-1,0], [1,0]]
    if map[pos[0]][pos[1]] == "+":
        for p in paths:
            if p[0] == -direction[0] and p[1] == -direction[1]:
                continue
            if map[pos[0]+p[0]][pos[1]+p[1]] != " ":
                direction = p[:]
                pos = [pos[0] + p[0], pos[1] + p[1]]
                break
    else:
        break

print(retezec, steps-1)

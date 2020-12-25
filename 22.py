#!/usr/bin/python3

import fileinput
import re

def count_infected(map):
    infected = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '#':
                infected += 1
    return infected

directions = [[-1, 0],[0,1],[1, 0],[0,-1]]
dir = 0

map = []

for line in fileinput.input():
    line = re.sub(r'\s*', '', line)
    map.append(list(line))

line = ["." for i in range(1000)]
for i in range(len(map)):
    map[i] = line + map[i]+line

line = [['.' for i in range(len(map[0]))] for i in range(1000)]
map = line+map+line

infected = 0
pos = [int(len(map)/2), int(len(map[0])/2)]

for i in range(10000000):
    if map[pos[0]][pos[1]] == '.':
        dir = (dir - 1) if dir >= 1 else 3
        map[pos[0]][pos[1]] = 'w'
    elif map[pos[0]][pos[1]] == 'w':
        map[pos[0]][pos[1]] = '#'
        infected += 1
    elif map[pos[0]][pos[1]] == '#':
        map[pos[0]][pos[1]] = 'f'
        dir = (dir+1)%4
    else:
        map[pos[0]][pos[1]] = '.'
        dir = (dir+2)%4


    pos[0] += directions[dir][0]
    pos[1] += directions[dir][1]

for i in range(len(map)):
    print("".join(map[i]))
print(infected)

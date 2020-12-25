#!/usr/bin/python3

import sys
from math import sqrt

num = int(sys.argv[1])**2
final = int(sys.argv[2])

if num == 1:
    print(2)
    exit()

edge = sqrt(num)

#corner cases
if edge != int(edge):
    edge = int(edge)+1
if (edge%2 == 0):
    edge += 1

edge = int(edge)

map = [[0 for x in range(edge+2)] for y in range(edge+2)]

pos = [int(edge/2)+1, int(edge/2)+1]
map[pos[0]][pos[1]] = 1
pos[1] = pos[1]+1
dirs = [[1,0],[1,1],[0,1],[-1,0],[-1,-1],[0,-1],[1,-1],[-1,1]]

x = 1
square = 3

while x < num:
    count = 0
    x += 1

    for i in range(len(dirs)):
        count += map[pos[0]+dirs[i][0]][pos[1]+dirs[i][1]]
    map[pos[0]][pos[1]] = count

    if count > final:
        print(count)
        break

    corners = []
    #first edge is shorter
    corners.append((square-2)**2+1 + square-2)
    corners.append(corners[0] + square-1)
    corners.append(corners[1] + square-1)
    corners.append(corners[2] + square-1)

    if x < corners[0]:
        pos[0] += 1
    elif x < corners[1]:
        pos[1] -= 1
    elif x < corners[2]:
        pos[0] -= 1
    elif x < corners[3]:
        pos[1] += 1
    elif x == corners[3]:
        square += 2
        pos[1] += 1


for line in map:
    print(line)


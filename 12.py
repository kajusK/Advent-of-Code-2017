#!/usr/bin/python3

import fileinput
import re

def group_parts(pipes, id):
    can_see = [id]
    i = 0

    while 1:
        id = can_see[i]
        for p in pipes[id]:
            if p not in can_see:
                can_see.append(p)

        i += 1
        if i >= len(can_see):
            return can_see

pipes = {}

for line in fileinput.input():
    parts = line.split("<->")
    left = int(parts[0])

    parts = parts[1].split(',')
    right = []
    for p in parts:
        right.append(int(p))

    pipes[left] = right

can_see0 = group_parts(pipes, 0)
print(len(can_see0))

seen = can_see0[0:]
groups = 1

for id, p in pipes.items():
    if id in seen:
        continue

    seen += group_parts(pipes, id)
    groups += 1

print(groups)


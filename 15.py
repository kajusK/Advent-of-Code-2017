#!/usr/bin/python3

import fileinput
import collections

factorx = 16807
factory = 48271
divisor = 2147483647

genx = 0
geny = 0

iterations = 5000000

for line in fileinput.input():
    start = line.split()
    genx = int(start[0])
    geny = int(start[1])

match = 0
lastx = collections.deque()
lasty = collections.deque()
cnt = 0

while iterations != 0:
    genx = genx*factorx
    if genx >= divisor:
        genx = genx % divisor

    geny = geny*factory
    if geny >= divisor:
        geny = geny % divisor

    if genx % 4 == 0:
        lastx.append(genx)
    if geny % 8 == 0:
        lasty.append(geny)

    if len(lastx) != 0 and len(lasty) != 0:
        x = lastx.popleft()
        y = lasty.popleft()
        iterations -= 1
        if bin(x)[2:].zfill(32)[16:] == bin(y)[2:].zfill(32)[16:]:
            match += 1

print(match)


#!/usr/bin/python3

import fileinput

for line in fileinput.input():
    step = int(line)

map = [0]
insert = 0
position = 0

#while insert != 2017:
#    insert += 1
#    position = (position + step)%len(map) + 1
#
#    if position == len(map):
#        map.append(insert)
#    else:
#        map.insert(position, insert)
#
#position = map.index(0)
#position = (position + 1) % len(map)
#print(map[position])

at_1 = 0

while insert != 50000000:
    insert += 1
    position = (position + step)%insert + 1

    if position == 1:
        at_1 = insert

print(at_1)

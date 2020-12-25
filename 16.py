#!/usr/bin/python3

import fileinput
import string

commands = []
map_len = 16
loops = 1000000000
map = list(string.ascii_lowercase)[:map_len]

for line in fileinput.input():
    commands = line.split(",")

#TODO detekovat kdy se opakuji a pak preskocit az ke konci
#abcd nastane po 47 opakovanich, kazde dalsi je 47*x + x-1

history = []
history.append(map)

adder = 0

while 1:
    count = 47*adder + adder-1
    if count > 1000000000:
        break
    adder += 1

adder -= 1

for i in range(47*adder+adder, loops):
    for seq in commands:
        cmd = seq[0]
        param = seq[1:]

        if cmd == "s":
            shift = int(param)
            map = map[-shift:] + map[:-shift]
        elif cmd == "x":
            param = param.split('/')
            a = int(param[0])
            b = int(param[1])
            tmp = map[a]
            map[a] = map[b]
            map[b] = tmp
        elif cmd == "p":
            a = map.index(param[0])
            b = map.index(param[2])
            tmp = map[a]
            map[a] = map[b]
            map[b] = tmp
        else:
            print("bullshit")
            exit()


print("".join(map))

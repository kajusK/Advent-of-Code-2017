#!/usr/bin/python3

import fileinput

def get_score(layers, delay):
    score = 0

    time = delay
    for i in range(max(layers)+1):
        if i not in layers.keys():
            time += 1
            continue

        position = time % (layers[i]*2 - 2)
        if position == 0:
            score += i * layers[i]

        time += 1

    return score

def is_clean(layers, delay):
    time = delay
    for i in range(max(layers)+1):
        if i not in layers.keys():
            time += 1
            continue

        position = time % (layers[i]*2 - 2)
        if position == 0:
            return False

        time += 1
    return True


layers = {}

for line in fileinput.input():
    parts = line.split(":")
    layers[int(parts[0])] = int(parts[1])

delay = 0
while not is_clean(layers, delay):
    delay += 1

print(delay)

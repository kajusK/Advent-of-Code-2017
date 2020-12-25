#!/usr/bin/python3

import fileinput
import operator


def spreadBlocks(blocks, index_max):
    count = blocks[index_max]
    blocks[index_max] = 0
    index = index_max

    while count > 0:
        index = index + 1 if index + 1 < len(blocks) else 0
        blocks[index] += 1
        count -= 1

    return blocks

def inHistory(history, blocks):
    for i in range(len(history)):
        if history[i] == blocks:
            print(len(history)-i)
            return True
    return False


for line in fileinput.input():
    blocks = list(map(int, line.split()))

    history = []
    count = 0

    while True:
        history.append(blocks[:])

        index_max, max_value = max(enumerate(blocks), key=operator.itemgetter(1))
        blocks = spreadBlocks(blocks, index_max)

        count += 1

        if inHistory(history, blocks):
            break
    print(count)


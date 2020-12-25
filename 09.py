#!/usr/bin/python3

import fileinput
import re

for line in fileinput.input():
    in_garbage = False
    remove_next = False
    cleaned = ""

    garbage_count = 0
    #clean garbage
    for c in line:
        if remove_next:
            remove_next = False
            continue
        if c == "<" and not in_garbage:
            in_garbage = True
            continue
        if c == ">" and in_garbage:
            in_garbage = False
            continue
        if c == "!" and in_garbage:
            remove_next = True
            continue
        if in_garbage:
            garbage_count += 1
            continue

        cleaned += c

    print(garbage_count)

    counter = 1
    score = 0

    #get the groups
    for c in cleaned:
        if c == '{':
            score += counter
            counter += 1
            continue
        if c == '}':
            counter -= 1
            continue

    print(score)

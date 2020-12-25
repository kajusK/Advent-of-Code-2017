#!/usr/bin/python3

import fileinput
import re

for line in fileinput.input():
    sum = 0
    line = re.sub(r'\s', '', line)

    for i  in range(0, len(line)-1):
        if (line[i] == line[i+1]):
            sum += int(line[i])
    if line[0] == line[len(line)-1]:
        sum += int(line[0])
    print(sum)


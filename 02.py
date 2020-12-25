#!/usr/bin/python3

import fileinput
import re

sum = 0
for line in fileinput.input():
    numbers = list(map(int, line.split()))
    sum += max(numbers) - min(numbers)
print(sum)


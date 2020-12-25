#!/usr/bin/python3

import fileinput

steps = []

for line in fileinput.input():
    steps.append(int(line))

cur = 0
count = 0

while True:
    next_step = steps[cur]
    next = cur + next_step
    if steps[cur] >= 3:
        steps[cur] -= 1
    else:
        steps[cur] += 1

    cur = next
    count += 1

    if next > len(steps)-1 or next < 0:
        break

print(count)

#!/usr/bin/python3

import fileinput
import re

def get_nums(part):
    return list(map(int, part[3:-1].split(",")))

def add_vect(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] + b[i])
    return res

particles = []

for line in fileinput.input():
    line = re.sub(r'\s*$', '', line)
    parts = line.split(", ")
    data = {}
    data['p'] = get_nums(parts[0])
    data['v'] = get_nums(parts[1])
    data['a'] = get_nums(parts[2])

    particles.append(data)

for i in range(1000):
    for i, p in enumerate(particles):
        remove = False
        if p['p'] == False:
            continue
        for j in range(i+1, len(particles)):
            q = particles[j]
            if q['p'] != False and p['p'] == q['p']:
                particles[j]['p'] = False
                remove = True
        if remove:
            particles[i]['p'] = False

    for p in particles:
        if p['p'] == False:
            continue
        p['v'] = add_vect(p['a'], p['v'])
        p['p'] = add_vect(p['v'], p['p'])

#min = 1000000000
#min_i = -1
#
#for i in range(len(particles)):
#    p = particles[i]
#    dist = abs(p['p'][0]) + abs(p['p'][1]) + abs(p['p'][2])
#    if dist < min:
#        min = dist
#        min_i = i
#    print(i, dist, p['v'], p['a'])
#
#print(min_i, min)

print(particles)

count = 0
for p in particles:
    if p['p'] != False:
        count += 1
print(count)


#!/usr/bin/python3

import sys
from math import sqrt

num = int(sys.argv[1])

if num == 1:
    print(0)
    exit()

closest = sqrt(num)

#corner cases
if closest != int(closest):
    closest = int(closest)+1
if (closest%2 == 0):
    closest += 1

#closest contain witdh/height of the map
dist_x = int(closest/2)

centers = []
centers.append((closest-2)**2+1 + dist_x-1)
#first edge is shorter
centers.append(centers[0] + closest-1)
centers.append(centers[1] + closest-1)
centers.append(centers[2] + closest-1)

dist_y = 0
for i in range(0,2):
    if (num > centers[i] and num < centers[i+1]):
        dist_y = min(num-centers[i], centers[i+1]-num)
        break

if num > centers[3]:
    dist_y = num - centers[3]
if num < centers[0]:
    dist_y = centers[0] - num

print(dist_x+ dist_y)


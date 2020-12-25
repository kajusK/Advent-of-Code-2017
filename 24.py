#!/usr/bin/python3

import fileinput

def find_matching(adapters, used, nums):
    num = nums[len(nums)-1]
    for a in adapters:
        if a in used:
            continue
        if a[0] == num:
            used.append(a)
            nums.append(a[1])
            return nums, used
        if a[1] == num:
            used.append(a)
            nums.append(a[0])
            return nums, used
    return nums, used

def weights(used):
    res = 0
    for p in used:
        res += sum(p)
    return res

adapters = []
used = []

for line in fileinput.input():
    ada = line.split("/")
    adapters.append([int(ada[0]), int(ada[1])])

nums = [0]
max = 0
maxlen = 0

def recurse(available, used, nums, max, maxlen):
    while 1:
        length = len(nums)
        nums, used = find_matching(available, used, nums)
        if len(nums) == length:
            weight = weights(used)
            if len(used) >= maxlen and weight > max:
                max = weight
                maxlen = len(used)
            print(weight, used)
            return max, maxlen
        else:
            max, maxlen = recurse(available[:], used[:], nums[:], max, maxlen)
            available.remove(used.pop())
            nums.pop()

max, len = recurse(adapters, used, nums, max, maxlen)
print(max, maxlen)

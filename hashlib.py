#!/usr/bin/python3

import fileinput
import re


def reverse(array, pos, length):
    for i in range(0, int(length/2)):
        first = pos + i
        if first >= len(array):
            first = first - len(array)

        last = pos + length - i - 1
        if last >= len(array):
            last = last - len(array)
        elif last < 0:
            last = len(array) + last

        tmp = array[first]
        array[first] = array[last]
        array[last] = tmp
    return array

def sparsehash(rounds, lengths, size):
    pos = 0
    skip = 0
    array = []

    for i in range(0,size):
        array.append(i)

    for round in range(0, rounds):
        for i in lengths:
           array = reverse(array, pos, i)
           pos += i + skip
           if (pos >= len(array)):
               pos = pos%len(array)
           skip += 1

    return array

def hash(rounds, lengths):
    size = 256
    xor_size = 16
    sparse = sparsehash(rounds, lengths, size)
    res = []

    for i in range(0, size, xor_size):
        sum = sparse[i]
        for j in range(1, xor_size):
            sum ^= sparse[i+j]

        res.append(sum)

    formated = ""
    for i in res:
        num = hex(i)[2:]
        if (len(num) == 1):
            formated += '0'
        formated += num

    return formated

def getHash(string):
    add_lengths = [17, 31, 73, 47, 23]
    line = re.sub(r'\s*$', '', string)
    input = [ord(c) for c in string]
    input += add_lengths
    return hash(64, input)

#!/usr/bin/python3

import fileinput
import re

def isvalid1(line):
    words = line.split()
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j]:
                return False
    return True

def isanagram(word1, word2):
    if ''.join(sorted(word1)) == ''.join(sorted(word2)):
        return True
    return False

def isvalid2(line):
    words = line.split()
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if len(words[i]) == len(words[j]) and isanagram(words[i], words[j]):
                return False
    return True

count = 0
for line in fileinput.input():
    if isvalid1(line) and isvalid2(line):
        count += 1

print(count)

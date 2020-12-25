#!/usr/bin/python3

import fileinput

sum = 0
for line in fileinput.input():
    numbers = list(map(int, line.split()))
    for i in range(0, int(len(numbers)-1)):
        for j in range(i+1, len(numbers)):
            div1 = numbers[i] % numbers[j]
            div2 = numbers[j] % numbers[i]
            print(numbers[i], numbers[j], div1, div2)
            if div1 == 0:
                sum += numbers[i]/numbers[j]
                print(numbers[i], numbers[j])
            if div2==0:
                sum += numbers[j]/numbers[i]
                print(numbers[i], numbers[j])
print(sum)


#!/usr/bin/python2

import fileinput

registers = {}
max = 0

for line in fileinput.input():
    items = line.split()
    reg = items[0]
    op = items[1]
    num = int(items[2])
    q_reg = items[4]
    q_mark = items[5]
    q_val = int(items[6])

    q_reg_val = 0 if q_reg not in registers else registers[q_reg]

    if q_mark == ">" and not q_reg_val > q_val:
        continue
    if q_mark == "<" and not q_reg_val < q_val:
        continue
    if q_mark == ">=" and not q_reg_val >= q_val:
        continue
    if q_mark == "<=" and not q_reg_val <= q_val:
        continue
    if q_mark == "==" and not q_reg_val == q_val:
        continue
    if q_mark == "!=" and not q_reg_val != q_val:
        continue

    if op == "inc":
        registers[reg] = num if reg not in registers else registers[reg] + num
    elif op == "dec":
        registers[reg] = -num if reg not in registers else registers[reg] - num
    else:
        print("incorrect syntax")

    if registers[reg] > max:
        max = registers[reg]

#print(max(registers.values()))
print(max)

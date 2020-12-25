#!/usr/bin/python3

import fileinput

queue = [[], []]
counters = [0, 0]

def get_reg_val(regs, reg):
    if reg.lstrip("-").isdigit():
        return int(reg)
    if reg in regs:
        return regs[reg]
    return 0

def parser(parsed, index, registers, pid):
    print(pid, index, parsed, registers)
    print(queue)
    if parsed[0] == "snd":
        queue[(pid+1)%2].append(get_reg_val(registers,parsed[1]))
        counters[pid] += 1
    elif parsed[0] == "set":
        registers[parsed[1]] = get_reg_val(registers,parsed[2])
    elif parsed[0] == "add":
        if parsed[1] not in registers:
            registers[parsed[1]] = 0
        registers[parsed[1]] += get_reg_val(registers,parsed[2])
    elif parsed[0] == "mul":
        if parsed[1] not in registers:
            registers[parsed[1]] = 0
        registers[parsed[1]] *= get_reg_val(registers,parsed[2])
    elif parsed[0] == "mod":
        if parsed[1] not in registers:
            registers[parsed[1]] = 0
        registers[parsed[1]] %= get_reg_val(registers,parsed[2])
    elif parsed[0] == "rcv":
        if len(queue[pid]) != 0:
            registers[parsed[1]] = queue[pid].pop(0)
        else:
            return index
    elif parsed[0] == "jgz":
        if get_reg_val(registers,parsed[1]) > 0:
            index += get_reg_val(registers, parsed[2])
        else:
            index += 1

    if parsed[0] != "jgz":
        index += 1

    return index


last_played = 0
instructions = []
for line in fileinput.input():
    parsed = line.split()
    instructions.append(parsed)

registers = [{'p': 0},{'p': 1}]
index = [0,0]
prev = [0,0]

while max(index) < len(instructions) and min(index) >= 0:
    index[0] = parser(instructions[index[0]], index[0], registers[0], 0)
    index[1] = parser(instructions[index[1]], index[1], registers[1], 1)

    print()

    if index[0] == prev[0] and index[1] == prev[1]:
        break

    prev = index[:]

print(counters)

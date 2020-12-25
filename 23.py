#!/usr/bin/python3

import fileinput
import string

#def get_reg_val(regs, reg):
#    if reg.lstrip("-").isdigit():
#        return int(reg)
#    if reg in regs:
#        return regs[reg]
#    return 0
#
#def parser(parsed, index, registers, pid):
#    if parsed[0] == "set":
#        registers[parsed[1]] = get_reg_val(registers,parsed[2])
#    elif parsed[0] == "sub":
#        registers[parsed[1]] -= get_reg_val(registers,parsed[2])
#    elif parsed[0] == "mul":
#        registers[parsed[1]] *= get_reg_val(registers,parsed[2])
#    elif parsed[0] == "jnz":
#        if get_reg_val(registers,parsed[1]) != 0:
#            index += get_reg_val(registers, parsed[2])
#        else:
#            index += 1
#        return index
#
#    index += 1
#    return index
#
#instructions = []
#for line in fileinput.input():
#    parsed = line.split()
#    instructions.append(parsed)
#
#registers = {}
#for c in string.ascii_lowercase[:8]:
#    registers[c] = 0
#
#index = 0
#count = 0
#
#
#registers["a"] = 1
#
#while index < len(instructions) and index >= 0:
#    count += 1
#
#    parsed = instructions[index]
#    print(count, index, parsed)
#
#    if parsed[0] == "set":
#        registers[parsed[1]] = get_reg_val(registers,parsed[2])
#    elif parsed[0] == "sub":
#        registers[parsed[1]] -= get_reg_val(registers,parsed[2])
#    elif parsed[0] == "mul":
#        registers[parsed[1]] *= get_reg_val(registers,parsed[2])
#    elif parsed[0] == "jnz":
#        if get_reg_val(registers,parsed[1]) != 0:
#            index += get_reg_val(registers, parsed[2])
#        else:
#            index += 1
#        continue
#
#    index += 1
#
#print(count)

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if not(num & 1):
        return False

    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

b = 99*100+100000
c = b + 17000
h = 0

for i in range(b, c+1, 17):
    print(i)
    if not is_prime(i):
        h += 1
print(h)

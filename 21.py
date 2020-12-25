#!/usr/bin/python3

import fileinput
import re

image = [list(".#."), list("..#"), list("###")]
size = 3

def save_dict(patterns, inputs, outputs):
        if inputs[0] not in patterns:
            patterns[inputs[0]] = {}
        if len(inputs) == 2:
            patterns[inputs[0]][inputs[1]] = outputs
            return patterns

        if not inputs[1] in patterns[inputs[0]]:
            patterns[inputs[0]][inputs[1]] = {}
        patterns[inputs[0]][inputs[1]][inputs[2]] = outputs
        return patterns

def rotate_90(inputs):
    out = [[0 for i in range(len(inputs))] for j in range(len(inputs))]
    for i in range(len(inputs)):
        for j in range(len(inputs)):
            out[i][j] = inputs[len(inputs)-j-1][i]
    return list(map(lambda t: "".join(t), out))

def flip_x(inputs):
    out = []
    for i in range(len(inputs)):
        out.append(inputs[len(inputs)-1-i])
    return out

def add_dict(patterns, inputs, outputs):
    patterns = save_dict(patterns, inputs, outputs)

    rotated = inputs
    for i in range(3):
        rotated = rotate_90(rotated);
        patterns = save_dict(patterns, rotated, outputs)
        patterns = save_dict(patterns, flip_x(rotated), outputs)

    return patterns

def enhance2(patterns, image):
    new_image = [[] for i in range(int(len(image)/2*3))]
    l = 0

    for line in range(0, len(image), 2):
        for row in range(0, len(image), 2):
            pixels = [image[line][row:row+2], image[line+1][row:row+2]]
            pixels = list(map(lambda t: "".join(t), pixels))

            new_image[l] += patterns[pixels[0]][pixels[1]][0]
            new_image[l+1] += patterns[pixels[0]][pixels[1]][1]
            new_image[l+2] += patterns[pixels[0]][pixels[1]][2]
        l += 3

    return new_image, len(new_image)

def enhance3(patterns, image):
    new_image = [[] for i in range(int(len(image)/3*4))]
    l = 0

    for line in range(0, len(image), 3):
        for row in range(0, len(image), 3):
            pixels = [image[line][row:row+3], image[line+1][row:row+3], image[line+2][row:row+3]]
            pixels = list(map(lambda t: "".join(t), pixels))

            new_image[l] += patterns[pixels[0]][pixels[1]][pixels[2]][0]
            new_image[l+1] += patterns[pixels[0]][pixels[1]][pixels[2]][1]
            new_image[l+2] += patterns[pixels[0]][pixels[1]][pixels[2]][2]
            new_image[l+3] += patterns[pixels[0]][pixels[1]][pixels[2]][3]
        l += 4

    return new_image, len(new_image)

patterns = {}

#add_dict(patterns, ["123","456","789"], ["12"])
#exit()

for line in fileinput.input():
    parts = line.split("=>")
    parts[0] = re.sub(r'\s*', '', parts[0])
    parts[1] = re.sub(r'\s*', '', parts[1])
    inputs = parts[0].split("/")
    outputs = parts[1].split("/")

    patterns = add_dict(patterns, inputs, outputs)


for i in range(18):
    if size % 2 == 0:
        image, size = enhance2(patterns, image)
    else:
        image, size = enhance3(patterns, image)

count = 0
for i in range(len(image)):
    for j in range(len(image)):
        if image[i][j] == '#':
            count += 1

print(count)

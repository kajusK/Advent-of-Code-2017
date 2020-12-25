#!/usr/bin/python3

import fileinput


def getWeight(node, name):
    weight = node["value"]
    child_weight = []

    for child in node["children"]:
        cur = getWeight(nodes[child], child)
        weight += cur
        child_weight.append([child, cur])

    for i in range(len(child_weight)):
        if child_weight[i][1] == child_weight[0][1]:
            continue
        print("mismatch in ", name)
        for j in range(len(child_weight)):
            print(child_weight[j][0], child_weight[j][1])
        exit()

    return weight

nodes = {}

for line in fileinput.input():
    line = line.replace(',', '')
    line = line.replace('(', '')
    line = line.replace(')', '')

    parsed = line.split()

    name = parsed[0]
    value = int(parsed[1])
    children = []

    if len(parsed) > 2:
        for i in range(3, len(parsed)):
            children.append(parsed[i])


    nodes[name] = {
            "value": value,
            "children": children,
            "parent": False
            }

for name, node in nodes.items():
    if len(node["children"]) == 0:
        continue

    for child in node["children"]:
        nodes[child]["parent"] = name


master = ""
for name, node in nodes.items():
    if node["parent"] == False:
        master = name
        break

getWeight(nodes[master], master)

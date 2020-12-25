#!/usr/bin/python3

#state = "A"
#steps = 6
#
#states = { "A": [{"v": 1, "dir": 1, "state": "B"}, {"v": 0, "dir": -1, "state": "B"}],
#            "B": [{"v": 1, "dir": -1, "state": "A"}, {"v": 1, "dir": 1, "state": "A"}]}

state = "A"
steps = 12399302

states = { "A": [{"v": 1, "dir": 1, "state": "B"}, {"v": 0, "dir": 1, "state": "C"}],
            "B": [{"v": 0, "dir": -1, "state": "A"}, {"v": 0, "dir": 1, "state": "D"}],
            "C": [{"v": 1, "dir": 1, "state": "D"}, {"v": 1, "dir": 1, "state": "A"}],
            "D": [{"v": 1, "dir": -1, "state": "E"}, {"v": 0, "dir": -1, "state": "D"}],
            "E": [{"v": 1, "dir": 1, "state": "F"}, {"v": 1, "dir": -1, "state": "B"}],
            "F": [{"v": 1, "dir": 1, "state": "A"}, {"v": 1, "dir": 1, "state": "E"}]}

tape = [0 for i in range(steps)]
pos = int(len(tape)/2)

for i in range(steps):
    data = states[state][tape[pos]]
    tape[pos] = data["v"]
    pos += data["dir"]
    state = data["state"]

print(sum(tape))

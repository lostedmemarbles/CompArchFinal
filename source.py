#!/usr/bin/env python3

import sys

print("This doesn't do anything yet!")
filename = sys.argv[1]

openFile = open(filename, "r")

lines = openFile.readlines()
numBytesRead = 0
addressOfInstruction = ""
dataReadIngore = ""
i = 0
while i < len(lines):
    line = lines[i].split()
    print(line)
    if lines[i] == "\n":
        print("empty line")
        i += 1
        continue
    if line[0] == "EIP":
        numBytesRead = line[1][1:2]
        print(numBytesRead)
        addressOfInstruction = line[2]
        print(addressOfInstruction)
        dataReadIgnore = line[3:]
        print(dataReadIgnore)
    if line[0] == "dstM:":
        print("do some other stuff")
    i += 1
    
openFile.close()

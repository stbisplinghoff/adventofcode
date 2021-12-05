# Solution to Advent of Code 2021 day 5
import numpy

# Read input
with open("input.txt") as inFile:
    rawLines = [line.split(" -> ") for line in inFile.read().split("\n")]
lines = []
for line in rawLines:
    start, end = numpy.fromstring(line[0], dtype=int, sep=","), numpy.fromstring(line[1], dtype=int, sep=",")
    lines.append((start, end))

## Part 1
map = numpy.zeros((1000, 1000), dtype=int)
for line in lines:
    start, end = line
    # Skip diagonal lines for now
    if start[0] == end[0]:
        # Up
        if start[1] > end[1]:
            currentPos = end[1]
            while currentPos <= start[1]:
                map[start[0], currentPos] += 1
                currentPos += 1
        # Down
        else:
            currentPos = start[1]
            while currentPos <= end[1]:
                map[start[0], currentPos] += 1
                currentPos += 1
    elif start[1] == end[1]:
        # Left
        if start[0] > end[0]:
            currentPos = end[0]
            while currentPos <= start[0]:
                map[currentPos, start[1]] += 1
                currentPos += 1
        # Right
        else:
            currentPos = start[0]
            while currentPos <= end[0]:
                map[currentPos, start[1]] += 1
                currentPos += 1
zeroCount = 1000 * 1000 - numpy.count_nonzero(map)
print("Solution for part 1:", numpy.count_nonzero(map - 1) - zeroCount)

## Part 2
for line in lines:
    start, end = line
    # Skip straight lines in part 2, already done
    if start[0] == end[0] or start[1] == end[1]:
        continue
    else:
        # Down-right
        if end[0] >= start[0] and end[1] >= start[1]:
            currentPos = start
            while currentPos[0] <= end[0] and currentPos[1] <= end[1]:
                map[currentPos[0], currentPos[1]] += 1
                currentPos += 1
        # Down-left
        elif end[0] <= start[0] and end[1] >= start[1]:
            currentPos = start
            while currentPos[0] >= end[0] and currentPos[1] <= end[1]:
                map[currentPos[0], currentPos[1]] += 1
                currentPos[0] -= 1
                currentPos[1] += 1
        # Up-left
        elif end[0] <= start[0] and end[1] <= start[1]:
            if end[0] <= start[0] and end[1] <= start[1]:
                currentPos = start
                while currentPos[0] >= end[0] and currentPos[1] >= end[1]:
                    map[currentPos[0], currentPos[1]] += 1
                    currentPos -= 1
        # Up-right
        elif end[0] >= start[0] and end[1] <= start[1]:
            currentPos = start
            while currentPos[0] <= end[0] and currentPos[1] >= end[1]:
                map[currentPos[0], currentPos[1]] += 1
                currentPos[0] += 1
                currentPos[1] -= 1
zeroCount = 1000 * 1000 - numpy.count_nonzero(map)
print("Solution for part 2:", numpy.count_nonzero(map - 1) - zeroCount)

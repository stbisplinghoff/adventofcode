# Solution to Advent of Code 2021 day 12
from collections import defaultdict

# Read input
with open("input.txt") as inFile:
    connections = [connection.split("-") for connection in inFile.read().split("\n")]

cavePaths = defaultdict(list)
for connection in connections:
    cavePaths[connection[0]].append(connection[1])
    cavePaths[connection[1]].append(connection[0])

print(cavePaths)


def travel(current, visitedCaves, path, validPathStorage):
    if current == "end":
        validPathStorage.append(list(path))
        return
    for next in cavePaths[current]:
        if next == next.upper() or next not in visitedCaves:
            path.append(next)
            visitedCaves.append(next)
            travel(next, visitedCaves, path, validPathStorage)
            path.pop()
            visitedCaves.pop()


def travel2(current, visitedCaves, path, validPathStorage, singleCaveTwiceFlag):
    if current == "end":
        validPathStorage.append(list(path))
        return
    for next in cavePaths[current]:
        if next != "start" and (
                next == next.upper() or next not in visitedCaves or (next in visitedCaves and not singleCaveTwiceFlag)):
            if next == next.lower() and next in visitedCaves:
                singleCaveTwiceFlag = True
            path.append(next)
            visitedCaves.append(next)
            travel2(next, visitedCaves, path, validPathStorage, singleCaveTwiceFlag)
            path.pop()
            visitedCaves.pop()
            if next == next.lower() and next in visitedCaves:
                singleCaveTwiceFlag = False


validPaths = []
travel("start", ["start"], ["start"], validPaths)
for path in validPaths:
    print(path)
print(len(validPaths))

validPaths = []
travel2("start", ["start"], ["start"], validPaths, False)
for path in validPaths:
    print(path)
print(len(validPaths))

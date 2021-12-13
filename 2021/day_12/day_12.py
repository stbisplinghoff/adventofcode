# Solution to Advent of Code 2021 day 12
from collections import defaultdict

# Read input
with open("input.txt") as inFile:
    connections = [connection.split("-") for connection in inFile.read().split("\n")]

cavePaths = defaultdict(list)
for connection in connections:
    cavePaths[connection[0]].append(connection[1])
    cavePaths[connection[1]].append(connection[0])


def travel(current, path, validPaths):
    if current == "end":
        validPaths.append(list(path))
        return
    for next in cavePaths[current]:
        if next == next.upper() or next not in path:
            path.append(next)
            travel(next, path, validPaths)
            path.pop()


validPaths = []
travel("start", ["start"], validPaths)
print("Solution for part 1:", len(validPaths))


def travel2(current, path, validPaths, singleCaveTwiceFlag):
    if current == "end":
        validPaths.append(list(path))
        return
    for next in cavePaths[current]:
        if next != "start" and (
                next == next.upper() or next not in path or (next in path and not singleCaveTwiceFlag)):
            if next == next.lower() and next in path:
                singleCaveTwiceFlag = True
            path.append(next)
            travel2(next, path, validPaths, singleCaveTwiceFlag)
            path.pop()
            if next == next.lower() and next in path:
                singleCaveTwiceFlag = False


validPaths = []
travel2("start", ["start"], validPaths, False)
print("Solution for part 2:", len(validPaths))

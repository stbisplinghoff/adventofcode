# Solution to Advent of Code 2020 day 3
import math

# Read input
with open("input.txt") as inFile:
    data = inFile.read()
forest = [[1 if c == "#" else 0 for c in line] for line in data.split("\n")]


def run(forest, slope=(3, 1)):
    # Straight forward using for loop and counter
    currentPosition = slope[0]
    hits = 0
    for currentLine in range(slope[1], len(forest), slope[1]):
        hits += forest[currentLine][currentPosition]
        currentPosition = (currentPosition + slope[0]) % len(forest[0])
    return hits


def runfancy(forest, slope=(3, 1)):
    # One-liner but actually 50% slower than -run- when running input data with slope (3,1)
    return [forest[x[0]][x[1]] for x in zip(range(slope[1], len(forest), slope[1]),
                                            [(slope[0] * x) % len(forest[0]) for x in range(1, len(forest))]
                                            )
            ].count(1)


# Part 1
print("Slope (3,1) - Hits:", run(forest))
print("Slope (3,1) - Hits:", runfancy(forest))

# Part 2
print("Solution part 2:", math.prod([run(forest, (l, 1)) for l in range(1, 8, 2)] + [run(forest, (1, 2))]))
print("Solution part 2:", math.prod([runfancy(forest, slope) for slope in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2])]))

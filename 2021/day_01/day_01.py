# Solution to Advent of Code 2021 day 1

# Read input
with open("input.txt") as inFile:
    depthValues = [int(value) for value in inFile.read().split("\n")]

# Part 1
print("Solution for part 1:",
      [depthValues[idx] - depthValues[idx - 1] > 0 for idx in range(1, len(depthValues))].count(True))

# Part 2
slidingWindow = [depthValues[idx - 2] + depthValues[idx - 1] + depthValues[idx] for idx in range(2, len(depthValues))]
print("Solution for part 2:",
      [slidingWindow[idx] - slidingWindow[idx - 1] > 0 for idx in range(1, len(slidingWindow))].count(True))
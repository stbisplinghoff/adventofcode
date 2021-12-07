# Solution to Advent of Code 2021 day 7

# Read input
with open("input.txt") as inFile:
    positions = [int(pos) for pos in inFile.read().split(",")]

## Part 1
fuelDemand = []
for target in range(max(positions)):
    fuelDemand.append(sum([abs(pos - target) for pos in positions]))
print("Part1: Minimum fuel demand {} at position target {}".format(min(fuelDemand), fuelDemand.index(min(fuelDemand))))

## Part 2
fuelDemand = []
fuelConsumption = [sum(range(1, x)) for x in range(2000)]
for target in range(max(positions)):
    fuelDemand.append(sum([fuelConsumption[abs(pos - target) + 1] for pos in positions]))
print("Part2: Minimum fuel demand {} at position target {}".format(min(fuelDemand), fuelDemand.index(min(fuelDemand))))

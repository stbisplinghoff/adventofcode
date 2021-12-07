# Solution to Advent of Code 2021 day 6
import numpy

# Read input
with open("input.txt") as inFile:
    initialFishState = [int(age) for age in inFile.read().split(",")]

## Part 1
# Simulate every fish in a numpy array
fish = numpy.array(initialFishState, dtype=int)
for day in range(80):
    newFish = fish.size - numpy.count_nonzero(fish)
    fish -= 1
    fish = numpy.append(numpy.where(fish == -1, 6, fish), [8] * newFish)
print("Solution for part 1:", fish.size)

## Part 2
# Different approach, as numbers will get too large for handling an array element for each fish
# Do not store every fish but only number of fish per age
fishPopulation = {age: initialFishState.count(age) for age in range(9)}
for day in range(256):
    newFish = fishPopulation[0]
    for age in range(8):
        fishPopulation[age] = fishPopulation[age+1]
    fishPopulation[6] += newFish
    fishPopulation[8] = newFish
print("Solution for part 2:", sum(fishPopulation.values()))
# Solution to Advent of Code 2021 day 11
import numpy
from scipy.signal import convolve2d

# Read input
with open("input.txt") as inFile:
    field = numpy.array([[int(c) for c in row] for row in inFile.read().split("\n")])

sumFlashes = 0
for step in range(1,1000):
    field += 1
    flashes = numpy.zeros(field.shape)
    checkFlashes = True
    while checkFlashes:
        newFlashes = numpy.where(field >= 10, 1, 0)
        newFlashes = numpy.where(flashes == 0, newFlashes, 0)
        flashes += newFlashes
        field = field + convolve2d(newFlashes, numpy.ones((3, 3)), mode="same").astype(int)
        if step <= 100:
            sumFlashes += numpy.sum(newFlashes)
        checkFlashes = numpy.sum(newFlashes) > 0
    field = numpy.where(flashes == 1, 0, field)
    if numpy.all(flashes == 1):
        print("Solution for part 2:", step)
        break
print("Solution for part 1:", sumFlashes)

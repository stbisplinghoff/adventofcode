# Solution to Advent of Code 2021 day 9
import numpy

# Read input
with open("input.txt") as inFile:
    puzzleArray = numpy.array([[int(value) for value in list(row)] for row in inFile.read().split("\n")])

## Part 1
# Create a border with high values around
map = numpy.ones((puzzleArray.shape[0] + 2, puzzleArray.shape[1] + 2), dtype=int) * 10
map[1:-1, 1:-1] = puzzleArray

# Compare each value with a shifted representation of the map
localMin = ((map < numpy.roll(map, 1, 0)) &
            (map < numpy.roll(map, -1, 0)) &
            (map < numpy.roll(map, 1, 1)) &
            (map < numpy.roll(map, -1, 1)))[1:-1, 1:-1]
# Calculate risk (reshape to 1D for list comprehension)
puzzleArray1D = puzzleArray.reshape(puzzleArray.size)
localMin1D = localMin.reshape(localMin.size)
print("Solution for part 1:", sum([1 + puzzleArray1D[i] if localMin1D[i] else 0 for i in range(puzzleArray1D.size)]))


## Part 2
# For every identified local minimum, crawl the map recursively to fill the basins
def fillBasin(basin, map, currentPos, evaluatedPos):
    evaluatedPos[tuple(currentPos)] = 1
    for step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newPos = currentPos + step
        if not (0 <= newPos[0] < map.shape[0] and 0 <= newPos[1] < map.shape[1]):
            continue
        if (evaluatedPos[tuple(newPos)] == 0) and (9 > map[tuple(newPos)] > map[tuple(currentPos)]):
            basin[tuple(newPos)] = 1
            fillBasin(basin, map, newPos, evaluatedPos)


basinSizes = []
for minPos in numpy.argwhere(localMin):
    basin = numpy.zeros(puzzleArray.shape, dtype=int)
    basin[tuple(minPos)] = 1
    evaluatedPos = numpy.zeros(puzzleArray.shape, dtype=int)
    fillBasin(basin, puzzleArray, minPos, evaluatedPos)
    basinSizes.append(numpy.sum(basin))
print("Solution for part 2:", numpy.prod(sorted(basinSizes)[-3:]))

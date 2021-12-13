# Solution to Advent of Code 2021 day 13
import numpy

# Read input
with open("input.txt") as inFile:
    data = inFile.read().split("\n\n")
    dots = [tuple([int(dot) for dot in line.split(",")]) for line in data[0].split("\n")]
    print(dots)
    folds = []
    for foldingInstructions in data[1].split("\n"):
        axis = 0 if foldingInstructions[11] == "x" else 1
        coordinate = int(foldingInstructions[13:])
        folds.append((axis, coordinate))

coordinates = [[],[]]
for dot in dots:
    coordinates[0].append(dot[0])
    coordinates[1].append(dot[1])

paper = numpy.zeros((max(coordinates[0])+1,max(coordinates[1])+2), dtype=int)
for dot in dots:
    paper[dot] = 1

foldedPaper = numpy.array(paper)
firstFoldDots = 0
for axis, coordinate in folds:
    print(foldedPaper.shape, axis, coordinate)
    if axis == 1:
        part1 = foldedPaper[:, :coordinate]
        part2 = foldedPaper[:, coordinate+1:]
        print(part1.shape, part2.shape, numpy.flip(part2, 1).shape)
        foldedPaper = numpy.clip(part1 + numpy.flip(part2, 1), 0, 1)
    else:
        part1 = foldedPaper[:coordinate, :]
        part2 = foldedPaper[coordinate+1:, :]
        print(part1.shape, part2.shape, numpy.flip(part2, 0).shape)
        foldedPaper = numpy.clip(part1 + numpy.flip(part2, 0), 0, 1)
    if firstFoldDots == 0:
        firstFoldDots = numpy.sum(foldedPaper)
print("Solution for part 1:", firstFoldDots)

print("Solution for part 2:")
print(foldedPaper.transpose())
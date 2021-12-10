# Solution to Advent of Code 2021 day 10

# Read input
with open("input.txt") as inFile:
    lines = inFile.read().split("\n")

## Part 1 + 2
scoreTable1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
scoreTable2 = {"(": 1, "[": 2, "{": 3, "<": 4}
pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
score_part1 = 0
scoreList_part2 = []
for line in lines:
    chunkStack = []
    for char in line:
        if char in pairs:
            if len(chunkStack) == 0 or pairs[char] != chunkStack.pop():
                score_part1 += scoreTable1[char]
                chunkStack = []
                break
        else:
            chunkStack.append(char)
    score = 0
    while len(chunkStack):
        score = score * 5 + scoreTable2[chunkStack.pop()]
    if score > 0:
        scoreList_part2.append(score)
print("Solution for part 1:", score_part1)
print("Solution for part 2:", sorted(scoreList_part2)[int((len(scoreList_part2)) / 2)])

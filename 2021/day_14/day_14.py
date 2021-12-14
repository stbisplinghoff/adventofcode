# Solution to Advent of Code 2021 day 14
from collections import defaultdict

# Read input
rules = {}
with open("input.txt") as inFile:
    start, ruleData = inFile.read().split("\n\n")
    rules = {k: v for k, v in [rule.split(" -> ") for rule in ruleData.split("\n")]}

currentChain = str(start)
for step in range(1,11):
    newChain = currentChain[0]
    for pair in range(len(currentChain)-1):
        newChain += rules[currentChain[pair:pair+2]] + currentChain[pair+1]
    currentChain = str(newChain)
occurences = {c: currentChain.count(c) for c in set(currentChain)}
mostCommonCharCount = occurences[max(occurences, key=occurences.get)]
leastCommonCharCount = occurences[min(occurences, key=occurences.get)]
print("Solution for part 1:", mostCommonCharCount-leastCommonCharCount)


## Part 2: Different approach, order of elements is irrelevant, just count number of pair occurences
pairs = defaultdict(int)
for pair in range(len(start)-1):
    pairs[start[pair:pair+2]] += 1
for step in range(1,41):
    currentPairs = {pair: occurences for pair, occurences in pairs.items() if occurences > 0}
    for pair, occurences in currentPairs.items():
        pairs[pair] -= occurences
        pairs[pair[0]+rules[pair]] += occurences
        pairs[rules[pair]+pair[1]] += occurences
characters = defaultdict(int)
for pair, occurences in pairs.items():
    characters[pair[1]] += occurences
characters[start[0]] += 1
mostCommonCharCount = characters[max(characters, key=characters.get)]
leastCommonCharCount = characters[min(characters, key=characters.get)]
print("Solution for part 2:", mostCommonCharCount-leastCommonCharCount)

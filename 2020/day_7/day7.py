# Solution to Advent of Code 2020 day 7
import re

# Read data
with open("input.txt") as inFile:
    rules = inFile.read().split("\n")

# Organize bag rules
keyExtractor = re.compile(r"(?P<key>\w+ \w+) bags contain")
insideExtractor = re.compile(r"((?P<amount>\d+) (?P<color>\w+ \w+)|no other) bags?(.|,)")
ruleMap = {}
for rule in rules:
    keyMatch = keyExtractor.match(rule)
    ruleMap[keyMatch.group("key")] = {}
    insideBagMatch = insideExtractor.search(rule, keyMatch.end())
    while insideBagMatch is not None:
        if insideBagMatch.group("color") is not None:
            ruleMap[keyMatch.group("key")][insideBagMatch.group("color")] = int(insideBagMatch.group("amount"))
        insideBagMatch = insideExtractor.search(rule, insideBagMatch.end())

# Part 1
carrier = {"shiny gold"}
formerCarrierSize = 0
while len(carrier) > formerCarrierSize:
    formerCarrierSize = len(carrier)
    for key, allowedBags in ruleMap.items():
        if any([color in allowedBags for color in carrier]):
            carrier |= {key}
print("Solution for part 1:", len(carrier) - 1)

# Part 2
currentBagList = ruleMap["shiny gold"]
individualBags = 0
while len(currentBagList) > 0:
    individualBags += sum([number for number in currentBagList.values()])
    newBagList = {}
    for color in currentBagList:
        for newColor, amount in ruleMap[color].items():
            if newColor not in newBagList:
                newBagList[newColor] = 0
            newBagList[newColor] += amount * currentBagList[color]
    currentBagList = dict(newBagList)
print("Solution for part 2:", individualBags)

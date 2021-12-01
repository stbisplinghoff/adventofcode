# Solution to Advent of Code 2020 day 6

# Read data
with open("input.txt") as inFile:
    groups = inFile.read().split("\n\n")

# Part 1
yesAnswers = sum([len(set(group.replace("\n", ""))) for group in groups])
print("Solution for part 1:", yesAnswers)

# Part 2
yesAnswers = 0
for group in groups:
    persons = group.split("\n")
    sameAnswers = set(persons[0])
    for person in persons[1:]:
        sameAnswers &= set(person)
    yesAnswers += len(sameAnswers)
print("Solution for part 2:", yesAnswers)

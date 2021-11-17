# Solution to Advent of Code 2020 day 2
import re

# Read data
with open("input.txt") as inFile:
    data = inFile.read().split("\n")

# Part 1 & 2 counters
validPasswords_p1 = 0
validPasswords_p2 = 0
fieldExtractor = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<key>\w): (?P<passwd>\w+)")
for password in data:
    fields = fieldExtractor.match(password)
    if int(fields.group("min")) <= fields.group("passwd").count(fields.group("key")) <= int(fields.group("max")):
        validPasswords_p1 += 1
    if (fields.group("passwd")[int(fields.group("min")) - 1] == fields.group("key")) \
            ^ (fields.group("passwd")[int(fields.group("max")) - 1] == fields.group("key")):
        validPasswords_p2 += 1
print("Valid passwords part 1:", validPasswords_p1)
print("Valid passwords part 2:", validPasswords_p2)

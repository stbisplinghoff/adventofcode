# Solution to Advent of Code 2021 day 2

# Read input
with open("input.txt") as inFile:
    instructions = [command.split(" ") for command in inFile.read().split("\n")]

# Part 1:
position, depth = 0, 0
for command, value in instructions:
    if command == "forward":
        position += int(value)
    elif command == "up":
        depth -= int(value)
    elif command == "down":
        depth += int(value)
print("Solution for part 1:", position * depth)

# Part 2:
position, depth, aim = 0, 0, 0
for command, value in instructions:
    if command == "forward":
        position += int(value)
        depth += int(value) * aim
    elif command == "up":
        aim -= int(value)
    elif command == "down":
        aim += int(value)
print("Solution for part 2:", position * depth)

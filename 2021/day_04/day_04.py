# Solution to Advent of Code 2021 day 4

# Read input
with open("input.txt") as inFile:
    data = inFile.read().split("\n\n")
numbers = [int(value) for value in data[0].split(",")]
fields = [[[int(element) for element in column.replace("  ", " ").split(" ")[-5:]] for column in rows.split("\n")] for
          rows in data[1:]]


def checkRowBingo(field):
    result = False
    for row in field:
        if sum(row) == 0:
            result = True
    return result


def checkColumnBingo(field):
    result = False
    for column in range(5):
        column = [field[row][column] for row in range(5)]
        if sum(column) == 0:
            result = True
    return result


def checkNumber(field, number):
    bingo = False
    for row in field:
        if number in row:
            row[row.index(number)] = 0
            bingo = checkRowBingo(field) | checkColumnBingo(field)
    return bingo


## Part 1
bingoFlag = False
for round in range(len(numbers)):
    number = numbers[round]
    for field in fields:
        if checkNumber(field, number):
            print("Bingo!", field)
            print("Sum of remaining fields:", sum([sum(row) for row in field]))
            print("Solution for part 1: ", sum([sum(row) for row in field]) * number)
            bingoFlag = True
            break
    if bingoFlag:
        break

## Part 2
for round in range(len(numbers)):
    winningFields = []
    number = numbers[round]
    for fieldIdx in range(len(fields)):
        field = fields[fieldIdx]
        if checkNumber(field, number):
            winningFields.append(field)
    if len(winningFields):
        for field in winningFields:
            fields.remove(field)
        if len(fields) == 0:
            print("Last winning field:", winningFields[-1])
            print("Solution for part 2: ", sum([sum(row) for row in winningFields[-1]]) * number)

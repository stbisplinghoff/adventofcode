# Solution to Advent of Code 2020 day 23
from datetime import datetime


# PUZZLE_INPUT = "389125467"
PUZZLE_INPUT = "198753462"

# PART 1
# Convert to list for better handling
startTime = datetime.now()
cups = [int(cupID) for cupID in PUZZLE_INPUT]
cupCount = len(cups)
currentCup = 0
for move in range(100):
    # Rotate so that currentCup is at the beginning
    cups = cups[currentCup:] + cups[:currentCup]
    currentLabel = cups[0]
    pickedCups = cups[1:4]
    del cups[1:4]
    # Calculate destination label (-2 / + 1 to allow modulo to wrap around 1 instead of 0)
    newLabel = ((currentLabel - 2) % cupCount) + 1
    # Destination cup must not be picked up currently, search further if this is the case
    while newLabel not in cups:
        newLabel = ((newLabel - 2) % cupCount) + 1
    # Insert picked cups after destination cup
    cups = cups[:cups.index(newLabel) + 1] + pickedCups + cups[cups.index(newLabel) + 1:]
    # Select new cup
    currentCup = cups.index(currentLabel)
    currentCup = (currentCup + 1) % cupCount

# Repeat circle for easier access when seeking for cups after cup label 1
cups = cups + cups
print("Final order for part 1:", "".join(str(id) for id in cups[cups.index(1) + 1:cups.index(1) + 9]))

# PART 2
# Using a list is not performant enough to handle 1e6 items and 1e7 cycles.
# Using a linked list to minimize the amount of data access / shuffle. Only three write operations to dictionary
# per cycle should be necessary
# Initial cups
cups = {}
for i in range(8):
    cups[int(PUZZLE_INPUT[i])] = int(PUZZLE_INPUT[i+1])
cups[int(PUZZLE_INPUT[8])] = 10
# Add remaining cups
for i in range(10, 1000001):
    cups[i] = i+1
cups[1000000] = int(PUZZLE_INPUT[0])

cupCount = len(cups)
currentCup = int(PUZZLE_INPUT[0])
for move in range(10000000):
    # Pick three
    pickedFirst = cups[currentCup]
    pickedMiddle = cups[pickedFirst]
    pickedLast = cups[pickedMiddle]
    # Remove from chain by re-linking current cup
    cups[currentCup] = cups[pickedLast]
    destinationCup = ((currentCup - 2) % cupCount) + 1
    # Destination cup must not be within those cups that are currently picked, search further if this is the case
    while destinationCup in [pickedFirst, pickedMiddle, pickedLast]:
        destinationCup = ((destinationCup - 2) % cupCount) + 1
    # Insert picked cups by re-linking both ends
    cups[pickedLast] = cups[destinationCup]
    cups[destinationCup] = pickedFirst
    currentCup = cups[currentCup]

# Neighbours right to 1 are the solution
print("Neighbours:", cups[1], cups[cups[1]])
print("Product is solution for part 2:", cups[1]*cups[cups[1]])
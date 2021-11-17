# Solution to Advent of Code 2020 day 5

# Read data
with open("input.txt") as inFile:
    seats = inFile.read().split("\n")

# Part 1
seatIDs = []
for seat in seats:
    row = int(seat[:7].replace("F", "0").replace("B", "1"), base=2)
    column = int(seat[7:].replace("L", "0").replace("R", "1"), base=2)
    seatIDs.append(row * 8 + column)
print("Max seat ID:", max(seatIDs))

# Part 2
missingSeats = set(range(1023)) - set(seatIDs)
for seat in missingSeats:
    if not ((seat - 1) in missingSeats or (seat + 1) in missingSeats):
        mySeat = seat
        break
print("My seat ID:", mySeat)

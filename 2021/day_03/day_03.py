# Solution to Advent of Code 2021 day 3

# Read input
with open("input.txt") as inFile:
    codes = [[int(c) for c in code] for code in inFile.read().split("\n")]

### Part 1
gamma = 0
for idx in range(len(codes[0])):
    # Count the number of "ones" at position idx for every code
    sumOfOnes = 0
    for code in codes:
        sumOfOnes += code[idx]
    # Build solution by bit shifting after every idx and adding the most common bit
    gamma = (gamma << 1) + int(2 * sumOfOnes > len(codes))
# Instead of recalculating everything again, solution for epsilon is just a bitwise inversion of gamma
epsilon = gamma ^ ((1 << 12) - 1)
print("Solution for part 1:", gamma * epsilon)


### Part 2
# Practically same as for part 1 but carrying over codes that have the significant bit
# Defining a method here to avoid having the same code twice. Only difference is the "checkDigit" which
# differentiates between the oxygen/co2 puzzle parts.
def getSolution(codes, checkDigit):
    codes = list(codes)
    for idx in range(len(codes[0])):
        codesNextCycle = []
        # Count the number of "ones" at position idx for every code
        sumOfOnes = 0
        for code in codes:
            sumOfOnes += code[idx]
        # Check condition for all codes and push accepted codes to the list for the next cycle
        for code in codes:
            if (2 * sumOfOnes >= len(codes) and code[idx] == checkDigit) \
                    or (2 * sumOfOnes < len(codes) and code[idx] == checkDigit ^ 1):
                codesNextCycle.append(code)
        # Copy the list for next cycle, abort if only one code is remaining
        codes = list(codesNextCycle)
        if len(codes) == 1:
            break
    # Build the decimal number by shifting every bit in the list according to its position and simply sum up
    return sum([codes[0][idx] << (11 - idx) for idx in range(12)])


print("Solution for part 2:", getSolution(codes, 1) * getSolution(codes, 0))

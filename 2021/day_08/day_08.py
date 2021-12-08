# Solution to Advent of Code 2021 day 8

# Read input
with open("input.txt") as inFile:
    observations = {pattern: outputValue for pattern, outputValue in
                    [line.split(" | ") for line in inFile.read().split("\n")]}

## Part 1
# Count all output values with 2,3,4,7 segments
easyDigits = 0
for value in observations.values():
    easyDigits += [2 <= len(number) <= 4 or len(number) == 7 for number in value.split(" ")].count(True)
print("Solution for part 1:", easyDigits)

## Part 2
# Explanations reference to the order
#     aaaa
#    b    c
#    b    c
#     dddd
#    e    f
#    e    f
#     gggg
overallSum = 0
for pattern, value in observations.items():
    wireMap = {}
    segments = pattern.split(" ")
    segment1 = list([s for s in segments if len(s) == 2][0])
    segment4 = list([s for s in segments if len(s) == 4][0])
    segment7 = list([s for s in segments if len(s) == 3][0])
    segment8 = list([s for s in segments if len(s) == 7][0])
    segment6or9or0 = list([s for s in segments if len(s) == 6])
    segment2or3or5 = list([s for s in segments if len(s) == 5])
    # Identify a by comparing 1 and 7
    wireMap["a"] = [s for s in segment7 if s not in segment1][0]
    # Identify c. Compare 1 with 6,9,0, where c is missing
    for s in segment6or9or0:
        if segment1[0] not in list(s):
            wireMap["c"] = segment1[0]
        elif segment1[1] not in list(s):
            wireMap["c"] = segment1[1]
    # Identify f (remaining segment from 1)
    wireMap["f"] = segment1[0] if segment1[1] == wireMap["c"] else segment1[1]
    # Identify 6 (8 - c segment)
    segment6 = list(set(segment8).difference(set(wireMap["c"])))
    # Identify 5 (from 2,3,5 where c is missing)
    # Identify 2 (from 2,3,5 where f is missing)
    for s in segment2or3or5:
        if wireMap["c"] not in list(s):
            segment5 = s
        if wireMap["f"] not in list(s):
            segment2 = s
    # Identify 3 (remaining from 2,3,5)
    segment2or3or5.remove(segment2)
    segment2or3or5.remove(segment5)
    segment3 = list(segment2or3or5[0])
    # Identify 9 (3 + 4)
    segment9 = list(set(segment3).union(set(segment4)))
    # Identify d segment ((3 - 7) AND 4)
    wireMap["d"] = list(set(segment3).difference(set(segment7)).intersection(set(segment4)))[0]
    # Identify 0 (8 - d segment)
    segment0 = list(set(segment8).difference(set(wireMap["d"])))

    digits = {"".join(sorted(segment1)): "1", "".join(sorted(segment2)): "2", "".join(sorted(segment3)): "3",
              "".join(sorted(segment4)): "4", "".join(sorted(segment5)): "5", "".join(sorted(segment6)): "6",
              "".join(sorted(segment7)): "7", "".join(sorted(segment8)): "8", "".join(sorted(segment9)): "9",
              "".join(sorted(segment0)): "0"}
    overallSum += int("".join([digits["".join(sorted(list(x)))] for x in value.split(" ")]))
print("Solution for part 2:", overallSum)

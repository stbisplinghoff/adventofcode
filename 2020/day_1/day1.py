# Solution for day 1 challenge

# Read input data
with open("input.txt", "r") as f:
    values = f.read().split("\n")

# Part 1
for i in range(len(values)):
    for j in range(i+1, len(values)):
        if int(values[i])+int(values[j]) == 2020:
            print("Found at index {} and {}: {}, {}".format(i, j, values[i], values[j]))
            print("Product is: ", int(values[i])*int(values[j]))

# Part 2
for i in range(len(values)):
    for j in range(i+1, len(values)):
        for k in range(j + 1, len(values)):
            if int(values[i])+int(values[j])+int(values[k]) == 2020:
                print("Found at index {}, {} and {}: {}, {}, {}".format(i, j, k, values[i], values[j], values[k]))
                print("Product is: ", int(values[i])*int(values[j])*int(values[k]))
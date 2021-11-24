# Solution to Advent of Code 2020 day 25

PUBLIC_KEYS = {"card": 6929599, "door": 2448427}

def transform(subjectNumber, loopSize):
    result = 1
    for i in range(loopSize):
        result = (result * subjectNumber) % 20201227
    return result

# During search, the transform does not need to restart again for every new (increasing loop size). Just reuse the value
# from the last trial. "transform" function is later then used for encryption key calculation (one full cycle from
# the beginning)
cardLoopSize = doorLoopSize = 0
loopResult = 1
# Due to the modulo operation the maximum size of each loop size is known
for loopSize in range(1,20201227):
    loopResult = (loopResult * 7) % 20201227
    if loopResult == PUBLIC_KEYS["card"]:
        cardLoopSize = loopSize
        print("Found card:", cardLoopSize)
    if loopResult == PUBLIC_KEYS["door"]:
        doorLoopSize = loopSize
        print("Found door:", doorLoopSize)
    if cardLoopSize>0 and doorLoopSize>0:
        break

print("Encryption key:", transform(PUBLIC_KEYS["card"], doorLoopSize))
print("Encryption key:", transform(PUBLIC_KEYS["door"], cardLoopSize))


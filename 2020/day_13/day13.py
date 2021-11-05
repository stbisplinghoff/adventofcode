# Solution for day 13 challenge

inputdata = """1006605
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,883,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,797,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"""

# Read data
currentTime = int(inputdata.split("\n")[0])
busList = [int(i) for i in inputdata.split("\n")[1].split(",") if i != "x"]

# Part 1
waitTimes = [i-(currentTime % i) for i in busList]
nextBusID = busList[waitTimes.index(min(waitTimes))]
print("Solution: ", nextBusID * min(waitTimes))

# Part 2
# Solve (t + d_i) % n_i = 0   for a set of delays and numbers (bus IDs)
# This is the brute force method, does around 10^13 timestamps/hour with my input. Not feasible :-/
busListComplete = [int(i) if i != "x" else -1 for i in inputdata.split("\n")[1].split(",") ]
delayList = [busListComplete.index(i) for i in busList]
currentTimeStamp = -delayList[busList.index(max(busList))]
found = False
stepSize = busList[busList.index(max(busList))]
from datetime import datetime
startTime = datetime.now()
while not found:
    currentTimeStamp += stepSize
    found = all([(currentTimeStamp + delayList[i]) % busList[i] == 0 for i in range(len(busList))])
print("Solution:", currentTimeStamp, ". Processing time:", (datetime.now()-startTime))

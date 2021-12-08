from statistics import * 

data = open('inputData_daySeven.txt', 'r').read().split('\n')

#Clean up data
crabPos = []
data = str(data[0])
data = data.replace(",", " ")
crabPos = [int(i) for i in data.split()]

#Variables
fuelDict = {}
fuelPosDict = {
    0 : 0,
    1 : 1,
    2 : 3
}
#Crab positional stats
crabPosCopy = crabPos.copy()
crabPosCopy.sort()
maxPos = crabPosCopy[-1] #0
minPos = crabPosCopy[0] #1936
medPos = median(crabPosCopy) #333
meanPos = mean(crabPosCopy) #479.59

for i in range(3, maxPos + 1):
    positionsMoved = i
    cost = i + fuelPosDict[i-1]
    fuelPosDict.update({positionsMoved : cost})

print(fuelPosDict)


for i in range(maxPos):
    fuelSum = 0
    for x in crabPos:
        if x > i:
            posMoves = x - i
            fuelCost = fuelPosDict[posMoves]
        else:
            posMoves = i - x
            fuelCost = fuelPosDict[posMoves]
        fuelSum += fuelCost
    fuelDict.update({f"Pos_{i}" : fuelSum})

fuelValues = list(fuelDict.values())
fuelValues.sort()
minValue = fuelValues[0]

print(minValue)

'''
So this just needs the fuelCost calc changed.

I'm quite proud myself for this one. Didn't even try to brute force it. 
Recognised quite quickly that it would be way too much computation and I remembered
about dynamic programming and so created a dictionary with fuelCosts for the number of moves 
required and used that so that no complicated computation has to take place in the search for 
the appropriate position. 

I think this could be improved, however, it would tailored to the individual input. Probably
basing the numbers of positions checked on some combination of the mean and median would cut
down the amount of work needed significantly. However, it only took a second or so for my input 
here.
'''

from statistics import * 

data = open('inputData_daySeven.txt', 'r').read().split('\n')

#Clean up data
crabPos = []
data = str(data[0])
data = data.replace(",", " ")
crabPos = [int(i) for i in data.split()]

#Get maximum position and minimum position
crabPosCopy = crabPos.copy()
crabPosCopy.sort()
maxPos = crabPosCopy[-1] #0
minPos = crabPosCopy[0] #1936
medPos = median(crabPosCopy) #333
meanPos = mean(crabPosCopy) #479.59

fuelDict = {}

for i in range(maxPos):
    fuelSum = 0
    for x in crabPos:
        if x > i:
            fuelCost = x - i
        else:
            fuelCost = i - x
        fuelSum += fuelCost
    fuelDict.update({f"Pos_{i}" : fuelSum})

fuelValues = list(fuelDict.values())
fuelValues.sort()
minValue = fuelValues[0]

print(minValue)

'''
Correct!
Intuitive algorithm but not efficient at all. 
'''

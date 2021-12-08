data = open('inputData_daySix.txt', 'r').read().split('\n')

#Clean up data
data = data[0]
data = data.replace(',', '')
fishPopulation = []
for i in data:
    fishPopulation.append(int(i))

#NewFishBorn
newFish = {}
fishDict = {}

for i in range(80):
    x = len(fishPopulation)
    for y in range(x):
        if fishPopulation[y] == 0:
            fishPopulation.append(8)
            fishPopulation[y] = 6
            if f"day{i}" in newFish:
                newFish[f"day{i}"] += 1
            else:
                newFish.update({f"day{i}" : 1})
        else:
            fishPopulation[y] -= 1
    fishDict.update({f"day{i}" : len(fishPopulation)})
            
'''
#Check manually for sequence
for i in newFish.items():
    print(i)
    print('\n')

#Sequence found n = (n-7) + (n-9)
'''

#Update dict up to day 256
for i in range(80, 256):
    value = fishDict[f"day{i-7}"]  + fishDict[f"day{i-9}"]
    fishDict.update({f"day{i}" : value})

print(fishDict['day255'])
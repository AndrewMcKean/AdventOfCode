data = open('inputData_dayThree.txt', 'r').read().split('\n')

posDict = {
            'pos0': 0, 
            'pos1': 0,
            'pos2': 0,
            'pos3': 0,
            'pos4': 0,
            'pos5': 0,
            'pos6': 0,
            'pos7': 0,
            'pos8': 0,
            'pos9': 0,
            'pos10': 0,
            'pos11': 0,
        }

gammaRate = ""
epsilonRate = ""

for i in range(len(data) - 1):
    currNum = data[i]
    for x in range(12):
        if currNum[x] == "1":
            posDict.update({f"pos{x}": posDict[f"pos{x}"] + 1})

#Get the finalBinary number
for i in range(len(posDict)):
    if posDict[f"pos{i}"] > 500:
        gammaRate += '1'
    else:
        gammaRate += '0'

#Reverse the finalBinary number
for i in gammaRate:
    if i == "1":
        epsilonRate += '0'
    else:
        epsilonRate += '1'

#Convert to int
gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate, 2)

#Solve
powerConsumption = gammaRate * epsilonRate
print(powerConsumption)

'''
Got it.

Took a lot longer than yesterday, however.
'''
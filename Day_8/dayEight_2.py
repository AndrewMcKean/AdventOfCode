data = open('inputData_dayEight.txt', 'r').read().split('\n')
fData = []
x = 0

for i in data:
    fData.append(i.split())


def decode(item):
    checkDict = {}
    numDict = {
        0 : '',
        1 : '',
        2 : '',
        3 : '',
        4 : '',
        5 : '',
        6 : '',
        7 : '',
        8 : '',
        9 : ''
        }
    breakPoint = item.index('|')
    inputData = []
    outputData = []
    output = []
    outputStr = ""
    for i in range(breakPoint):
        inputData.append(item[i])
    for i in range(breakPoint + 1, len(item)):
        outputData.append(item[i])

    for i in item:
        if len(i) == 2:
            numDict[1] = i
        if len(i)  == 4:
            numDict[4] = i
        if len(i) == 3:
            numDict[7] = i
        if len(i) == 7:
            numDict[8] = i 

    fives = []
    sixes = []

    for i in item:
        if len(i) == 6:
            sixes.append(i)
        elif len(i) == 5:
            fives.append(i)

    posDict = {
        'a' : '',
        'b' : '',
        'c' : '',
        'd' : '',
        'e' : '',
        'f' : '',
        'g' : '',
        }

    posDict['a'] = [x for x in numDict[7] if x not in numDict[1]]

    #Get 6 and update 'c' in posDict
    diffList = []
    for i in range(len(sixes)):
        diff = [x for x in numDict[1] if x not in sixes[i]]
        if diff != []:
            posDict['c'] = diff
            numDict[6] = sixes[i]
            sixes.remove(sixes[i])
            break
    #Get 0 and update 'd'
    diffList = []
    for i in range(len(sixes)):
        diff = [x for x in numDict[4] if x not in sixes[i]]
        if diff != []:
            posDict['d'] = diff
            numDict[0] = sixes[i]
            sixes.remove(sixes[i])
            break
    #Get 9 and update 'e'
    numDict[9] = sixes[0]
    diff = [x for x in numDict[8] if x not in sixes[0]]
    posDict['e'] = diff

    #Get 'f'
    strSoFar = posDict['a'][0] + posDict['c'][0]
    posDict['f'] = [x for x in numDict[1] if x not in strSoFar]

    #Get 'b'
    strSoFar = posDict['c'][0] + posDict['d'][0] + posDict['f'][0]
    posDict['b'] = [x for x in numDict[4] if x not in strSoFar]

    #Get 'g'
    strSoFar = strSoFar + posDict['a'][0] + posDict['b'][0] + posDict['e'][0]
    posDict['g'] = [x for x in numDict[8] if x not in strSoFar]



    #Craft 2
    numDict[2] = (posDict['a'][0]
            + posDict['c'][0]
            + posDict['d'][0]
            + posDict['e'][0]
            + posDict['g'][0])

    #Craft 3
    numDict[3] = (posDict['a'][0]
            + posDict['c'][0]
            + posDict['d'][0]
            + posDict['f'][0]
            + posDict['g'][0])

    #Craft 5
    numDict[5] = (posDict['a'][0]
            + posDict['b'][0]
            + posDict['d'][0]
            + posDict['f'][0]
            + posDict['g'][0])

    #Flip keys/values and sort in numDict
    for i in numDict.items():
        srtKey = sorted(i[1])
        nKey = "".join(srtKey)
        checkDict.update({nKey : i[0]})

    #Clean and sort outputNums
    for i in outputData:
        sorted_ch = sorted(i)
        newStr = "".join(sorted_ch)
        output.append(newStr)
    
    #Get output num as str
    for i in output:
        outputStr += (str(checkDict[i]))

    return int(outputStr)
        


for i in fData:
    x += decode(i)

print(x)
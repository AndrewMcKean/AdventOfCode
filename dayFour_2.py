import numpy as np
import numpy.ma as ma
callSheet = [79,9,13,43,53,51,40,47,56,27,0,14,33,60,61,36,72,48,83,42,10,86,41,75,16,80,15,93,95,45,68,96,84,11,85,63,18,31,35,74,71,91,39,88,55,6,21,12,58,29,69,37,44,98,89,78,17,64,59,76,54,30,65,82,28,50,32,77,66,24,1,70,92,23,8,49,38,73,94,26,22,34,97,25,87,19,57,7,2,3,46,67,90,62,20,5,52,99,81,4]
data = open('inputData_dayFour.txt', 'r').read().split('\n')

#Set up variables
board = []
boardsList = []
winner = []
winningNum = 0
winDict = {}

#Remove empty items
dataNoEmpty = []
dataNoEmpty[:] = [x for x in data if not (x == "")]

#Convert each row to a list of strings
for i in range(len(dataNoEmpty)):
    dataNoEmpty[i] = str.split(dataNoEmpty[i])

#Convert each string in each list to an int
for i in range(len(dataNoEmpty)):
    for x in range(5):
        dataNoEmpty[i][x] = int(dataNoEmpty[i][x])

count = 0
#Group into 5x5 boards
for i in range(len(dataNoEmpty)):
    if count != 5:
        board.append(dataNoEmpty[i])
        count += 1
        
    if count == 5:
        boardsList.append(board)
        count = 0
        board = []

#Convert boardsList to numpy array
boardsList = np.array(boardsList)

found = False
for i in range(len(callSheet)):
    num = callSheet[i]
    s = np.where(boardsList == num)
    if found:
        break
    else:
        #Mark off numbers on boards
        for x in range(len(s[0])):
            boardsList[s[0][x]][s[1][x]][s[2][x]] = boardsList[s[0][x]][s[1][x]][s[2][x]] - num

        
        #Check for complete cols/rows
        for y in range(len(boardsList)):
            curr = boardsList[y]
            rowSum = np.sum(curr, axis=1)
            colSum = np.sum(curr, axis=0)

            print(y)
            rowCheck = np.where(rowSum == 0)
            colCheck = np.where(colSum == 0)
            if(rowCheck[0].size > 0 or colCheck[0].size > 0):
                winDict.update({y: 'winner'})
                if len(winDict.keys()) + 1 == 101:
                    winner = curr
                    winningNum = num
                    found = True
                    print(winner)
                    print(boardsList[39])
                    break

print(winningNum * np.sum(winner))

'''
This. Was. Grueling.

I haven't done anything this hard before. 
Perhaps that's not quite right. I haven't done anything before that I've been this
unfamiliar with. I've only used numpy arrays in my machine learning module and haven't even
done anything much with them there with code I've had to produce myself.
I'm very pleased I recognised how to mark the bingo numbers as found. 

Overall, I'm pleased with my solution. I don't think it's that fast and it probably has a lot
of unnecessary work but it took me a fair amount of effort to finish it and I'm pleased with myself 
that I did. God knows what day 5 is going to bring, however.
'''
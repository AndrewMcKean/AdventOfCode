import numpy as np
callSheet = [79,9,13,43,53,51,40,47,56,27,0,14,33,60,61,36,72,48,83,42,10,86,41,75,16,80,15,93,95,45,68,96,84,11,85,63,18,31,35,74,71,91,39,88,55,6,21,12,58,29,69,37,44,98,89,78,17,64,59,76,54,30,65,82,28,50,32,77,66,24,1,70,92,23,8,49,38,73,94,26,22,34,97,25,87,19,57,7,2,3,46,67,90,62,20,5,52,99,81,4]
data = open('inputData_dayFour.txt', 'r').read().split('\n')

#Set up variables
board = []
boardsList = []
winner = []
winningNum = 0

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
            print(rowSum)


            rowCheck = np.where(rowSum == 0)
            colCheck = np.where(colSum == 0)

            if colCheck[0].size > 0 or rowCheck[0].size > 0 :
                #print("The number is: ", i, "\n", f"Board number {y} has won")
                winner = boardsList[y]
                winningNum = num
                found = True
                break

print(np.sum(winner) * winningNum)
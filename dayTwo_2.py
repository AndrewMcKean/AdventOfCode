data = open('inputData_dayTwo.txt', 'r').read().split('\n')

horizontalPosition = 0
depth = 0
aim = 0

for i in range(len(data)):
    currInstr = str.split(data[i])

    if currInstr[0] == 'forward':
        horizontalPosition += int(currInstr[1])
        depth += (aim * int(currInstr[1]))

    elif currInstr[0] == 'up':
        aim -= int(currInstr[1])
    
    elif currInstr[0] == 'down':
        aim += int(currInstr[1])


print(horizontalPosition * depth)
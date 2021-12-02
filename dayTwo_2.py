data = open('inputData_dayTwo.txt', 'r').read().split('\n')

horizontalPosition = 0
depth = 0
aim = 0

for i in range(len(data)):
    currInstr = str.split(data[i])
    value = int(currInstr[1])

    if currInstr[0] == 'forward':
        horizontalPosition += value
        depth += (aim * value)

    elif currInstr[0] == 'up':
        aim -= value
    
    elif currInstr[0] == 'down':
        aim += value

print(horizontalPosition * depth)

data = open('inputData_dayTwo.txt', 'r').read().split('\n')

horizontalPosition = 0
depth = 0

for i in range(len(data)):
    currInstr = str.split(data[i])

    if currInstr[0] == 'forward':
        horizontalPosition += int(currInstr[1])

    elif currInstr[0] == 'up':
        depth -= int(currInstr[1])
    else:
        depth +=  int(currInstr[1])


print(horizontalPosition * depth)


'''
Correct!

Not sure if there's a more elegant way to do it rather than if statements.
'''
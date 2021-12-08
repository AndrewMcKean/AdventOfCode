import numpy as np

data = open('inputData_dayFive.txt', 'r').read().split('\n')
grid = np.zeros((10, 10), dtype=int)

#
test = [
        '1113',
        '9777'
]

#
count = 0
for instr in test:
    currInstr = instr
    x1 = int(currInstr[0])
    y1 = int(currInstr[1])   
    
    x2 = int(currInstr[2])
    y2 = int(currInstr[3])

    #If vertical position equal
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                grid[i][x1] += 1
        elif y2 < y1: 
            for i in range(y2, y1 + 1):
                grid[i][x1] += 1

    #If horizontal position equal        
    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                grid[y1][i] += 1

        elif x2 < x1:
            for i in range(x2, x1 + 1):
                grid[y1][i] += 1

print(grid)

x, y
x2, y2

f"x{x1}y{y1}" : += 1

'''
Try numpy mesh grid
'''
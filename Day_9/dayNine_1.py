data = open('inputData_dayNine.txt', 'r').read().split('\n')
lowPoints = []
lowSum = 0

#Convert each row to a list of strings
for i in range(len(data)):
    data[i] = list(data[i])

#Convert each string in each list to an int
for i in range(len(data)):
    for x in range(len(data[i])):
        data[i][x] = int(data[i][x])

lowPoint = False
for i in range(len(data)):
    for x in range(len(data[i])):
        lowPoint = False
        curr = data[i][x]
        if i == 0:
            above = data[i+1][x]
            if x == 0:
                right = data[i][x+1]
                if curr < above and curr < right:
                    lowPoint = True

            elif x == len(data[i]) - 1:
                left = data[i][x-1]
                if curr < above and curr < left:
                    lowPoint = True
                
            else:
                right = data[i][x+1]
                left = data[i][x-1]
                if curr < above and curr < right and curr < left:
                    lowPoint = True
        
        elif i == len(data) - 1:
            below = data[i-1][x]
            if x == 0:
                right = data[i][x+1]
                if curr < below and curr < right:
                    lowPoint = True
            elif x == len(data[i]) - 1:
                left = data[i][x-1]
                if curr < below and curr < left:
                    lowPoint = True
            else:
                right = data[i][x+1]
                left = data[i][x-1]
                if curr < below and curr < right and curr < left:
                    lowPoint = True
            
        else:
            above = data[i + 1][x]
            below = data[i - 1][x]
            left = data[i][x - 1]
            if x == 0:
                right = data[i][x+1]
                if curr < above and curr < right and curr < below:
                    lowPoint = True
            elif x == len(data[i]) - 1:
                left = data[i][x-1]
                if curr < above and curr < left and curr < below:
                    lowPoint = True
            else:
                right = data[i][x+1]
                left = data[i][x-1]
                if curr < above and curr < below and curr < right and curr < left:
                    lowPoint = True
        
        if lowPoint:
            lowPoints.append((i, x))
            lowSum += curr + 1 

print(lowSum)

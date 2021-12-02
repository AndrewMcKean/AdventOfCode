data = open('inputData_dayOne.txt', 'r').read().split('\n')
total = 0

inputData = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

for x in range(len(data)):
    if x == len(data) - 3:
        break

    else:
        windowA = int(data[x]) + int(data[x+1]) + int(data[x+2])
        windowB = int(data[x+1]) + int(data[x+2]) + int(data[x+3])
        if windowB > windowA:
            total += 1

print(total)
'''   
Complete - wooo!

This one also took a few attempts. It turns out I was halting the comparisons too early
missing off the final sum.

Both of these really hammered home the importance of checking with AoC's unit tests as I go,
like I do in leetcode.
'''
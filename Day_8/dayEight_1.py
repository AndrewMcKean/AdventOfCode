data = open('inputData_dayEight.txt', 'r').read().split('\n')

'''
0 has 6 segments a/b/c/ e/f/g
1 has 2 segments c/f/                   Unique
2 has 5 segments a/c/d/e/g              
3 has 5  segments a/c/d/f/g
4 has 4 segments b/c/d/f                Unique
5 has 5 segments a/b/d/f/g
6 has 6 segments a/b/d/e/f/g
7 has 3 segments a/c/f                  Unique
8 has 7 segments a/b/c/d/e/f/g          Unique
9  has 6 segments a/b/c/d/f/g
'''
oneCount = 0
fourCount = 0
sevenCount = 0
eightCount = 0

for item in data:
    splitString = item.split()
    start = splitString.index('|') + 1
    for i in range(start, len(splitString)):
        print(splitString[i])
        if len(splitString[i]) == 2:
            oneCount += 1
        elif len(splitString[i]) == 4:
            fourCount += 1
        elif len(splitString[i]) == 3:
            fourCount += 1
        elif len(splitString[i]) == 7:
            sevenCount += 1

print(oneCount + fourCount + sevenCount + eightCount)

'''
Correct. 
Didn't take me too long. Though I'm not very excited to see part 2 if I'm honest!
'''
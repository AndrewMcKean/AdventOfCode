data = open('inputData_daySix.txt', 'r').read().split('\n')

#Clean up data
data = data[0]
data = data.replace(',', '')
fishPopulation = []
for i in data:
    fishPopulation.append(int(i))



for i in range(80):
    x = len(fishPopulation)
    for y in range(x):
        if fishPopulation[y] == 0:
            fishPopulation.append(8)
            fishPopulation[y] = 6
        else:
            fishPopulation[y] -= 1
    print(i)


print(len(fishPopulation))

'''
Correct.
Easy enough - difficulty is going to come in part 2. Tried to brute force it and it 
didn't go well lol.
'''
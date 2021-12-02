data = open('inputData_dayOne.txt', 'r').read().split('\n')
total = 0

for x in range(1, 2000):
    if x == 2000:
        break
    else:
        if int(data[x]) > int(data[x-1]):
            total += 1

print(total)

'''
This was the correct answer - woo.

I got this wrong a few times though. The key was converting the data items to ints for the
comparison.
'''
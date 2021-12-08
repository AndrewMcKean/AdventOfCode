data = open('inputData_dayThree.txt', 'r').read().split('\n')


oxygenData = data.copy()
c02Data = data.copy()

posString = ""
revString = ""

commonBit = ""


#Determine oxygen generator
count = 0
i = 0
while len(oxygenData) > 1:
    ones = 0
    zeroes = 0
    #Count the ones and zeroes
    for item in oxygenData:
        if item[i] == "1":
            ones += 1
        else:
            zeroes += 1
    
    #Declare commonBit
    if ones >= zeroes:
        commonBit = "1"
    else:
        commonBit = "0"
    
    #Remove items which don't match commonBit
    oxygenData[:] = [x for x in oxygenData if not (x[i] != commonBit)]
    
    #Increment index
    i += 1


count = 0
i = 0
while len(c02Data) > 1:
    ones = 0
    zeroes = 0
    #Count the ones and zeroes
    for item in c02Data:
        if item[i] == "1":
            ones += 1
        else:
            zeroes += 1
    
    #Declare commonBit
    if ones >= zeroes:
        commonBit = "0"
    else:
        commonBit = "1"
    
    #Remove items which don't match commonBit
    c02Data[:] = [x for x in c02Data if not (x[i] != commonBit)]
    
    #Increment index
    i += 1

oxygenRating = int(oxygenData[0],  2)
scrubberRating = int(c02Data[0], 2)

lifeSupportRating = oxygenRating * scrubberRating

print(lifeSupportRating)

'''
Done. Finally.

Spent way too long trying to get it to work with list.remove() before I realised this would 
change the indexing in place. It then essentially skipped a list item every time it removed one.
Had a google and came across list comprehension. I haven't used this very much but glad it worked
out well in the end.
'''

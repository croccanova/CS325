#Christian Roccanova
#CS 325
#HW 2 - stooge sort

import math

def stoogeSort(data, first, last):
    
    #compare first and last elements and swap if first is greater than last
    if data[first] > data[last]:
        temp = data[first]
        data[first] = data[last]
        data[last] = temp

    if last - first + 1 > 2:
        third = math.ceil((last - first) / 3) #size of a third of the array
        front = last - third #index of end of front 2/3rds
        back  = first + third #index of start of back 2/3rds
        
        #sort front 2/3rds
        stoogeSort(data, first, front)

        #sort back 2/3rds
        stoogeSort(data, back, last)

        #sort front 2/3rds again
        stoogeSort(data, first, front)
        
  

#main
# get data from file
dataFile = open("data.txt", "r")
lines = dataFile.readlines()
dataFile.close()
lineCount = len(lines)

#separate lines
for i in range(0, lineCount):
    sortData = []

    #separate line elements
    currLine = lines[i].split()    
    dataLength = int(currLine[0])
    
    #append line elements to data array
    for j in range(1, dataLength + 1):
        sortData.append(int(currLine[j]))

    #call stooge sort  
    n = len(sortData)
    stoogeSort(sortData, 0, n - 1)
   
    #write data to output file
    stoogeOut = open("stooge.out", "a")
    for k in range (0, dataLength):
        stoogeOut.write(str(sortData[k]))
        stoogeOut.write(" ")
    stoogeOut.write("\n")
    stoogeOut.close()

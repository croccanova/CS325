# Christian Roccanova
# CS 325 Fall 2018
# HW 1 - insertion sort

#insertion sort function
def insertSort(data):

    #loop through each element
    for i in range(0, len(data)):
        curr = data[i]
        j = i - 1

        #compare current element to those before it and replace them if it is smaller
        while j >= 0 and curr < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = curr

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

    #call insertion sort
    insertSort(sortData)

    #write data to output file
    insertOut = open("insert.out", "a")
    for k in range (0, dataLength):
        insertOut.write(str(sortData[k]))
        insertOut.write(" ")
    insertOut.write("\n")
    insertOut.close()




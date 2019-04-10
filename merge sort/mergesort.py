# Christian Roccanova
# CS 325 Fall 2018
# Mergesort - sorts data from file by splitting it into subarrays and recombining them

#merges left and right sub arrays
def merge(data, left, right):
     
       #array indices
       i = 0
       j = 0
       k = 0

       sizeL = len(left)
       sizeR = len(right)

       #merge sub arrays 
       while i < sizeL and j < sizeR:
           if left[i] < right[j]:
               data[k] = left[i]
               i += 1
           else:
               data[k] = right[j]
               j += 1
           k += 1

       #copy remaining elements of left sub array
       while i < sizeL:
           data[k] = left[i]
           i += 1
           k += 1
       #copy remaining elements of right sub array
       while j < sizeR:
           data[k] = right[j]
           j += 1
           k += 1

#recursively sorts array by splitting it into sub arrays, sorting those and then re-combining them
def mergeSort(data):

   dataSize = len(data)

   #if only one element, its already sorted
   if dataSize > 1:
       
       #split passed data into left and right halves
       mid = int(dataSize/2) #get position of middle and force it to be an int
       left = data[:mid] #array of all elements from position 0 to mid
       right = data[mid:] #array of all elements from mid to last element


       #recursive calls on each split
       mergeSort(left)
       mergeSort(right)

       #re-combines sub arrays
       merge(data, left, right)

# Main 
#get data from file
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
    for j in range(1, dataLength+1):
        sortData.append(int(currLine[j]))

    #call insertion sort
    mergeSort(sortData)

    #write data to output file
    mergeOut = open("merge.out", "a")
    for k in range (0, dataLength):
        mergeOut.write(str(sortData[k]))
        mergeOut.write(" ")
    mergeOut.write("\n")
    mergeOut.close()


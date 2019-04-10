# Christian Roccanova
# CS 325 Fall 2018
# mergeTime - sorts randomly generated arrays of numbers and collects running times of the sorting

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

#main
import random
import time
arrSize = [5000, 7500, 10000, 12500, 15000, 17500, 20000]

#generate data for each of 7 arrays
for i in range(0, 7):
    sortData = []
    totalTime = 0
    #generate random data
    for j in range(0, arrSize[i]):
        element = random.randint(0, 10000)
        sortData.append(element)

    #run each 10 times
    for k in range(0, 10):        
        start = time.time()
        mergeSort(sortData)
        end = time.time()
        elapsed = end - start   
        totalTime += elapsed

    #print the average of the 10 runs
    print("Array size n = ", arrSize[i])
    print("Average run time (10 runs) = ", totalTime/10)
    print("\n")
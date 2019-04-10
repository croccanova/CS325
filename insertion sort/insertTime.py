# Christian Roccanova
# CS 325 Fall 2018
# HW 1 - insertion sort - sorts randomly generated data by comparing an element to those before it and collects running times of the sorting

#insertion sort function
def insertSort(data):

    #loop through each element
    for i in range(1, len(data)):
        curr = data[i]
        j = i - 1

        #compare current element to those before it and replace them if it is smaller
        while j >= 0 and curr < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = curr

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
        insertSort(sortData)
        end = time.time()
        elapsed = end - start     
        totalTime += elapsed

    
    #print the average of the 10 runs
    print("Array size n = ", arrSize[i])
    print("Average run time (10 runs) = ", totalTime/10)
    print("\n")





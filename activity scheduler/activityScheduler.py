# Christian Roccanova
# CS325 - fall 2018
# last-to-start - reads a set of activities with start and end times from a file.  These are then sorted via merge sort and a greedy algorithm selects the gretest possible number of activities based on latest start time.


#activity class definition
class activity:
        def __init__(self, number, start, finish):
            self.num = number
            self.start = start
            self.fin = finish

#mergeSort code taken from HW 1
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
           if left[i].start > right[j].start:   #flipped < to > to make descending order based on start time
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


#greedy algorithm to select the gretest possible number of activities based on latest start time
def selection(activities):

    #sort in descending order by start time
    mergeSort(activities)

    #initialize new schedule
    schedule = []
    key = 0

    #first activity is always chosen
    schedule.append(activities[0])
    selectCount = 1

    #loop through remaining activities, adding them to the schedule if their end time is at or before the start time of the most recent addition
    for i in range(1, len(activities)):
        if activities[key].start >= activities[i].fin:
            schedule.append(activities[i])
            key = i
            selectCount += 1

    #flip schedule so that activities are in order from start to finish
    schedule.reverse()

    #print data to terminal
    print("Number of activities selected = ", selectCount )
    print("Activities selected:", end='')
    for x in range(0, selectCount):        
        print(" ", schedule[x].num, end='')

    print("\n")


# Main
# get data from file
dataFile = open("act.txt", "r")
lines = dataFile.readlines()
dataFile.close()
lineCount = len(lines)


j = 0
setCount = 1
while j < lineCount:

    activities = []    
    actCount = int(lines[j])

    #build activity list
    for k in range(j + 1, j + actCount + 1):
        currLine = lines[k].split()
        actNum = int(currLine[0])
        actStart = int(currLine[1])
        actFin = int(currLine[2])

        activities.append(activity(actNum, actStart, actFin))

    j = j + actCount + 1

    print("Set ", setCount)

    #call selection function
    selection(activities)
    setCount += 1


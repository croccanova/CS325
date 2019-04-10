# Christian Roccanova
# CS 325  Fall 2018
#shopping - dynamic programming implementation of a 0-1 knapsack that determines the best possible total value of items for a given weight as well as which items those are for a given set of people and carrying capacities

#items class definition
class items:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

        
#determines items to be chosen for maximum benefit based on value and weight
def shop(merch, members, capacity):

    n = len(merch)
    total = 0
    memItems = [] #will be a 2D list holding the items chosen by each member

    #loop once for each family member
    for m in range(0, members):
        best = 0
        curItems = []
        W = capacity[m]
        K = [[0 for x in range(W+1)] for x in range(n+1)] 
        
  
        #Build table K 
        for i in range(n+1): 
            for w in range(W+1): 
                if i==0 or w==0: 
                    K[i][w] = 0

                #item usable    
                elif merch[i-1].weight <= w: 
                    K[i][w] = max(merch[i-1].price + K[i-1][w-merch[i-1].weight],  K[i-1][w])
                    
                #item not used
                else: 
                    K[i][w] = K[i-1][w] 
        
        #final cell in table contains best price
        best = K[n][W]
        total = total + best        
        cartWt = W
        
        #determine items for each member
        for i in range(n,0,-1):
            if best <= 0:
                break
            
            if best == K[i-1][cartWt]:
                continue

            #item is in the cart
            else:
                #append to array of current items
                curItems.append(i)
                
                #deduct item's price and weight from totals
                best = best - merch[i-1].price
                cartWt = cartWt - merch[i-1].weight

        #append this member's list of items into the family's list
        memItems.append(curItems[::-1])
        
    #write total price of cart
    shopOut.write("Total Price " + str(total) + "\n")
    shopOut.write("Member Items\n")

    #write member items
    for i in range(0, members):
        shopOut.write(str(i+1) + ": ")
        for j in range(0, len(memItems[i])):
            shopOut.write(str(memItems[i][j]) + " ")
        shopOut.write("\n")
    
    



#main
# get data from file
dataFile = open("shopping.txt", "r")
lines = dataFile.readlines()
dataFile.close()
shopOut = open("shopping.out", "a")
lineCount = len(lines)


j = 1
testCount = 1
while j < lineCount:

    merchandise = []
    carryCap = []
    itemCount = int(lines[j])

    #build merchandise list
    for k in range(j + 1, j + itemCount + 1):
        currLine = lines[k].split()
        p = int(currLine[0])
        w = int(currLine[1])
        merchandise.append(items(p, w))

    j = j + itemCount + 1
    famCount = int(lines[j])

    #build carry capacity list
    for l in range(j+1, j + famCount+1):
         carryCap.append(int(lines[l]))
    j = j + famCount + 1

    shopOut.write("Test Case "  + str(testCount) + "\n")

    testCount += 1

    #call shopping function
    shop(merchandise, famCount, carryCap)

shopOut.close()
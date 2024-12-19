#Distribution of two dice program

#-------------------------
#Import libraries
#-------------------------
import random


#-------------------------
#Subprograms
#-------------------------
def distribution(rolls):
    #Initialise dice and results
    dice = [0, 0]
    result = [0 for roll in range(13)]
    random.seed()
    
    #Simulate dice rolls
    for counter in range(rolls):
        dice[0] = random.randint(1, 6)
        dice[1] = random.randint(1, 6)
        sum = dice[0] + dice[1]
        result[sum] = result[sum] + 1
        

    #Output result
    for roll in range(2, len(result)):
        print(roll, ":", result[roll])
        

#-------------------------
#Main program
#-------------------------
rolls = int(input("How many rolls to simulate? :"))
distribution(rolls)
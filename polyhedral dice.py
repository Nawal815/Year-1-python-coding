#Polyhedral dice program

#-----------------------
#Import libraries
#-----------------------
import random


#-----------------------
#Subprograms
#-----------------------
def roll_dice():
    faces = int(dice)
    result = random. randint(1, faces)
    return result

#-----------------------
#Main Program
#-----------------------
random.seed()
dice = input("Roll a D")
number = roll_dice()
if (number == 8) or (number == 11):
    print ("You rolled an", number)
else:
    print("You rolled a", number)



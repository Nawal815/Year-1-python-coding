#Dungeon master program

#----------------------
#Import libraries
#----------------------
import random

#----------------------
#Subprograms
#----------------------
#Function to return if a skill check is passed in DnD5e
def check_skill(skill, modifier, dm_valie):
    #Check is always passed if skill is 5 or more than needed
    if skill + modifier >= dm_value + 5:
        return "Automatic pass"
    else:
        roll = random.randint(1, 20)
        print("You rolled a", roll)
        #A roll of 1 is a critical fial ragardless of skill (house rule)
        if roll == 1:
            return "Critical fail"
        #A roll of 20 is a critical succes regardless of skill (house rule)
        elif roll == 20:
            return "Critical success"
        else:
            #Check is passes if skill + dice + modifier is greater than or equal to the DM value
            if skill + modifier + roll >= dm_value:
                return "Check passed"
            else:
                return "Check failed"




#----------------------
#Main Program
#----------------------
random.seed()
skill = int(input("Enter the skill value:"))
modifier = int(input("Enter any modifier:"))
dm_value = int(input("Enter the number to pass:"))
result = check_skill(skill, modifier, dm_value)
print(result)

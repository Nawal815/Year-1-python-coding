#Random name generator program

#---------------------
#import libraries
#---------------------
import random



#---------------------
#Subprograms
#---------------------
#Functions to return a random name
def generate_name():
    forename_list = ["Muhammad", "Noah", "Jack", "Lily", "Sophia", "Olivia"]
    surname_list = ["Wang", "Smith", "Devi", "Jones", "Kim", "Rodriguez"]
    random.seed()
    forename = forename_list[random.randint(0,5)]
    surname = surname_list[random.randint(0,5)]
    return forename + "" + surname


#---------------------
#Main program
#---------------------
print("Press Enter to generate a new name, or input 'end' to quit.")
wait = ""
while wait != "end":
    wait = input()
    if wait != "end":
        print(generate_name())

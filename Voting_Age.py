#A program to check if the user is old enough to vote in the UK

#-------------------------
#Subprograms
#-------------------------
def check_age(age):
    if age >=18:
        print("You are old enough to vote!")
    else:
        print("You are too young to vote!")
        
#-------------------------
#Main Program
#-------------------------
user_age = int(input("how old are you?"))
check_age(user_age)

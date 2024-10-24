#Capital city program

#----------------------
#Subprograms
#----------------------
def check_answer(country, city):
    if country == "England" and city == "London":
        return True
    if country == "France" and city == "Paris":
        return True
    else:
        return False
    
def capital_cities():
    correct = False
    while not correct:
        city = input("What is the capital city of England?:")
        correct = check_answer("England", city)
        
    correct = False 
    while not correct:
        city = input("What is the capital city of France?:")
        correct = check_answer("France", city)


#----------------------
#Main Program
#----------------------
capital_cities()
print("The quiz is complete.")
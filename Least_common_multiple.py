#Least common multiple program

#------------------------
#Subprograms
#------------------------
#Function to use trial and error to calculate LCM
def lcm(number1, number2):
    #Optimisation to start the counter at the highest number
    if number1> number2:
        counter = number1
    else:
        counter = number2
    #Find the LCM by checking every number until found
    while counter % number1 != 0 or counter % number2 != 0:
        counter = counter + 1
    return counter

#------------------------
#Main program
#------------------------
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
result = lcm(number1, number2)
print("The LCM of {0} and {1} is {2}.".format(number1, number2, result))
#carpet cost program

#-----------------------------
#subprograms
#-----------------------------
def carpet_cost(width, length, price):
    carpet = width * length * price
    grippers = width + length 
    fitting = 50
    return carpet + grippers + fitting

#-------------------------------
#Main program
#-------------------------------
width = int(input("Enter the width of the room to the nearest meter:"))
length = int(input("Enter the length of the room to the nearest meter:"))
price = float(input("Enter the price of the carpet per m²:"))
print("The total coast is: £", carpet_cost(width, length, price))



#valid month program

#--------------------------------
#Subprograms
#--------------------------------
def validate_month(month):
    #Must be between 1 and 12
    if (month >= 1) and (month <=12) :
        return Trye
    else:
        return False

#--------------------------------
#Main program
#--------------------------------
valid_month = False
while not valid_month:
    month = int(input("Enter a month 1-12:"))
    valid_month = validate_month(month)
print("Thank you. Input accepted.")
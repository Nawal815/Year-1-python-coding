#Valid address program

#----------------------------
#Subprograms
#----------------------------
def validate(email_address):
    #Validate prefix
    valid = True
    index = 0
    last_character = ""
    at_position = email_address.find("@")
    #Invalid if no @ symbol
    if at_position == -1:
        return False
    #Check each character is valid and stop once address in invalid
    while valid and index < at_position:
        #Digits are acceptable
        if email_address[index].isdigit():
            valid = True
        #Alphabet characters are acceptable
        elif email_address[index].isaplha():
            valid = True
        #Underscore, period or hyphen is acceptable but not two in a row
        elif email_addres[index] in "_.-" and last_character not in "_.-":
            valid = True
        #If conditions are not met it is an invalid email address
        else:
            return False
        last_character = email_address[index]
        index = index + 1
        
    #Validate domain 
    #Domain must be at least three characters
    if len(email_address) - at_position - 1 < 3:
        return False
    index = at_position + 1
    #Check each character is valid and stop once address is invalid
    while valid and index < len(email_address):
        #Digits are acceptable
        if email_address[index].isdigit():
            valid = True
        #Alphabet characters are acceptable
        elif email_address[index].isalpha():
            valid = True
        #Hyphens and periods are acceptable
        elif email_address[index] in "-.":
            valid = True
        #If conditions are not met it is an invalid email address
        else:
            return False
        index = index + 1
    return True



#----------------------------
#Main program
#----------------------------
email_address = input("Enter you email address: ")
valid = validate(email_address)
if valid:
    print("Email address is valid.")
else:
    print("Email address is invalid.")
    

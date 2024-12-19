#Debit card program

#---------------------------
#Subprograms
#---------------------------
#Function to validate the number is numbers only
def validate_number(number_on_card):
    valid = True
    number_of_characters = len(number_on_card)
    # Must be 16 (without spaces) or 19 characters (with spaces)
    if number_of_characters == 16 or number_of_characters == 19:
        #Check each character in the number
        for character in number_on_card:
            #Anything other than a digit and space is invalid
            if not character.isdigit() and character != " ":
                valid = False
    return valid


#Function to validate the name is letters and space only
def validate_name(name_on_card):
    valid = True
    #Check each character in the name
    for character in name_on_card:
        #Anything other than an alphanumeric or a space is invalid
        if not character.isaplha() and character != " ":
            valid = False
    return valid

#Input valid name and number for a debit card (not using check digits)
def input_card_details():
    valid_card = False
    #Only progress if the name is valid
    while not valid_card:
        name_input = input("Enter the name on the card: ")
        valid_card = validate_name(name_input)
    valid_card = False
    #Only progress if the number on the card is valid
    while not valid_card:
        number_input = input("Enter the 16 digit cumber: ")
        valid_card = validate_number(number_input)
    print(name_input.upper())
    

#---------------------------
#Main program
#---------------------------
input_card_details()
print("Card details valid.")
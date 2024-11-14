
#PIN Program

#-------------------------
#Subprograms
#-------------------------
#Function to return if pin entered is valid or invalid
def get_pin(pin):
    attempts = 0
    valid_input = False
    #validation
    while not valid_input and attempts < 3:
        number = input("Enter PIN: ")
        #Check if PIN matches
        if number == pin:
            valid_input = True
        else:
            attempts = attempts + 1
    #Return whethern PIN is accepted or not
    if attempts < 3:
        return True
    else:
        return False
#-------------------------
#Main program
#-------------------------
security_passed = get_pin("7528")
if security_passed:
    print("Security check passed.")
else:
    print("Locked out.")

    
#Measurements program

#--------------------------
#Subprograms
#--------------------------
#Subroutine to concvert feet to inches
def feet_to_inches(feet):
    return feet * 12
#Subroutine to convert inches to feet
def inches_to_feet(inches):
    return inches / 12
#Subroutine to offer the convesion choice to user
def menu():
    menu_choice = "0"
    #Iterate until a valid option is chosen
    while menu_choice < "1" or menu_choice > "3":
        print("1. Feet to inches")
        print("2. Inches to feet")
        print("3. Quit")
        menu_choice = input("Enter choice: ")
    return menu_choice
#Subroutine to call conversion routines from user's choice
def converter():
    option = menu()
    match option:
        #Feet to inches
        case "1":
            feet = float(input("Enter the number of feet:"))
            inches = feet_to_inches(feet)
            print(feet, "feet is", inches, "inches")
        #Inches to feet
        case "2":
            inches = float(input("Enter the number of inches: "))
            feet = inches_to_feet(inches)
            print(inches, "inches is", feet, "feet.")
        #Quit
        case "3":
            print("Goodbye")
#--------------------------
#Main program
#--------------------------
converter()
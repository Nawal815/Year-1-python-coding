#Ride height program

#---------------------------
#Subprograms
#---------------------------
def valid_height(height):
    if height > 104:
        return True
    else:
        return False
    
#---------------------------
#Main program
#---------------------------
height = float(input("Enter the height of the person in cm:"))
if valid_height(height):
    print("Height OK.")
else:
    print("Sorry, you are too small.")

#Extension
#Ride height program
#----------------------------
#Subporgrams
#----------------------------
#Check if the child is under 91cm
def valid_height(height):
    if height <91:
        return True
    else:
        return False


#-----------------------------
#Main program
#-----------------------------
height = float(input("Enter the height of the person in cm: "))
if valid_height(height):
    print("Height OK.")
else:
    print("Sorry, you are too tall. ")
#A program to check if a user's password matches the default password

#----------------------
#Constants
#----------------------
PASSWORD = "LetMeIn"

#----------------------
#Subprograms
#----------------------
def check_password():
    password = input("Enter password: ")
    if password == PASSWORD:
        print("Login successful")
    else:
        print("Incorrect password")
    while PASSWORD != password:
        check_password()
        break


#----------------------
#Main Program
#----------------------
print("Welcome to password checker")
check_password()

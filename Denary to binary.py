#Denary to binary program

#------------------------
#Subprograms
#------------------------
def den_to_bin(number):
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    return binary


#------------------------
#Main programs
#------------------------
number = int(input("Enter the denary number to convert: "))
print("Binary:", den_to_bin(number))
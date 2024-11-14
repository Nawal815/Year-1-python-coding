#Cashpoint program

#--------------------------
#Subprograms
#--------------------------
def dispense(amount):
    print("W", + amount)
    #£20 notes
    iamount = int(amount)
    while iamount >=20:
        print("D20")
        iamount = iamount - 20
    #£10 notes
    while iamount >=10:
        print("D10")
        iamount = iamount - 10
    #£5 notes
    while iamount >=5:
        print("D5")
        iamount = iamount - 5
    
#--------------------------
#Main program
#--------------------------
amount = input("Enter the amount to withdraw: £")
dispense(amount)
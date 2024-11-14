#Compound interest program

#----------------------------
#Subprogram
#----------------------------
#calculate compound interest
def compound(balance, interest_rate, target_balance):
    year = 1
    interest_rate = interest_rate / 100
    #calculate interest until the balance matches the target balance
    while balance < target_balance:
        interest = balance * interest_rate
        balance = int(balance + interest)
        print("Year", year, ":balance £", balance)
        year = year + 1

#----------------------------
#Main program
#----------------------------
balance = int(input("Enter the balance to the nearest pound: £"))
interest_rate = float(input("Enter the % interest rate:"))
target_balance = int(input("Enter the target balance to the nearest pound: £"))
compound(balance, interest_rate, target_balance)
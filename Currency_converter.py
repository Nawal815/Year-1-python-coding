#Currency converter program

#--------------------------
#Subprograms
#--------------------------
def exchange(gbp, currency):
    money = 0
    #US Dollars.
    if currency == "USD":
        money = gbp * 1.3
    #European Euros.
    elif currency == "Euro":
        money = gbp * 1.11
    #Chinese Yuan.
    elif currency == "Yuan":
        money = gbp * 8.92
    #Japanese Yen.
    elif currency == "Yen":
        money = gbp * 138.44
    return money   

#--------------------------
#Main Program
#--------------------------
gbp = float(input("Enter the numberof Great British pounds:"))
currency = input("Enter the currency (USD, Euro, Yuan, Yen):")    
money = exchange(gbp, currency)
print(gbp, "GBP =", money, currency)

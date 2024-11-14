#Save the change program

#-----------------------
#Subprograms
#-----------------------
def nearest_pound(amount):
    if int(amount) != amount:
        nearest = int(amount) + 1
    else:
        nearest = int(amount)
    return nearest
#Return the difference between the number and the rounded number
def save_the_change(amount):
    if int(amount) != amount:
        savings = nearest_pound(amount) - amount
    else:
        savings = 0
    return savings

#-----------------------
#Main Program
#-----------------------
purchase_price = flaot(input("Enter the purchase price: £"))
debit = nearest_pound(purchase_price)
savings = save_the_change(purchse_price)
print("Debit - £{0:.2f}".format(debit))
print("Credit to savings - £{0:.2f}".format(savings))


#--------------------------------
#subprograms
#--------------------------------

def c_to_f(centigrade):
    return(centigrade * 1.8) + 32

#--------------------------------
#Main program
#--------------------------------

centigrade =int(input("Enter the temperature in centigrade:"))
fahrenheit =c_to_f(centigrade)
print(centigrade, "degrees Centrigrade is", fahrenheit, "degres Fahrenheit.")


#Times tables program

#---------------------------
#Subprograms
#---------------------------
#Procedure to output the x times table.
def times_table(x):
    #ouput table 1-12
    for counter in range (1, 13):
        print(counter, "x", "x", "=", counter * x)
        

#---------------------------
#Main program
#---------------------------
table = int(input("Which table do you want to output? 1-12:"))
times_table(table)
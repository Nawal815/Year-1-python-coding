#Fizz buzz program

#--------------------------
#Subprograms
#--------------------------
#Subroutines to output Fizz for multiples of 3 and Buzz for multiples of 5
def fizz_buzz(x):
    #Loop from 1 to x
    for counter in range(1, x + 1):
        #Multiple of 3 and 5
        if counter % 3 == 0 and counter % 5 == 0:
            print("Fizz Buzz")
        #Multiple of 3 only
        elif counter % 3 == 0:
            print("Fizz")
        #Multiple of 5 only
        elif counter % 5 == 0:
            print("Buzz")
        #Not multiple of 3 or 5
        else:
            print(counter)
            
#--------------------------
#Main program
#--------------------------
maximum = int(input("What number should the count be up to? :"))
fizz_buzz(maximum)
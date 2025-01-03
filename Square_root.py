#Square root program

#--------------------------
#Subprograms
#--------------------------
def sqroot(x):
    root = x
    last_root = 0
    while root != last_root:
        last_root = root
        root = 0.5 * (root + (x / root))
        return root

#--------------------------
#Main program
#--------------------------
num = float(input("Enter a number:"))
print("The square root of", num, "is", sqroot(num))
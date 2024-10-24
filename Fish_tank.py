#Fish tank volume problem

#------------------------
#subprograms
#------------------------
def volume(length, width, height):
    return(length * width * height) / 1000
def litres_to_gallons(litres):
    return litres / 4.564



#------------------------
#Main program
#------------------------
length = int(input("Enter the length of the tank in cm:"))
width = int(input("Enter the height of the tank in cm:"))
height = int (input("Enter the height of the tank in cm:"))
litres = volume(length, width, height)
gallons = litres_to_gallons(litres)
print("A", length, "x", width, "x", height, "cm tank is", litres, "litres and", gallons, "imperial gallons.")

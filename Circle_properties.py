#circle properties program

#-------------------------
#subprograms
#-------------------------
#calculate the area of a circle
def circle_area(diameter):
    radius = diameter / 2
    area = 3.14 * (radius * radius)
    return area
#calculate the circumference of a circle
def circle_circumference(diameter):
    circumference = 3.14 * diameter
    return circumference
#-------------------------
#Main program
#-------------------------
diameter = float(input("Enter the diameter of the circle:"))
area = circle_area(diameter)
circumference = circle_circumference(diameter)
print("Area:", area)
print("Circumference:", circumference)

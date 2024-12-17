#Search for life program

#-------------------------
#Import libraries
#-------------------------
import random


#-------------------------
#Subprograms
#-------------------------
#Function to return what probes find
def probe(planet):
    #Ensure the planet always returns the same result
    random.seed(planet)

    climate = ["hot", "frozen", "barren", "temperature"]
    weather = random.randint(0,3)

    #Only temperature planets can host life
    if weather ==3:
        creature = ["lizards", "humanoids","insects"]
        colour = ["red", "green", "blue"]
        characteristics = ["shy", "angry", "docile"]
        lifeform = random.randint(0,2)
        specimen = random.randint(0,2)
        behaviour = random.randint(0,2)
        report= ""
        report = colour [specimen]
        report = report + "," + characteristic[behaviour]
        report = report + "" + creature[lifeform]
        report = report + "on a" + climate [weather] + "planet."
    else:
        report = "a" + climate[weather] + "planet with no signs of life."
    return report

#---------------------------
#Main program
#---------------------------
planet = int(input("Enter the catalogue number of a planet: "))
report = probe(planet)
print("Probes report", report)
    


    

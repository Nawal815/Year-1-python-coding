#Airline ticket program

#-------------------------
#Subprograms
#-------------------------
#Function to return truncated airport names
def airports(departure, arrival):
    #Extract first four characters
    departure = departure[0:4]
    arrival = arrival[0:4]
    #Insert dash
    output = departure + "-" + arrival
    #Convert to uppercase
    output = output.upper()
    return output


#------------------------
#Main program
#------------------------
print(airports("Gatwick", "Amsterdam"))


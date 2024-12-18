#London Underground program

#----------------------
#Subprograms
#----------------------
#Function to input a valid station name
def get_station():
    valid_station = False
    #Validation
    while not valid_station:
        station_input = input("Enter station: ")
        #Lookup check
        if station_input in stations:
            valid_station = True
        else:
            print("Invalid station.")
    return station_input



#Function to calculate the number of stops between two stations
def calculate_stops(ticket):
    start_at = stations.index(ticket[0])
    stop_at = stations.index(ticket[1])
    stops = abs(start_at - stop_at)
    return stops


#----------------------
#Main program
#----------------------
#Victoria line
stations = ["Brixton", "Stockwell", "Vauxhall", "Pimlico", "Victoria", "Green Park", "Oxford Circus", "Warren Street", "Euston", "King's Cross", "Highbury & Islington", "Finsbury Park", "Seven Sisters", "Tottenham Hale", "Blackhorse Road", "Walthanstow Central"]
ticket = [0, 0] #The two stations on the ticket
ticket[0] = get_station()
ticket[1] = get_station()
stops = calculate_stops(ticket)
if stops == 1:
    print(ticket[0], "to", ticket[1], "is", stops, "stop.")
else:
    print(ticket[0], "to", ticekt[1], "is", stops, "stops.")

#Rainfall program

#--------------------------
#Subprograms
#--------------------------
#Function to analyse a rainfall data set
def analyse1(data):
    #Initialise variables
    count = 0 #Count of days with no rainfall
    average = 0 #The average rainfall recorded in the period
    highest = 0 #The highest rainfall recorded in the period
    #Consider each item of data in the data set
    for value in data:
        #If the value is zero then there was no rainfall
        if value == 0:
            count = count + 1
        #Keep a running total for the average
        average = average + value
        #If the value is greater than the highest so far, record this as the highest instead
        if value > highest:
            highest = value
    #Calculate the average
    average = average / len(data) 
    return [count, average, highest]


#Function to analyse a rainfall data set
def analyse2(data):
    #Initialise variables
    count = 0 #Count of days with no rainfall
    average = 0 #The average rainfall recorded in the period
    highest = 0 #The highest rainfall recorded in the period
    #Consider each item of data in the data set
    for index in range(len(data)):
        #If the value is zero then there was no rainfall
        if data[index] == 0:
            count = count + 1
        #Keep a running total for the average
        average = average + data[index]
        #if the value is greater than the highest so far, recoord this as the highest instead
        if data[index] > highest:
            highest = data[index]
    #Calculate the average
    average = average / len(data)
    return [count, average, highest]


#--------------------------
#Main program
#--------------------------
daily_rainfall_mm = [0.1, 0.0, 0.2, 0.4, 0.1, 0.0, 0.0,
                     0.0, 0.3, 0.3, 0.2, 0.0, 0.0, 0.1]

analysis = analyse1(daily_rainfall_mm)
print("Days with no rain:", analysis[0])
print("Average rainfall: {0:.2f}".format(analysis[1]))
print("Highest rainfall:", analysis[2])

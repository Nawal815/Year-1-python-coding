#seconds in a day program

#------------------------
#Subprograms
#------------------------
def seconds_to_hours(seconds):
    return seconds // 3600
# Function to return the number of minutes from seconds
def seconds_to_minutes(seconds):
    return (seconds // 60) % 60
# Function to reduce the number of seconds after miunuts calculated
def seconds_remaining(seconds):
    return seconds % 60
#-------------------------
#Main program
#-------------------------
seconds = int(input("Enter the number of seconds:"))
hours = seconds_to_hours(seconds)     
mintes = seconds_to_minutes(seconds)
seconds = seconds_remaining(seconds)
print(hours, "hours", minutes, "minutes", seconds, "seconds")    

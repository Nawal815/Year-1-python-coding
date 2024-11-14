#A program to:

#---------------------
#Subprograms
#---------------------
def main():
    age_in_years = int(input("Please enter your age in years:"))

    

    # calculating age in seconds
    def calculate_seconds(years):
        return years * 365 * 24 * 60 * 60
    #calculating age in minutes
    def calculate_minutes(years):
        return years * 365 * 24 * 60
    #Calculating age in hours
    def calculate_hours(years):
        return years * 365 * 24
    #Calculating age in days
    def calculate_days(years):
        return years * 365
    #calculating age in weeks
    def calculate_weeks(years):
        return years * 365 // 7
    #Calculating age in months
    def calculate_months(years):
        return years * 12
    
    seconds = calculate_seconds(age_in_years)
    minutes = calculate_minutes(age_in_years)
    hours = calculate_hours(age_in_years)
    days = calculate_days(age_in_years)
    weeks = calculate_weeks(age_in_years)
    months = calculate_months(age_in_years)

    #dispaying results
    print("You are", seconds, "seconds old")
    print("You are", minutes, "minutes old")
    print("You are", hours, "hours old")
    print("You are", days, "days old")
    print("You are", weeks, "weeks old")
    print("You are", months, "months old")
    


#---------------------
#Main program
#---------------------
main()

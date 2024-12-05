#Leap year program

#------------------------
#Subprograms
#------------------------
def is_leap_year(year):
    leap_year = False
    #If the year is divisible by 4 then it is a leap year...
    if year % 4 == 0:
        leap_year = True
    #...however, if it is also divisible by 100 it is not a leap year
        if year % 100 == 0:
            #...but if it is divisible by 400 then it is a leap year
            if year % 400 == 0:
                leap_year = True
                #All other years are not leap years
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False
        return leap_year
#------------------------
#Main program
#------------------------
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "year is not a leap year.")

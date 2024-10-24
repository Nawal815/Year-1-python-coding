#Seasons program

#----------------------------
#Subprograms
#----------------------------
def seasons(month):
    match month:
        #Winter months.
        case "December" | "12" | "January" | "1" | "February" | "2":
            return "Winter"
        #Spring months.
        case "March" | "3" | "April" | "4" | "May" | "5" :
            return "Spring"
        #Summer months
        case "June" | "6" | "July" | "7" | "August" | "8":
            return "Summer"
        #Autumn months
        case "September" | "9" | "October" | "10" | "November" | "11":
            return "Autumn"
        #Not a valid month
        case _:
            return "Error"
    
    

#----------------------------
#Main Program
#----------------------------
month = input("Enter the month:")
season = seasons(month)
print("Month", month, "is in the", season)

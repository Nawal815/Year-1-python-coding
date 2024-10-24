
#Exam Grade program

#-------------------------
#subprograms
#-------------------------
def grade(mark):
    # Eighty or more is a grade nine
    if mark >=80:
        return "9"
    #Sixty seven or more is a grade eight
    elif mark >=67:
        return "8"
    #Fifty four or more is a grade seven
    elif mark >=54:
        return "7"
    #Forty one or more is a grade six
    elif mark >=41:
        return "6"
    # Thirty one or more is a grade five
    elif mark >=31:
        return "5"
    #Twenty two or more is a grade four
    elif mark >=22:
        return "4"
    #Thirteen or more is a grade three
    elif mark >=13:
        return "3"
    #Four or more is a grade two
    elif mark >=4:
        return "2"
    #Two or more is a grade one
    elif mark >=2:
        return "1"
    #Less than two is unclassified
    else:
        return "U"
        
    def marks_needed(mark):
        #Top grade already achieved
        if mark >=80:
            return 0
        #Next grade is eighty marks
        elif mark >=67:
            return 80 - mark
        #Next grade is sixty seven marks.
        elif mark >=54:
            return 67-mark
        #Next grade is fifty four marks
        elif mark >=41:
            return 54 - mark
        #Next grade is forty one marks
        elif mark >=31:
            return 41 - mark
        #Next grade is thirty one marks
        elif mark >=22:
            return 31 - mark
        #Next grade is thirteen marks
        elif mark >=4:
            return 13 - mark
        #Next grade is four marks
        elif mark >=2:
            return 4 - mark
        #First grade is two marks
        else: 
            return 2 - mark
            

#-------------------------
#Main Program
#-------------------------
my_mark = int(input("Enter the mark 0-100:"))
my_grade = grade(my_mark)
next_grade = marks_needed(my_mark)
print("A mark of", my_mark, "is grade", my_grade)
print("You needed", next_grade, "more marks to achieve the next grade.")

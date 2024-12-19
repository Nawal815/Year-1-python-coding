#Teahcer code program

#--------------------------
#Subprograms
#--------------------------
def tcode(teacher, number):
    #Remove apostrophe
    teacher = teacher.replace("'", "")
    letters = ["", ""]
    #Extract first letter
    letters[0] = teacher[0]
    space = teacher.find(" ")
    #Extract number of letters after the space
    letters[1] = teacher[space + 1: space + number]
    #Join letters together into a single string
    teacher_code = "".join(letters)
    #Convert to upper case
    teacher_code = teacher_code.upper()
    return teacher_code


#--------------------------
#Main program
#--------------------------
teacher = input("Enter the name of the teacher: ")
number = int(input("How many letters: "))
teacher_code = tcode(teacher, number)
print(teacher_code)



#Notebook program

#-------------------------
#Subprograms
#-------------------------
#Function to return valid input
def get_note_number():
    valid_input = False
    #Validation
    while not valid_input:
        note_number = int(input("Note number: "))
        #Note must be between 0 and 9.
        if note_number >= 0 and note_number < 10:
            valid_input = True
        else:
            print("Invalid input. Enter 0-9.")
    return note_number

#Procedure to write a new note
def add_note():
    index = get_note_number()
    note = input("Enter the note: ")
    notebook[index] = note
   
#Procedure to clear a note
def delete_note():
    index = get_note_number()
    notebook[index] = ""
    
#Clear notebook
def clear_notes():
    choice = ""
    #Validation
    while choice not in ["y", "n"]:
        choice = input("Are you suer you want to delete all notes? y/n :")
    #if yes selected, clear the notebook
    if choice == "y":
        for index in range(len(notebook)):
            notebook[index] = ""
            
#Procedure to swap two notes
def move_note():
    first_note = get_note_number()
    print("To be moved to...")
    second_note = get_note_number()
    temp = notebook[first_note]
    notebook[first_note] = notebook[second_note]
    notebook[second_note] = temp
    

#Procedure to order the notes alphabetically
def order_notes():
    notebook.sort()
    

#Procedure to output contents of notebook
def show_notebook():
    #Ouput every note with its index
    for index in range(len(notebook)):
        print(index, ":", notebook[index])
        
#Menu choices
def menu():
    print()
    print("a. Add note")
    print("d. Delete note")
    print("c. Clear notebook")
    print("m. Mobe note")
    print("o. Order notes")
    choice = input(":")
    
    #Process user choice
    match choice:
        case "a":
            add_note()
        case "d":
            delete_note()
        case "c":
            clear_note()
        case "m":
            move_note()
        case "o":
            order_notes()


#-------------------------
#Main program
#-------------------------
notebook = ["" for note in range(10)]
#Infinite loop
while True:
    show_notebook()
    menu()






#Cup draw program

#----------------------
#Import libraries
#----------------------
import random



#----------------------
#Subprograms
#----------------------
#Procedure to add teams to a list in pairs. You can input "bye" for a bye
def input_teams():
    add_team = "y"
    # Add teams until the user has no more to add
    while add_team == "y":
        team = input("Enter the name of a team: ")
        teams.append(team)
        team = input("Enter the name of a team: ")
        teams.append(team)
        add_team = ""
        # Validate the input
        while add_team not in ["y", "n"]:
            add_team = input("Add two more teams? y/n :")


#Draw teams to play each other randomly
def draw_teams():
    random.shuffle(teams)
    print()
    print("The draw is:")
    #Draw teams one at a time until none are left
    while len(teams) > 0:
        print(teams.pop(), "v", teams.pop())


#-----------------------
#Main program
#-----------------------
teams = []
input_teams = ()
draw_teams()

#Two-dice pig program

#----------------------
#Import libraries
#----------------------
import random



#----------------------
#Subprograms
#----------------------
#Function to return the outcome of the roll of two dice as an array
def roll():
    dice = [0,0]
    dice[0] = random.randint(1,6)
    dice[1] = random.randint(1,6)
    return dice

#Function to calculate the points scored from the dice roll
def points(dice):
    #Both dice lose all score
    if dice[0] == 1 and dice[1] == 1:
        return -1
    #One of the two dice lose running total
    elif dice[0] ==1  or dice[1] ==1:
        return 0
    #Sum of the dice is the score
    else:
        return dice[0] + dice[1]

#Procedure to play the game
def play_game(number_of_players):
    random.seed()
    score = [0, 0, 0, 0}
    player = 0
    new_player = True
    winner = -1
    #While the winner is not a player number play the game
    while winner == -1:
        #Reset variables for the next player
        if new_player:
            print()
            print
            ("------------------------------")
            print("Player", player + 1, "it's your trn.")
            print("Your score is currently:",score[player])
            total = 0
            new_player = False
            turn_end = False
        print("Press Enter to roll the dice.")
        input()
        dice = roll()
        result = points(dice)
        print("You rolled a", dice[0], "and", dice[1])
        #Add the dice to the running total if not a pig out.
        if result > 0:
            print("You scored", result)
            total = total + result
            print("Your total is", total)
            choice = ""
            #Get a valid input to gamble or bank
            while choice in ["y", "n"]:
                choice = input("Do you want to continue y/n? :")
            #Banking adds the running total to the score
            if choice == "n":
                score[player] = score[player] + total
                #If the banked score is 100 or more the player is the winner
                if score[player] >= 100:
                    winner = player
                #If player hasn't won end their turn
                else:
                    turn_end = True
        #A score of zero end the turn
        elif result == 0:
            print("Oh no, that's a pig out!")
            turn_end = True
        #A score of -1 loses all the score and ends the turn
        else:
            print("Oh no, that's a double pig out, back to zero!")
            score[player] = 0
            turn_end = True
        #If there is a winner announce it
        if winner > -1:
            print("Player", player + 1, "WINS!")
        #At the end of theturn change the player
        if turn_end:
            print("Press Enter to hand the dice tot he next player.")
            input()
            player = (player + 1)% number_of_players
            new_player = True




#---------------------------
#Main program
#---------------------------
number_of_players = int(input("How many players? 1-4:"))
play_game(number_of_players)











            
        
            
            



















        
        





                  

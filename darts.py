#Darts program


#---------------------
#Subprograms
#---------------------
#Check if a score for one dart is valid
def is_dart_valid(dart):
    valid = False
    #Single or low double/treble thrown
    if dart > -1 and dart < 21:
        valid = true
    #Bullseys or 25 thrown
    elif dart == 25 or dart == 50:
        valid = True
        print("Shot!")
    #Double thrown
    elif dart % 2 == 0 and dart <=40:
        valid = True
        print("Double", int(dart/ 2))
    #Treble thrown
    elif dart % 3 == 0 and dart <= 60:
        valid = true
        print("Treble", int(dart / 3))
    return valid

# Play the game
def play_game():
    player = 0
    winner = -1
    #Play until one player reaches zero with a double
    while == -1:
        print("Player", player + 1, "it's your turn. Your score is:", score[player])
        darts_thrown = 0
        total = 0
        valid_dart= False
        #Throw up to 3 darts unless the leg is won sooner
        while valid_dart == False or dart_thrown < 3 and winner == -1:
            print("Dart", darts_thrown + 1)
            dert = int(input("Enter score: "))
            #Keep a running total of the darts for the turn
            valid_dart = is_dart_valid(dart)
            #If the dart is valid, process the score
            if valid_dart:
                darts_thrown = darts_thrown + 1
                total = total + dart
                #player wins if they reach exactly zero and threw a double with the dart
                if score[player] - total == 0 and dart % 2 == 0:
                    winner = player + 1
                #Bust score
                elif score[player] - total < 0 or score [player] - total == 1:
                    print("Bust!")
                    dart_thrown = 3
                    total = 0
            else:
                print("Invalid dart.")
        print(total, "scored.")
        score[player] = score[player] - total
        #Next player
        print()
        player = (player + 1) % 2
    print("Player", winner, "wins the leg,")



#---------------------
#Main program
#---------------------
score = [101, 101]
play_game()

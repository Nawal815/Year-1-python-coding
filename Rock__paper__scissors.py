#Rock, paper, scissors program

#-----------------------
# Import libraries
#-----------------------



#-----------------------
#Subprograms
#-----------------------
#Function to convert r/p/s to rock, paper, scissors
#Input is less hassle for the user and output is nice
def convert (rps):
    match rps:
        case "r":
            return "rock"
        case "p":
            return "paper"
        case "s":
            return "scissors"
        
#Function to return valid player choice
def get_player_choice():
    valid = False
    #Input must be r,p or s
    while not valid:
        choice =input("Enter rock, paper, scissors (r/p/s): ")
        if choice == "r" or choice == "p" or choice == "s":
            valid = True
    return choice


        
#Function to return cpu choice 
def get_cpu_choice():
    cpu = random.randint (1, 3)
    #convert random number to cpu choice
    match cpu:
        case 1:
            return "r"
        case 2:
            return "p"
        case 3:
            return "s"
    
#Function to determine the winner of a round
def who_won_round(player, cpu):
    winner = "draw"
    #Check who wins the round
    if player == "r" and cpu == "s":
        winner = "player"
    if player == "p" and cpu == "r":
        winner = "player"
    if player == "s" and cpu == "p":
        winner = "player"
    if cpu == "r" and player == "s":
        winner = "cpu"
    if cpu == "p" and player == "r":
        winner = "cpu"
    if cpu == "s" and player == "p":
        winner = "cpu"
    return winner

#Procedure to play the game - first to 5 points 
def play_game():
    player_score = 0
    cpu_score = 0
    random.seed()
    #Play until a score of 10 is reached
    while player_score < 5 and cpu_score < 5:
        print("player score:", player_score, "cpu score:", cpu_score)
        player_choice = get_player_choice()
        cpu_choice = get_cpu_choice()
        round_winner = who_won_round
        (player_choice, cpu_choice)
        player_shape = convert(player_choice)
        cpu_shape = convert(cpu_choice)
        #Add to the score
        if round_winner == "player":
            print("player's", player_shape, "beat's cpu's", cpu_shape)
            player_score = player_score + 1
        elif round_winner == "player":
            print("cpu's", cpu_shape, "neat's player's", player_shape)
            cpu_score = cpu_score + 1
        else:
            print(player_shape, "-",cpu-shape, "- it's a draw.")
        print()
    if player_score == 10:
        print("Player WINS!")
    else:
        print("CPU WINS!")
        
#-----------------------
#Main program
#-----------------------
play_game()
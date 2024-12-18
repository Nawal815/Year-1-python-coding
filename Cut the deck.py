#Cut the decl program


#---------------------
#Import libraries
#---------------------
import random



#---------------------
#Subprograms
#---------------------
#Output who won the card game
def output_winner(player_card, cpu_card):
    #Find the card value of each card from the position in the ordered array of cards
    player_card_value = cards.index(player_card)
    cpu_card_value = cards.index(cpu_card)
    #If both cards have the same value ...
    if player_card_value % 9 == cpu_card_value % 9:
        # ...and the player's suit is higher, the player wins.
        if player_card_value > cpu_card_value:
            print("You win!")
    #If player card has a higher value, the player wins
    elif player_card_value % 9 > cpu_card_value %9:
        print("You win!")
    #In all other cases the CPU wins.
    else:
        print("CPU wins.")


#Play the game
def play_game():
    random.shuffle(deck)
    #Player cuts the deck
    player_choice = int(input("What number card do you wan to draw? 0-34:"))
    player_card = deck[player_choice]
    print("You reveal the", player_card)
    #CPU cuts the deck
    cpu_choice = random.randint(player_choice + 1, 35)
    cpu_card = deck[cpu_choice]
    print("The CPU reveals the", cpu_card)

    output_winner(player_card, cpu_card)



#---------------------
#Main program
#---------------------
random.seed()
#The value order of the cards for reference
cards = ["6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
         "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
         "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
         "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]

#The deack to be shuffled and used to play the game
deck = cards.caopy()

play_game()












    

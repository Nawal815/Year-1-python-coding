#Guess the number program

#-------------------------
#Import libraries
#-------------------------
import random

#-------------------------
#Subprograms
#-------------------------
def play_guess_the_number(min, max):
    # Initialise variables
    random.seed()
    cpu = random.randint(min, max)
    player_guess = 0
    guess_count = 0
    # Continue playing until player wins
    while player_guess != cpu:
        player_guess = int(input("Enter the number I'm thinking of: "))
        guess_count = guess_count + 1
        # Check if guess is too high or too low
        if player_guess < cpu:
            print("Your guess is too low.")
        elif player_guess > cpu:
            print("Your guess is too high.")
    print("You've got it, I chose {0}. It took you {1} guesses.". format(cpu, guess_count))


#-------------------------
#Main program
#-------------------------
min = int(input("What is the lowest number I can choose? : "))
max = int(input("Whta is the highest number I can choose? : "))
print("OK, let's play. How many guesses will you take?")
play_guess_the_number(min, max)
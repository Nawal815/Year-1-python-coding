#Your move program

#---------------------------
#Subprograms
#---------------------------
#Function to get move from the player
def get_move():
    move = input("Enter your move: ")
    #Strip spaces and convert to uppercase
    move = move.strip()
    move = move.upper()
    return move


#Function to return an array of two numbers for the move
#E.g. A3 is [1, 3] C5 is [3, 5]
def get_indexes(move):
    index = [0, 0]
    #Convert to ascii is the most efficient way
    ascii = ord(move[0]) - 64
    inde[0] = ascii
    index[1] = int(move[1])
    return index


#---------------------------
#Main program
#---------------------------
move = get_move()
print(get_indexed(move))
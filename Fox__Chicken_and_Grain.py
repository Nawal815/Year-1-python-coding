#Fox, chicken, grain program

#-------------------------
#Subprograms
#-------------------------
#Output the state of the puzzle
from xml.sax.handler import all_features


def output():
    print("---------------------")
    print("This side of the river:")
    #Check if the farmer, fox or grain is this side of the river
    if farmer == 0:
        print("Farmer")
    if fox == 0:
        print("Fox")
    if chicken == 0:
        print("Chicken")
    if grain == 0:
        print("Grain")
    print()
    print("The other side of the river:")
    #Check if the farmer, fox or grain is on the other side of the river
    if farmer == 1:
        print("Farmer")
    if fox == 1:
        print("Fox")
    if chicken == 1:
        print("Chicken")
    if grain == 0:
        print("Grain")
    print("---------------------")
    
#Check if the puzzle is lost
def wrong_move():
    #The farmer is this side of the river
    if farmer == 0:
        #Check if the fox was left with the chicken
        if fox == 1 and chicken == 1:
            print("The fox ate the chicken.")
            return True
        #Check if the chicken was left with the grain
        if chicken == 1 and grain == 1:
            print("The chicken ate the grain.")
            return True
    #The farmer is on the other side of the river
    if farmer == 1:
        #Check if the fox was left with the chicken
        if fox == 0 and chicken == 0:
            print("The fox ate the chicken.")
            return True
        #Check if the chicken was leeft with the grain
        if chicken == 0 and grain == 0:
            print("The chicken ate the grain")
            return True
    return False


#Check if the puzzle has been solved
def puzzle_solved():
    #If the fox, chicken and grain are all on the other side of the river the puzzle is solved 
    if fox == 1 and chicken == 1 and grain == 1:
        print("You solved the puzzle.")
        return True
    else:
        return False
    

#-------------------------
#Main program
#-------------------------
print("A fox, chicken and a bag of grain wait by the side of a river.")
fox = 0
chicken = 0
grain = 0
farmer = 0
game_over = False
#Keep running until the puzzle is solved or a wrong move is taken
while not game_over:
    print("Which item will you take in your rowboat to the other side?")
    print("fox, chicken, grain or farmer?")
    choice = input("Choose: ")
    #Handle each item being moved
    match choice:
        case "farmer":
            if farmer == 0:
                farmer = 1
            else:
                farmer = 0
        case "fox":
            if farmer == fox and fox == 0:
                fox = 1
                farmer = 1
            elif farmer == fox and fox == 1:
                fox = 0
                farmer = 0
        case "chicken":
            if farmer == chicken and chicken == 0:
                chicken = 1
                farmer = 1
            elif farmer == chicken and chicken == 1:
                chicken = 0
                farmer = 0
        case "grain":
            if farmer == grain and grain == 0:
                grain = 1
                farmer = 1
            elif farmer == grain and grain == 0:
                grain = 0
                farmer = 0
    output()
    #Check the puzzle winning and losing condition
    if puzzle_solved() or wrong_move():
        game_over = True

            








            








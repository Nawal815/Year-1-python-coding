#Feud program

#-----------------------
#Subprograms
#-----------------------
#forage for herb
def forage_herb():
    herb = input("What herb do you want to look for? :")
    #Collect the herb if it exists
    if herb in ["dandelion", "burdock", "pipewort", "ragwort", "snapdragon", "toadflax"]:
        herbs_collected.append(herb)
        print(herb, "found.")
    else:
        print("Cannot find herb")

#Turn herbs into spells
def cauldron(spell, herb):
    #You must have the correct herbs to make the spell
    if herb[0] in herbs_collected and herb[1] in herbs_collected:
        herbs_collected.remove(herb[0])
        herbs_collected.remove(herb[1])
        spells_brewed.append(spell)
        print(spell, "has been brewed.")
    else:
        print("Cannot brew the spell, you don't have the correct herbs.")

#Brew spell with required ingedients
def brew_spell():
    spell = input("What spell do you want to brew? :")
    #If the spell is valid try and brew in the cauldron
    match spell:
        case "teleport":
            cauldron(spell, ["dandelion", "burdock"])
        case "protect":
            cauldron(spell, ["pipewort", "ragwort"])
        case "sprites":
            cauldron(spell, ["snapdragon", "toadflax"])
        case _:
            print("That spell is not in the spell book.")


#cast spell
def cast_spell():
    spell = input("What spell do you want to cast? :")
    #Cast a spell only if it has been brewed
    if spell in spells_brewed:
        spells_brewed.remove(spell)
        print(spell, "has been cast.")
    else:
        print("You have not brewed that spell.")

#Player takes an action
def take-action():
    choice = ""
    #Get a valid action from the player
    while choice not in ["f", "b", "c"]:
        choice = input("Forage herb, brew or cast a spell? f/b/c :")
    #take the action chosen
    match choise:
        case "f":
            forage_herb()
        case "b":
            brew_spell()
        case "c":
            cast_spell()



#-----------------------
#Main program
#-----------------------
herbs_collected = []
spells_brewed = []
#Infinite loop
while True:
    take_action()


            

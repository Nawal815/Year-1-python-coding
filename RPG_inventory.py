#RPG inventory program

#----------------------
#Subprograms
#----------------------
#Procedure to add an item to the inventory
def add_item():
    item = input("What item are you addin to your inventory? : ")
    inventory.append(item)
    print("Item added.")
    
#Procedure to search for an item in the inventory
def search():
    item = input("What item do you want to see if you have? : ")
    if item in inventory:
        print("You have the item.")
    else:
        print("You do not have a", item)
        
#Procedure to remove an item from the inventory
def drop_item():
    item = input("What item do you want to drop? : ")
    #Check item exists
    if item in inventory:
        inventory.remove(item)
        print("Item dropped.")
    else:
        print("You do not have this item.")
        
#Procedure to show and item in an inventory slot
def look():
    slot = int(input("Which inventory slot do you want to look at? : "))
    if slot < len(inventory):
        print("you have a", inventory[slot], "in slot")
    else:
        print("Invalid slot.")
        
#Procedure to craft an item
def craft_item():
    item = input("What item do you want to craft? : ")
    #Craft the item if the correct items are available
    if item == "charm" and "gem" in inventory and "leather" in inventory:
        inventory.remove("gem")
        inventory.remove("leather")
        inventory.remove("charm")
        print(item, "crafted.")
    else:
        print("You do not have the items to do this.")
        
#Procedute to choose an action
def choose_action():
    print("You have", len(inventory), "items in your inventory.")
    action = input("What action do you want to take? (add/craft/look/drop/search) : ")
    match action:
        case "add":
            add_item()
        case "craft":
            craft_item()
        case "drop":
            drop_item()
        case "look":
            look()
        case "search":
            search()
    print()
    


#------------------------
#Main program
#------------------------
inventory = ["sword", "sheild"]
while True:
    print(inventory)
    choose_action()
     
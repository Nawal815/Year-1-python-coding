
#Find and replace program

#-------------------------
#Subprograms
#-------------------------
#Function to replace x with y in list l
def replace(x, y, l):
    for index in range(len(l)):
        if l[index] == x:
            l[index] = y
    return l


#Procedure to output the list, each item on a new line
def output(l):
    for word in l:
        print(word)
        
#-------------------------
#Main program
#-------------------------
rhyme = ["roly", "poly", "roly", "poly", "up", "up", "up",
         "roly", "poly", "roly", "poly", "down", "down", "down"]
output(rhyme)
word = input("Which word to replace? :")
new_word = input("Replace with what? :")
rhyme = replace(word, new_word, rhyme)
output(rhyme)
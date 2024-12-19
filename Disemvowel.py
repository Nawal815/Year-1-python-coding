#Disemvowel program

#---------------------------
#Subprograms
#---------------------------
#Remove the vowels from a message
def dvowel(message):
    dvowelled = message.replace("a", "")
    dvowelled = dvowelled.replace("A", "")
    dvowelled = dvowelled.replace("e", "")
    dvowelled = dvowelled.replace("E", "")
    dvowelled = dvowelled.replace("i", "")
    dvowelled = dvowelled.replace("I", "")
    dvowelled = dvowelled.replace("o", "")
    dvowelled = dvowelled.replace("O", "")
    dvowelled = dvowelled.replace("u", "")
    dvowelled = dvowelled.replace("U", "")
    return dvowelled

#Alternative approach
#def dvowela(message):
#   dvowelled = ""
#   #Consider each character
#   for index in range(len(message)):
#       #Only add the character to the message if it is not a vowel
#       if message[index] not in "AaEeIiOoUu":
#           dvowelled = dvowelled + message[index]
#   return dvowelled


#---------------------------
#Main program
#---------------------------
message = input("Enter the message: ")
print("The disemvowelled version of the message is: ")
print(dvowel(message))
print(dvowela(message))
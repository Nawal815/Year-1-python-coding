#Palindrome program

#-------------------------
#Subprograms
#-------------------------
def palindrome(phrase):
    #Convert to lowercase for like-for-like comparisons
    phrase = phrase.lower()
    is_palindrome = True
    #Set indexes to beginning and end od the phrase
    letter_front = 0
    letter_back = len(phrase) - 1
    
    #Check all the letters up to half way or if the phrase is not a palindrome
    while(letter_front < len(phrase) // 2) and is_palindrome:
        #Skip over any characters that are not alphanumerics
        while not phrase[letter_front].isalnum():
            letter_front = letter_front + 1
        while not phrase[letter_back].isalnum():
            letter_back = letter_back - 1
        #If the two letters are nto the same the phrase is not a palindrome
        if phrase[letter_front] != phrase[letter_back]:
            is_palindrome = False
        #Increment and decrement the indexes
        letter_front = letter_front + 1
        letter_back = letter_back - 1
    return is_palindrome


#-------------------------
#Main program
#-------------------------
phrase = input("Enter a phrase: ")
#Check if the phrase is a palindrome
if palindrome(phrase):
    print(phrase, "is a palindrome.")
else:
    print(phrase, "is not a palindrome.")
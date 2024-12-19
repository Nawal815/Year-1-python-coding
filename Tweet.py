#Tweet program

#----------------------------
#Subprograms
#----------------------------
#Return message as a list of elements, each being num_chars long
def tweets(message, num_chars):
    tweet_list = []
    tweet = ""
    #Add each character to a list
    for index in range(len(message)):
        tweet = tweet + message[index]
        #Start a new tweet if num_chars reached
        if (index + 1) % num_chars == 0:
            tweet_list.append(tweet)
            tweet = ""
    #Add the last charactrs to the list if not exactly divisuble by num_chars
    if tweet != "":
        tweet_list.append(tweet)
    return tweet_list

#----------------------------
#Main program
#----------------------------
message = input("Enter the message: ")
max_chars = int(input("How many characters per message? :"))
print(tweets(message, max_chars))
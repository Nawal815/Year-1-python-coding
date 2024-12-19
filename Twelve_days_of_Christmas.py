#Twelve days of Christmas program

#-------------------------
#Subprograms
#-------------------------
#Procedure to output the twelve days of Christmas
def output_song():
    day = ["first", "second", "third", "fourth", "fifth"]
    item = ["partridge in a pear tree.", "Two turtle doves", "Three french hens", "Four calling birds", "Five gold rings"]
    verse = 0
    reverse_verse = 0
    #Output each verse
    for verse in range(len(day)):
        print("On the", day[verse], "of Christmas")
        print("My true love gave to me")
        #All the items from the previous verses are output
        for reverse_verse in range(verse, 0, -1):
            #Output only one partridge!
            if reverse_verse > 0:
                print(item[reverse_verse])
        #Needs an 'A' or 'And' prefix depending on the verse
        if verse == 0:
            print("A", item[0])
        else:
            print("And a", item[0])
        print()
        

#-------------------------
#Main program
#-------------------------
output_song()        
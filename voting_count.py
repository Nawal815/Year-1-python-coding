#Voting count program

#----------------------------
#Subprograms
#----------------------------
#Function to count votes A, B and return results as an array
def count_votes(ballot):
    result = [0, 0, 0, 0]
    #Look at each vote cast
    for vote in ballot:
        #Count A, B, C, D
        match vote:
            case "A":
                result[0] = result[0] + 1
            case "B":
                result[1] = result[1] + 1
            case "C":
                result[2] = result[2] + 1
            case "D":
                result[3] = result[3] + 1
    return result


#----------------------------
#Main program
#----------------------------
votes = ["A", "B", "B", "B", "B", "C", "C", "D", "A", "B",
         "A", "B", "A", "B", "D", "B", "C", "B", "B", "A"]

result = count_votes(votes)
print("Answer A:", result[0])
print("Answer B:", result[1])
print("Answer C:", result[2])
print("Answer D:", result[3])




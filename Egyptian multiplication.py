#Egyptian multiplication program

#-------------------------
#Subprograms
#-------------------------
#Input the numbers and return a list of the numbers
def input_numbers():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    return [first_number, second_number]

#Run the Egyptian multiplication algorithm
def mul(numbers):
    first_number = number[0]
    second_number = numbers[1]
    column1 = []
    # Stage 1 - Write the numbers into first column
    column1.append(first_number)
    #Integer division the first number by 2 until 1 is reaches
    while first_number > 1:
        first_number = first_number // 2
        column1.append(first_number)

    #Stage 2 - Write the numbers into the second column
    column2 = []
    column2.append(second_number)
    #Multiply the second number by 2 for as many times as there are numbers in the first column
    for counter in range(len(column1) - 1):
        second_number = second_number * 2
        column2.append(second_number)

    #The result is two columns with equal number or numbers
    #Stage 3 - remove number in the second column if the number in the first column is even
    column2_counter = 0
    #Consider each number in the first column
    for counter in range(len(column1)):
        #If it even remove the number from the second column...
        if column1[counter] % 2 == 0:
            column2.pop(column2_counter)
        #...or increase the index in the second column
        else:
            column2_counter = column2_counter + 1

    #Stage 4 - Add up the numbers in the second column
    total = 0
    #Consider each number left in column 2
    for number in column2:
        total = total + number

    #The result is the multiplication of the two numbers
    return total


#-------------------------
#Main program
#-------------------------
numbers = input_numbers()
print(mul(numbers))







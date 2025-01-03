#A program to display terms of the fibonacci sequence

#---------------------
#Subprograms
#---------------------
def generate_next_term(first_term, second_term):
    next_term = first_term + second_term
    return next_term
number_of_terms_generated = 0
while number_of_terms_generated < number_of_terms:
  print(first_term) 
  next_term = generate_next_term(first_term, second_term)
  first_term = second_term
  second_term = next_term
  number_of_terms_generated += 1
#---------------------
#Main program
#---------------------
print("Welcome to the fibonacci sequence generator!")
number_of_terms = int(input("How many terms would you like?"))
first_term = 0
second_term = 1
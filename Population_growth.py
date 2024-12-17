#A program to calculate the size of a population after a given number of years, given the average growth per year.

#----------------------
#Subprograms
#----------------------
def calculate_population_size(current_population_size, grwoth):
    new_population_size = population_size * (population_growth ** years)
    return new_population_size



#----------------------
#Main program
#----------------------
population_size = int(input("Enter the size of the current population: "))
population_growth = float(input("Enter the current percentage growth of the population per year (in the format 1.xx): "))
years = int(input("Enter the number of years of population growth: "))
future_population_size = calculate_population_size(population_size, population_growth)
print("In", years, "years time, the populatio will be :", future_population_size)




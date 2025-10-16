# Program #3: US_Population
#programmer:Devin Goshaw
#Date:10/12/25
#program: Us Population program


def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    num_entries = int(input("How many states populations would you like to enter? "))
    # Now have the user enter a year. 
     
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    for i in range(num_entries):
        print("\nEntry", i + 1)
        year = int(input("Enter the year: "))
        state = input("Enter the state name: ")
        population = int(input("Enter the population: "))

    all_entered_values.append([year, state, population])
    year_to_sum = int(input("\nEnter a year to find the total population: "))
    sum_population_for_year(all_entered_values, year_to_sum)

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    total_population = 0
    for record in all_entered_values:
        if record[0] == year_to_sum:
            total_population += record[2]
    # print the totalled population
    print("\nTotal population for year", year_to_sum, "is:", total_population)

# Call the main function.
if __name__ == '__main__':
    main()
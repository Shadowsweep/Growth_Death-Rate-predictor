import random
import time
import matplotlib.pyplot as plt

current_year = time.localtime().tm_year
print('*************************** Welcome to Our Island! ********************************\n')
current_population = int(input('Enter the initial population of our island(positive and greater than 100): '))

# Validate initial population
while current_population < 100:
    print('Initial population must be at least 100.(Should not be negative) \n')
    current_population = int(input('Enter the initial population of our island (positive): '))

death_reasons = ['disease', 'accident', 'natural causes', 'disaster']

def simulate_population(year, population):
    # Keep generating birth and death rates until the difference is within the required limit
    while True:
        birth_rate = random.randint(population, population*3)
        death_rate = random.randint(population, population*3)

        if death_rate / birth_rate <= 1.1:
            break
        elif birth_rate / death_rate <= 2:
            break

    # Generate a random number less than the length of death_reasons
    num_reasons = random.randint(1, len(death_reasons))

    # Pick num_reasons reasons randomly from the list of death reasons
    selected_reasons = random.sample(death_reasons, num_reasons)

    # Divide death rate among the selected reasons
    death_rates_by_reason = [int(death_rate / num_reasons)] * num_reasons

    # Distribute the remainder of the death rate randomly among the selected reasons
    remaining_death_rate = death_rate % num_reasons
    if remaining_death_rate > 0:
        extra_reasons = random.sample(selected_reasons, remaining_death_rate)
        for reason in extra_reasons:
            index = selected_reasons.index(reason)
            death_rates_by_reason[index] += 1

    population += int(birth_rate) - int(death_rate)

    # If population falls below 2, reset the population to initial and continue simulation
    if population < 2:
        print('\n Population is insufficient. Resetting population to initial.\n')
        population = current_population

    # Print the statistics for the year
    birth_text = f'{int(birth_rate)} people were born'
    death_text = ', '.join([f'{death_rates_by_reason[i]} due to {selected_reasons[i]}' for i in range(num_reasons)])
    death_text = f'{sum(death_rates_by_reason)} people died ({death_text})'
    pop_text = f'Population: {population}'
    print(f'In {year}, {birth_text} and {death_text}. {pop_text}\n')
    return population

# create empty lists to store population and year data
population_data = []
year_data = []

while True:
    try:
        user_year = int(input('Enter the year to check population(starting from current time till the year u want ):  '))
        if user_year < current_year:
            raise ValueError
        break
    except ValueError:
        print('Invalid input, please try again.\n')

population = current_population
for year in range(current_year, user_year+1):
    population = simulate_population(year, population)
    # append population and year data to their respective

import random


def infect(infection_probability: float):
    """
    takes a float giving the infection probability for the disease
    :param infection_probability:
    :return: randomly True or False
    """
    random_number = random.uniform(0, 1)
    if random_number < infection_probability:
        return True
    else:
        return False


def infect_test(num_times: int):
    """
    Test infect function
    :param num_times: int
    :return: total_infected and total_uninfected
    """
    total_infected = 0
    total_uninfected = 0
    for trial in range(num_times):
        result = infect(0.2)
        if result:
            total_infected += 1
        else:
            total_uninfected += 1
    return total_infected, total_uninfected


def recover(recovery_probability: float):
    """
    takes a float giving the recovery probability for a person
    infected with the disease
    :param recovery_probability: float
    :return: Randomly True or False
    """
    random_number1 = random.uniform(0, 1)
    if random_number1 < recovery_probability:
        return True
    else:
        return False


def contact_indices(pop_size: int, source: int, contact_range: int):
    """
    The function contact indices will return a list containing the
    indices within contact range positions of source in population list.
    :param pop_size: int
    :param source: int
    :param contact_range: int
    :return: the list of indices of people came in contact with infected people
    """
    start_index = max(0, source - contact_range)
    end_index = min(pop_size, source + contact_range + 1)

    indices = []
    for i in range(start_index, end_index):
        indices.append(i)
    return indices


def apply_recoveries(population: list, recovery_probability: float):
    """
    iterates through the list population once, uses the function recover to
    determine whether the infected person recovers
    :param population: list
    :param recovery_probability: float
    :return: True means recovers, False means otherwise
    """
    for i in range(len(population)):
        if population[i] == 'I' and recover(recovery_probability):
            population[i] = 'R'


def contact(population: list, source: int, contact_range: int, infect_chance: float):
    """
    makes changes to the list population based on the given parameters.
    :param population: list
    :param source: int.
    :param contact_range: int
    :param infect_chance: float
    :return: None
    """
    pop_size = len(population)
    start_index = max(0, source - contact_range)
    end_index = min(pop_size, source + contact_range + 1)

    for contact_index in range(start_index, end_index):
        if population[contact_index] == 'S' and infect(infect_chance):
            population[contact_index] = 'I'


def apply_contacts(population: list, contact_range: int, infect_chance: float):
    """
    Simulates all infected people in the population coming into contact with others.
    :param population: list
    :param contact_range: int
    :param infect_chance: float
    :return: None
    """
    currently_infected = []

    # Find currently infected individuals
    for i in range(len(population)):
        if population[i] == 'I':
            currently_infected.append(i)

    # Simulate contacts and infections
    for infected_person in currently_infected:
        start_index = max(0, infected_person - contact_range)
        end_index = min(len(population), infected_person + contact_range + 1)

        for contact_index in range(start_index, end_index):
            if population[contact_index] == 'S' and infect(infect_chance):
                population[contact_index] = 'I'


def population_SIR_counts(population: list):
    """
    Counts the number of susceptible, infected, and recovered individuals.
    :param population: list
    :return: dictionary with counts
    """
    counts = {'susceptible': 0, 'infected': 0, 'recovered': 0}

    for status in population:
        if status == 'S':
            counts['susceptible'] += 1
        elif status == 'I':
            counts['infected'] += 1
        elif status == 'R':
            counts['recovered'] += 1

    return counts


def simulate_day(population: list, contact_range: int, infect_chance: float, recover_chance: float):
    """
    Simulates one day in the progression of the disease.
    :param population: list
    :param contact_range: int
    :param infect_chance: float.
    :param recover_chance: float
    :return: None
    """
    apply_recoveries(population, recover_chance)
    apply_contacts(population, contact_range, infect_chance)


def initialize_population(pop_size: int) -> list:
    """
    Initializes the population with one infected individual.
    :param pop_size: int
    :return: list representing the population
    """
    population = ['S'] * pop_size
    population[0] = 'I'
    return population


def simulate_disease(pop_size: int, contact_range: int, infect_chance: float, recover_chance: float) -> list:
    population = initialize_population(pop_size)
    counts = population_SIR_counts(population)
    all_counts = [counts]
    while counts['infected'] > 0:
        simulate_day(population, contact_range, infect_chance, recover_chance)
        counts = population_SIR_counts(population)
        all_counts.append(counts)
    return all_counts


def peak_infections(all_counts: list) -> int:
    max_infections = 0
    for day in all_counts:
        if day['infected'] > max_infections:
            max_infections = day['infected']
    return max_infections


def display_results(all_counts: list) -> None:
    num_days = len(all_counts)
    days, sus, inf, rec = 'Day', 'Susceptible', 'Infected', 'Recovered'
    print(f'{days:>12}{sus:>12}{inf:>12}{rec:>12}')
    for day in range(num_days):
        print(f'{str(day):>12}{all_counts[day]["susceptible"]:>12}{all_counts[day]["infected"]:>12}'
              f'{all_counts[day]["recovered"]:>12}')
    print(f'\nPeak Infections: {peak_infections(all_counts)}')


def main():
    # Test
    i, u = infect_test(1000)
    print(f'Total infected: {i}, Total uninfected: {u}')

    # Recovery test
    def recovery_test(num_times):
        result = []
        for _ in range(num_times):
            population1 = ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I']
            apply_recoveries(population1, 0.3)
            result.append(population1.count('R'))
        return sum(result) / len(result)

    print(recovery_test(1000))

    # Used for Task 2, only change contact_range
    counts = simulate_disease(100, 2, 0.2, 0.05)
    print(display_results(counts))


if __name__ == "__main__":
    main()

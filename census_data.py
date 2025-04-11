def get_data(filename: str):
    """
    Takes a file name and returns a list of strings
    :param filename: Name of the file that contain the strings
    :return: A list of string
    """
    with open(filename, 'r') as file:  # Open file in read mode
        data = file.readlines()  # Read lines
    return data


def parse_data(file_name: str):
    """
    Take the list of strings and return it in readable format
    :param file_name: Name of the file that contain the strings
    :return: A string without extra characters asides from numbers
    """
    data = get_data(file_name)  # Result from get_data
    parsed_data = []  # Empty object

    for a in data:
        strip_line = a.strip("\n")  # Strip data of \n
        values = (strip_line.split(','))  # Split the line into a list of values with a comma
        parsed_data.append(values)  # Append the list of values to the parsed_data list
    return parsed_data


def get_populations(file_name: str):
    """
    Takes the result of parse_data and return only the populations
    :param file_name: Name of the file that contain the strings
    :return: A list of strings containing only the populations of the counties
    """
    pop_parsed = parse_data(file_name)  # Result from parse_data
    populations = []  # Empty object

    for pop in pop_parsed:
        populations.append(pop[2])  # Append only population numbers from the list

    return populations


def leading_digits(file_name: str):
    """
    Prints the frequency of leading digits in the populations list
    :param file_name: Name of the file that contain the strings
    :return: Frequency of the population in the file from highest to lowest order
    """
    pop_lead = get_populations(file_name)  # Result from get_populations
    total_digit = []
    digit_counted = {}

    # Collect leading digits
    for i in pop_lead:
        total_digit.append(i[0])  # Append the first index

    # Count occurrences of each digit
    for d in total_digit:
        digit_counted[d] = digit_counted.get(d, 0) + 1

    # Calculate frequencies and print
    for digit in range(1, 10):
        frequency = digit_counted.get(str(digit), 0) / len(total_digit)
        print(f"Frequency of {digit}: {frequency:.1%}")


# Print for the 3 dataset
print(leading_digits("data1.csv"))
print(leading_digits("data2.csv"))
print(leading_digits("data3.csv"))

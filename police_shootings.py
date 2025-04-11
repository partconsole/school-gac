def create_database(filename):
    data_file = open(filename, 'r')
    data_lines = data_file.readlines()

    database = {}
    for row in range(1, len(data_lines)):
        line = data_lines[row]
        entries = line.split(',')
        db_entry = {"name": entries[11], "date": entries[1], "armed_with": entries[4], "age": entries[12],
                    "gender": entries[13], "race": entries[14], "state": entries[7]}
        entry_id = int(entries[0])
        database[entry_id] = db_entry

    return database


def main():
    databases = create_database('fatal-police-shootings-data.csv')

    # Task 3
    # Print the name of the subject of the fatal police shooting with ID number 1694
    if 1694 in databases:
        print(databases[1694]["name"])

    # Print the name of all subjects of fatal police shootings in Minnesota
    minnesota_shootings = []
    for k, v in databases.items():
        if v["state"] == "MN":
            minnesota_shootings.append(v["name"])
    print(minnesota_shootings)

    # Create race_counts
    race_counts = {}
    total_shootings = len(databases)

    for k, v in databases.items():
        race = v["race"]
        # Skip entries with wrong input race
        if race != "male":
            race_counts[race] = race_counts.get(race, 0) + 1

    # Print fraction of fatal police shootings by race
    for race, count in race_counts.items():
        fraction = count / total_shootings
        print(f"{race}: {fraction}")

    # Question 1
    # Create a new dictionary for unarmed subjects
    unarmed_selection = {}
    for k, v in databases.items():
        if v["armed_with"] == "unarmed":
            unarmed_selection[k] = v

    # Create a new dictionary for counting races among unarmed subjects
    unarmed_race_counts = {}
    for k, v in unarmed_selection.items():
        race = v["race"]
        unarmed_race_counts[race] = unarmed_race_counts.get(race, 0) + 1

    # Print the fraction of unarmed fatal police shootings with a black subject
    total_unarmed_shootings = len(unarmed_selection)
    black_unarmed_shootings = unarmed_race_counts.get("B", 0)
    fraction_black_unarmed = black_unarmed_shootings / total_unarmed_shootings
    print(f"Black unarmed fraction: {fraction_black_unarmed}")


if __name__ == "__main__":
    main()

# Task 2 Question 3 - Check for class
database = create_database('fatal-police-shootings-data.csv')
value_type = type(database[8893])
print(value_type)

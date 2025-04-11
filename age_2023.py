def current_age() -> int:
    """Asks the user for their birthday to determine their age as of 10/26/2023"""
    # Get user input
    bday = input("Enter your birth day in the form mm/dd/yyyy: ")

    # Split input into month, day, year
    bday_split = bday.split("/")
    bday_month = int(bday_split[0])
    bday_day = int(bday_split[1])
    bday_year = int(bday_split[2])

    # Set project start date
    project_start_date = (2023, 10, 26)

    # Calculate age
    age = project_start_date[0] - bday_year

    # Check for TRUE
    if (bday_month, bday_day) == project_start_date[1:]:
        print("Happy Birthday!")

    return age


# Usage
if __name__ == "__main__":
    age = current_age()
    print(f'Your age is: {age}')

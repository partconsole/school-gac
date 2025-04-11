# Assign values to lawn depth and width
lawn_depth = float(input("Enter depth on lawn here: "))
lawn_width = float(input("Enter width on lawn here: "))

# calculate the area of the lawn
lawn_area = lawn_depth * lawn_width

# calculate how long it takes to mow an area knowing speed is two square feet per second
mow_time_hours = int((lawn_area/2)/3600)
mow_time_minutes = (int((lawn_area/2)/60))%60
mow_time_seconds = (int(lawn_area/2))%60

print(f'It will take {mow_time_hours} hours, {mow_time_minutes} minutes, and {mow_time_seconds} seconds to mow the lawn.')

# calculate how much to charge if I charge $20/hr
mow_charge = round(float(mow_time_hours*20), 2)

print(f'The total cost for mowing the lawn would be ${mow_charge}')
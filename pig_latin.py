# Task 1: Daemyen and Minh
# get user inputted pig latin word
pig_latin = input("Please enter a word in pig latin: ")

# split at "-" and create a list with ending and starting word
idx = pig_latin.find('-')

# create variables that will be used for concatenation
# first part of split
end = pig_latin[0:idx]

# second part of split and removes the ending 'ay'
start = pig_latin[idx+1:-2]

# display word after concatenation
print(start + end)
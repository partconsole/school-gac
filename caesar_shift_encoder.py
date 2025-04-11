# Task 2: Daemyen and Minh
# collect user input for phrase and number of skips
phrase = input("Please enter an English phrase in all lowercase: ")
num_skips = int(input("Please enter how many letters to shift forward by: "))

# use for loop to loop through every character and change it
encoded_phrase = ""
for i in phrase:
    # turn i into number and subtract by lowercase 'a' and add by the shift forward
    # use modulus 26 to keep within a-z range and add by uppercase 'A' to get to uppercase letters
    # turn entire equation into character
    encoded_phrase += chr(((ord(i) - 97) + num_skips) % 26 + 65)

print(encoded_phrase)
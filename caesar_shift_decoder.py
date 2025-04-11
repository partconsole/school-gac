# Task 3: Daemyen and Minh
# collect user input for phrase to decode
phrase = input("Please enter a Caesar shift cipher encrypted phrase: ")
num_skips = int(input("Please enter the number of letters the phrase was shifted: "))

# use for loop to loop through every character and change it
decoded_phrase = ""
for i in phrase:
    # similar to encoder but the opposite
    # change to number and subtract by uppercase 'A' and remove the number of skips by subtraction
    # use mod 26 to keep within a-z range and add by lowercase 'a' to get to lowercase letters
    # turn entire equation into a character
    decoded_phrase += chr(((ord(i) - 65) - num_skips) % 26 + 97)

print(decoded_phrase)
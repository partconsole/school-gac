#Group: Minh and Daemyen

def railfence(phrase: str) -> str:
    """
    To encode a phrase using Rail fence Cipher and output the encoded phrase
    :param phrase: Input phrase as a string
    :return: Encoded phrase
    """

    # Create three empty strings to hold characters above, between, and below the rails
    above_rail = ""
    between_rail = ""
    below_rail = ""

    # Loops through the characters in the input string
    # Above
    for idx in range(0, len(phrase), 4):
        above_rail += phrase[idx]

    # Between
    for idx in range(1, len(phrase), 2):
        between_rail += phrase[idx]

    # Below
    for idx in range(2, len(phrase), 4):
        below_rail += phrase[idx]

    # Concatenate 3 strings
    encoded_phrase = above_rail + between_rail + below_rail

    return encoded_phrase


# Testing
print(railfence("Railfence Cipher"))

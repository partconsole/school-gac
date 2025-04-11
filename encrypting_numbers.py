#Group: Minh and Daemyen

import copy


def swap(decrypted_list: list):
    """
    Swap every two integers next to each other
    :param decrypted_list: A list of integers
    :return: None
    """
    # Start at first index and skip every two so swap happens to each integer once
    # Go to the length of the list minus one because for loop uses the next index in list
    for idx in range(0, len(decrypted_list) - 1, 2):
        tmp = decrypted_list[idx + 1]
        decrypted_list[idx + 1] = decrypted_list[idx]
        decrypted_list[idx] = tmp


def add_to_evens(decrypted_list: list):
    """
    Add two to every even integer in a list.
    :param decrypted_list: A list of integers
    :return: None
    """
    for idx in range(len(decrypted_list)):
        if decrypted_list[idx] % 2 == 0:  # checks for even integer
            decrypted_list[idx] += 2


def left_circular_shift(decrypted_list: list):
    """
    Shift all integers in a list to the left by one. Left most integer gets placed at the end of the list
    :param decrypted_list: A list of integers
    :return: None
    """
    # similar to swap but does not skip any integers
    # pushes first integer to the end
    for idx in range(len(decrypted_list) - 1):
        tmp = decrypted_list[idx]
        decrypted_list[idx] = decrypted_list[idx + 1]
        decrypted_list[idx + 1] = tmp


def encrypting_numbers(decrypted_list: list):
    """
    Encrypt a copied list of integers in a certain order
    :param decrypted_list: A list of decrypted integers
    :return: List of encrypted integers
    """
    # Make a copy that can be changed without affecting original string
    encrypted_list = copy.deepcopy(decrypted_list)

    swap(encrypted_list)
    add_to_evens(encrypted_list)
    left_circular_shift(encrypted_list)
    swap(encrypted_list)

    return encrypted_list


# Testing
print(encrypting_numbers([4, 8, 15, 16, 23, 42]))

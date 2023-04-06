#!/usr/bin/python3

"""
    Function to determine the number of minmum operations 
    for a given n characters needed to the copied
"""


def minOperations(n):
    """
        A function to return the fewest number of operations
        needed to get result of exactly n H characters in a file
        args: n: number of characters to be displayed
        return:
               number of min operations
    """

    chars_in_file = 1
    clipboard = 0  # how many times chars (H's) copied
    counter = 0  # operations counter
    while chars_in_file < n:
        remainder = n - chars_in_file
        if (remainder % chars_in_file == 0):
            clipboard = chars_in_file
            chars_in_file += clipboard
            counter += 2
        else:
            chars_in_file += clipboard
            counter += 1
    return 

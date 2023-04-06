#!/usr/bin/python3

""" minmum operations for a given n characters"""


def minOperations(n):
    """
        perform the minimal number of operation        
        needed to get the result of exactly n H characters in a file
        args: n: number of characters
        return:
               number of minimun operations
    """

    char_file = 1
    n_copies = 0  # number of times (H's)is copied
    count = 0  # counter for the operation
    while char_file < n:
        rems = n - char_file
        if (rems % char_file == 0):
            n_copies = char_file
            char_file += n_copies
            count += 2
        else:
            char_file += n_copies
            count += 1
    return count

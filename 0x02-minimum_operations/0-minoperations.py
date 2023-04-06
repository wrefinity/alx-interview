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
    char_file = 1  # how many chars in the file
    copied = 0  # how many H's copied
    counter = 0  # operations counter

    while char_file < n:
        # if nothing is copied yet
        if copied == 0:
            # copyall
            copied = char_file
            #increment count
            counter += 1

        # if nothing is pasted yet
        if char_file == 1:
            # paste
            char_file += copied
            #incremnt count
            counter += 1
            # continue next loop
            continue

        rems = n - char_file  # the remainder of chars to Paste
        # check if impossible by checking if the clipboard
        # has more than needed to reach the number desired
        # This means that the number of chars in file is equal
        # or more than in the clipboard.
        # in both situations it's impossible to achieve n of chars
        if rems < copied:
            return 0

        # if it can't be divided
        if rems % char_file != 0:
            # paste current clipboard
            char_file += copied
            #increment count
            counter += 1
        else:
            # copyall
            copied = char_file
            # paste
            char_file += copied
            #increment count
            counter += 2

    # if the  desired result was obtained
    if char_file == n:
        return counter
    else:
        return 0

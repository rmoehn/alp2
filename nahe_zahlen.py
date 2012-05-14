#!/usr/bin/env python3.2
"""
From a list of numbers returns those two with the smallest difference (> 0)

If there is more than one pair with the same smallest difference, the one with
the smallest numbers is returned.

"""

from sorting import bsort
from sys import argv

def find_smallest_diff_pair(numbers):
    """
    Does exactly what the whole program does, on subroutine level

    """

    # Can only find pairs in lists with more than one element
    if len(numbers) < 2:
        return None

    # Sort input list
    numbers = bsort(numbers)
        # To many exercises to use and analyse a more efficient algorithm

    # Walk through adjacent numbers and determine least difference with flood
    # peak algorithm
    # Initialize flood peak with first pair
    least_difference_yet = numbers[1] - numbers[0]
    least_tuple_yet      = (numbers[0], numbers[1])
    for i in range(0, len(numbers) - 1):
        cur_difference = numbers[i+1] - numbers[i]

        # Update least pair and difference yet if smaller pair found
        if 0 != cur_difference < least_difference_yet:
            least_tuple_yet      = (numbers[i], numbers[i+1])
            least_difference_yet = cur_difference

    return least_tuple_yet


# If called as a program, work on the command line arguments
if __name__ == '__main__':
    print(
        find_smallest_diff_pair(
            list(map(
                float, # That's ok, I think.
                argv[1:]
            ))
        )
    )

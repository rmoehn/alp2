def find_abs_majority_elem_in(array):
    """
    Finds element with absolute majority of number occurrences in an array

    ...if it exists

    The absolute majority of the number of occurrences is reached, when the
    number of occurrences is at least (n/2 + 1) in an array of length n.

    Parameter: Array of immutable (dictionary keys) objects
    Rückgabe: the very element

    """

    # Initialise hash for storing the numbers of occurrences of the elements
    frequency_of = {}

    # Calculate threshold absolute majority
    abs_maj = len(array) // 2 + 1

    # Walk through the list and count elements
    for elem in array:
        # If element known already
        if elem in frequency_of:
            # Increment frequency
            frequency_of[elem] += 1

            # Check whether it has reached the absolute majority
            if frequency_of[elem] >= abs_maj:
                return elem

        # Create new entry if not known
        else:
            frequency_of[elem] = 1

    # All work and no play makes Jack a dull boy.
    return None

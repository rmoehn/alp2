import re

def gen_eq_suf_lists(string):
    """
    Group together words with the same last three characters

    From a string generates an array of arrays where words that share the
    last three characters are grouped together.

    """

    # Reverse the string
    string = string[::-1]

    # Split the string into list of sensible words and sort them
    words = re.split('\W', string)
    words = list(filter(lambda word : word != '', words))
    words.sort()

    # Initialise output list with an empty group
    suffix_groups = [ [] ]

    # Walk through words...
    cur_suffix = words[0][:3]
    for word in words:
        # Add word to last group if it has the same suffix
        if word[:3] == cur_suffix:
            suffix_groups[-1].append(word[::-1])

        # Make a new group on the encounter of a new suffix
        else:
            suffix_groups.append( [ word[::-1] ] )

            # Update the suffix that is compare with
            cur_suffix = word[:3]

    return suffix_groups

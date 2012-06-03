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


# Nein, es funktioniert nicht.
def radix_sort_words(words):

    cur_max_length = len(words[0])
    for word in words:
        if len(word) > cur_max_length:
            cur_max_length = len(word)

    for offs in range(cur_max_length - 1, -1, -1):
        print(offs)
        buckets = []

        for word in words:
            print('hallo')
            try:
                letterord = ord(word[offs])
            except IndexError:
                continue

            print(letterord)
            if letterord > len(buckets) - 1:
                # buckets += [[]] * (letterord - len(buckets) + 1)
                # Wer denkt sich diesen Scheiß aus? Eine Stunde um zu
                # verstehen, warum sich plötzlich alle Elemente verändern,
                # obwohl ich bloß auf eins zuweise!
                print(buckets)


            print(word)
            buckets[letterord].append(word)
            print(buckets)

        words = []

        for bucket in buckets:
            words.extend(bucket)

    return


#if __name__ == '__main__':
#    radix_sort_words(['abc', 'bac', 'acb', 'cba', 'cab', 'bca'])

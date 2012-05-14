#!/usr/bin/env python3.2
"""
Liest einen Text und bestimmt die Häufigkeiten der Wörter darin



"""

import sys
from re import split, sub

def read_words_from(filename):
    """
    Reads all sensible words from a file and puts them into an array

    That means, the text is stripped from whitespace and litter like
    punctuation marks or bad style. In the process all words are neatly put
    into an array. -- One word per index.

    Parameter: filename ... Name of the file with the important text
    Rückgabe: Array with all words.

    """

    # Read file into array of words
    text_file = open(filename, 'r')
    words = split('\s', text_file.read())

    # Initialize output array
    pure_words = []

    # Remove rubbish
    for word in words: # Not optimal, but other ways are not much better.
        # Discard puncuation marks
        word = sub('[;:(),.*]', '', word)

        # Discard words that were or have become empty
        if word == '':
            continue

        # Return the remaining
        pure_words.append(word)

    return pure_words


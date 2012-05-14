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
        # Discard everything that is not a 'word character'
        word = sub("[^\w]", '', word)

        # Discard words that were or have become empty
        if word == '':
            continue

        # Return the remaining
        pure_words.append(word)

    return pure_words


def build_freq_table_from(array):
    """
    Computes dictionary with the frequencies of the elements in an array

    """

    # Initialise array with frequencies
    frequency_of = {}

    # Walk through the elements of the array
    for elem in array:
        # Increment frequency of current element...
        if elem in frequency_of:
            frequency_of[elem] += 1
        # ...or set to zero on first occurrence
        else:
            frequency_of[elem] =  1

    return frequency_of


def sort_by_keys(dictionary):
    """
    Sorts a dictionary by its keys and returns list of (key, value)-tuples

    Brüder, verschließt die Augen vor dem Schmutz, der euch erwartet!

    """

    return list(reversed(mergesort_by_snd(tuplify(dictionary))))


def tuplify(dictionary):
    """
    Turns a dictionary into list of (key, value)-tuples

    """

    # Initialise list of tuples
    tuplelist = []

    # Do what I said!
    for key, value in dictionary.items():
        tuplelist.append( (key, value) )

    return tuplelist


def prettyprint_tuplelist(tuplelist):
    """
    Gibt eine Liste von (Schlüssel, Wert)-Tupeln als Tabelle aus

    """

    print(" {:<15s} | {:<10s} ".format("Wort", "Häufigkeit"))
    print("-----------------+------------")

    for (wort, haeufigk) in tuplelist:
        print(" {:<15s} | {:>10d} ".format(wort, haeufigk))
            # Longish words distort the table. However, they are seldom.


# Die folgenden Sortierfunktionen sind Kopien der Funktionen bsort und
# fancy_mergesort aus den ersten Aufgaben. Der Unterschied ist, dass sie
# Listen von Tupeln (oder Listen) entgegennehmen und nach jeweils dem zweiten
# Element in der Unterliste sortieren.
#
# Wenn wir nicht so viele Aufgaben bekommen hätten, hätte ich eine saubere und
# universelle Lösung programmiert.
#
# Wenn wir nicht gezwungen wären, ständig das Rad neu zu erfinden, hätte ich
# die eingebaute sorted()-Funktion benutzt, die komischerweise das gleiche
# kann und noch einiges mehr; und effizienter ist sie auch noch.

def bsort_by_snd(array, lower_ind=None, upper_ind=None):
    """
    Sortiert eine (Teil-)Liste in-place mit dem Bubblesort-Algorithmus

    """

    # If no bounds are given, sort the whole array
    if lower_ind == upper_ind == None:
        return bsort_by_snd(array, 0, len(array) - 1)

    # Loop as long as elements have been changed
    order_changed = True
    while order_changed:
        order_changed = False
            # Perhaps no change this time...

        # Walk through unsorted part of the list
        for i in range(lower_ind, upper_ind):
            # Exchange elements that are not in order
            if array[i][1] > array[i+1][1]:
                array[i], array[i+1] = array[i+1], array[i]

                # Something has changed...
                order_changed = True

        # This time's last element needs not be sorted any more
        upper_ind -= 1

    return array


# Mergesort
def mergesort_by_snd(array, lower_ind=None, upper_ind=None, buffer_ary=[]):
    """
    Sortiert eine Liste mit dem Mergesort-Algorithmus

    Dabei wird nur eine Hilfliste benutzt, die genau so groß wie die
    Eingabeliste ist. Außerdem werden Teillisten mit weniger als acht Element
    nicht gemergt, sondern mit Bubblesort sortiert.

    Parameter:
        array ... zu sortierende Liste
        lower_ind ... linker Index des zu sortierenden Bereichs
        upper_ind ... rechter Index des zu sortierenden Bereichs
        buffer_ary ... Array, das beim mergen als Puffer dient
    Rückgabe: (teilweise) sortierte Liste

    """

    # Work on the whole array if no arguments given
    if lower_ind == upper_ind == None:
        # Initialise buffer for merging
        buffer_ary = array[:]

        return mergesort_by_snd(array, 0, len(array) - 1, buffer_ary)

    # Sort smallish chunks with bubblesort
    if upper_ind - lower_ind < 8:
        return bsort_by_snd(array, lower_ind, upper_ind)

    # Sort halves of the current part separately/recursively
    middle_ind = lower_ind + (upper_ind - lower_ind) // 2
    array = mergesort_by_snd(array, lower_ind,      middle_ind, buffer_ary)
    array = mergesort_by_snd(array, middle_ind + 1, upper_ind,  buffer_ary)

    # Merge the sorted halves
    array = merge_by_snd(array, lower_ind, middle_ind + 1, upper_ind,
                         buffer_ary)

    return array


def merge_by_snd(array, lower_ind, middle_ind, upper_ind, buffer_ary):
    """
    Verschmilzt zwei sortierte Bereiche in einem Array

    Es entsteht ein großer sortierter Bereich.

    Dabei wird eine Hilfsliste verwendet, die zunächst eine Kopie der zu
    sortierendenen Liste ist. Auf diese Weise bleibt der Speicherverbrauch
    konstant.

    Parameter:
        array      ... Liste, in der Bereiche verschmolzen werden sollen
        lower_ind  ... Anfang des linken Bereichs
        middle_ind ... Anfang des rechten Bereichs/Ende des linken
        upper_ind  ... Ende des rechten Bereichs
        buffer_ary ... Array, in das gemergt wird und das dann wieder
                       zurückkopiert wird

    """

    # The smaller of the two first elements of the parts is written here
    buffer_ind = lower_ind

    # Boundary for processing of the lower part
    old_middle_ind = middle_ind

    # While there are elements in both parts
    while lower_ind < old_middle_ind and middle_ind <= upper_ind:
        # Place the smaller one of the first elements in the buffer
        if array[lower_ind][1] <= array[middle_ind][1]:
            buffer_ary[buffer_ind] = array[lower_ind]
            # Next element has to become first
            lower_ind += 1
        else:
            buffer_ary[buffer_ind] = array[middle_ind]
            middle_ind += 1

        # Next element has to be written at the index to the right
        buffer_ind += 1

    # If all elements of the upper part of the list are used up...
    if middle_ind > upper_ind:
        # ...put the remaining elements of the lower part in the buffer.
        buffer_ary[buffer_ind : buffer_ind + (old_middle_ind - lower_ind)] \
            = array[lower_ind : old_middle_ind]

    # If all elements of the lower part of the list are used up...
    elif lower_ind == old_middle_ind:
        # ...put the remaining elements of the upper part in the buffer.
        buffer_ary[buffer_ind : buffer_ind + (upper_ind - middle_ind) + 1] \
            = array[middle_ind : upper_ind + 1]

    else:
        raise Exception("Some mistake... (Very revealing, eh?)")

    # Return _copy_ of buffer elements. -- Reference would cause trouble.
    return buffer_ary[:]


# Run the whole read-freq-sort-print process if called as a program
if __name__ == "__main__":
    prettyprint_tuplelist(
        sort_by_keys(
            build_freq_table_from(
                read_words_from(sys.argv[1])
            )
        )
    )

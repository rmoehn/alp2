from random import seed, randint

def is_sorted(array):
    """
    Prüft, ob eine Eingabeliste korrekt aufsteigend sortiert ist

    Parameter: array ... sortierte (?) Liste
    Rückgabe: True / False

    Funktion für Faltung wäre ganz praktisch hier...

    """

    # Initialise 'former element' for first loop pass
    former_elem = array[0]

    # Loop over array elements
    for elem in array:
        # Überprüfe Einhaltung des Kriteriums für Sortiertheit einer Liste (!)
        if former_elem > elem:
            return False

        # Current element becomes former element of next cycle
        former_elem = elem

    return True


def random_list(my_seed=None):
    """
    Erzeugt eine Liste zufälliger Länge mit zufälligen Zahlen

    Parameter:
        [seed] ... für reproduzierbare Fehler
    Rückgabe:
        zzListe

    """

    # No harvest without tilling
    seed(my_seed)

    # Fill list of random length with random integers out of a random range
    randlist = []
    for index in range(randint(10, 100)):
        randlist.append(randint(randint(-500, 10), randint(10, 723)))
            # Obfuscation even in Python

    return randlist


# Quicksort
def qsort(array, lower_ind=None, upper_ind=None):
    """
    Sortiert eine (Teil-)Liste in-place mit dem Quicksort-Algorithmus

    Als Pivot-Element wird hier nicht jeweils das erste, sondern das mittlere
    Element einer Teilliste verwendet.

    Parameter:
        array ... zu sortierende Liste
        lower_ind ... linker Index des zu sortierenden Teils
        upper_ind ... rechter Index des zu sortiernden Teils

    """

    # On first call set proper parameters
    if upper_ind == lower_ind == None:
        qsort(array, 0, len(array) - 1)
        return array

    # As long as partial list length is not 1
    if lower_ind < upper_ind:
        # Partition current array part
        old_pivot_ind = partition_m(array, lower_ind, upper_ind)

        # Sort the partitions separately
        qsort(array, lower_ind,         old_pivot_ind - 1)
        qsort(array, old_pivot_ind + 1, upper_ind)

    return


def partition_m(array, lower_ind, upper_ind):
    """
    Sortiert eine (Teil-)Liste für den Quicksort-Algorithmus um

    Das mittlere Elemente der (Teil-)Liste wird als Pivot-Element gewählt und
    aller größeren Elemente dahinter, alle kleineren Elemente davor
    angeordnet.

    """

    # Move pivot element from the middle of the array to the front
    pivot_ind = lower_ind + (upper_ind - lower_ind) // 2
    pivot     = array[pivot_ind]
    array[lower_ind], array[pivot_ind] = array[pivot_ind], array[lower_ind]

    # Index of the element that is exchanged in exchange steps
    exch_ind = lower_ind

    # Walk through assigned part of the array
    for ind in range(lower_ind + 1, upper_ind + 1):
        # Move elements smaller than the pivot element to the front
        if array[ind] < pivot:
            exch_ind += 1
            array[ind], array[exch_ind] = array[exch_ind], array[ind]

    # Replace the pivot in the (new) middle
    array[lower_ind], array[exch_ind] = array[exch_ind], array[lower_ind]

    # Return boundary for subsequent calls
    return exch_ind


def bsort(array, lower_ind=None, upper_ind=None):
    """
    Sortiert eine (Teil-)Liste in-place mit dem Bubblesort-Algorithmus

    """

    # If no bounds are given, sort the whole array
    if lower_ind == upper_ind == None:
        bsort(array, 0, len(array) - 1)
        return

    # Loop as long as elements have been changed
    order_changed = True
    while order_changed:
        order_changed = False
            # Perhaps no change this time...

        # Walk through unsorted part of the list
        for i in range(lower_ind, upper_ind):
            # Exchange elements that are not in order
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

                # Something has changed...
                order_changed = True

        # This time's last element needs not be sorted any more
        upper_ind -= 1

    return array


def fancy_mergesort(array, lower_ind=None, upper_ind=None, buffer_ary=[]):
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

        return fancy_mergesort(array, 0, len(array) - 1, buffer_ary)

    # Sort smallish chunks with bubblesort
    if upper_ind - lower_ind < 8:
        return bsort(array, lower_ind, upper_ind)

    # Sort halves of the current part separately/recursively
    middle_ind = lower_ind + (upper_ind - lower_ind) // 2
    array = fancy_mergesort(array, lower_ind,      middle_ind, buffer_ary)
    array = fancy_mergesort(array, middle_ind + 1, upper_ind,  buffer_ary)

    # Merge the sorted halves
    array = merge(array, lower_ind, middle_ind + 1, upper_ind, buffer_ary)

    return array


def merge(array, lower_ind, middle_ind, upper_ind, buffer_ary):
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
        if array[lower_ind] <= array[middle_ind]:
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
        buffer_ary[buffer_ind : buffer_ind + (upper_ind - lower_ind) + 1] \
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


testlist = [14, 33, 89, 87, 68, 56, 40, 26, 96, 73]

if __name__ == '__main__':
    bla = [-413, -61, 82, 170, 372, -225, 110, 253, 408, 455, 118, 569, 127, -213, 31, 159, 75, -34, 1]
    print(fancy_mergesort(bla))

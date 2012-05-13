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
        return

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


def bsort(array):
    """
    Sortiert eine Liste in-place mit dem Bubblesort-Algorithmus

    """

    # Nothing is in the right place yet
    unsorted_end = len(array) - 1

    # Loop as long as elements have been changed
    order_changed = True
    while order_changed:
        order_changed = False
            # Perhaps no change this time...

        # Walk through unsorted part of the list
        for i in range(unsorted_end):
            # Exchange elements that are not in order
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

                # Something has changed...
                order_changed = True

        # This time's last element needs not be sorted any more
        unsorted_end -= 1

    return

testlist = [14, 33, 89, 87, 68, 56, 40, 26, 96, 73]

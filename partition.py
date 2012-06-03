from random import randint

def quicksort(A):

    def partition(low, high):
        middle = low + (high-low)//2            # we don't use the classic way to calculate the middle
                                                # of the subarrays (low + heigh)//2 to avoid integer
                                                # overflow with very large arrays. This is not a problem
                                                # in Python but in other languages.
        A[low], A[middle] = A[middle], A[low]   # We swap the middle element with the first element
        pivot = A[low]                          # and use this new first element as the pivot
        i = low
        for j in range(low+1,high+1):
            if ( A[j] < pivot ):
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i], A[low] = A[low], A[i]
        return i

    def qsort(low, high):
        if low<high:
            m = partition(low, high )
            qsort (low, m-1)
            qsort (m+1, high)

    qsort(0, len(A)-1)




def isSorted(A):
    """ Test if all numbers of A are sorted in ascending order """
    for i in range(len(A)-1):
        if A[i]>A[i+1]:
            return False
    return True

def gen_numbers(n):
    """ generate an array with n random numbers in the range 0 to 99 """
    return [randint(0,99) for i in range(n)]

def test_list_of_sort_algorithms (test_runs = 1,
                                  n = 10,
                                  sort_functions = [quicksort]):
    """ Test a List of sort-Algorithms using the isSorted function in an assert statement """
    print("\n Task 1-4 Sort-Algorithms ")
    A = gen_numbers(n)
    C = gen_numbers(2)
    D = gen_numbers(1)

    for sort in sort_functions:

        for i in range(test_runs):

            print("\n ", str(sort))
            B = A[:]
            print("input: ", B)
            sort(B)
            print("result:", B)
            assert isSorted(B)

            B = C[:]
            print("input: ", B)
            sort(B)
            print("result:", B)
            assert isSorted(B)

            B = D[:]
            print("input: ", B)
            sort(B)
            print("result:", B)
            assert isSorted(B)

            B = []
            print("input: ", B)
            sort(B)
            print("result:", B)
            assert isSorted(B)

test_list_of_sort_algorithms()

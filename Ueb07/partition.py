from random import randint

def quicksort(A):

    def partition(low, high):
        assert high - low >= 1 and len(A) > 0
        middle = low + (high-low)//2
        assert low <= middle <= high

        A[low], A[middle] = A[middle], A[low]
        pivot = A[low]
        i = low

        for j in range(low+1,high+1):
            assert low < j <= high and low <= i <= high
            if ( A[j] < pivot ):
                i += 1
                A[i], A[j] = A[j], A[i]
                assert A[i] < pivot

        A[i], A[low] = A[low], A[i]
        assert A[low] <= pivot and A[i] == pivot
        assert low <= i <= high

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

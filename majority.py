"""
Task 7

A majority element in an array A with n elements, appears at least n//2 + 1
times.  Our solution begins with the first element as a potencial majority
element and just counts repetitions, but each time a different element of the
current element occurs we decrement our counter.  If the counter = 0 we change
the potential majority element with this new element and counter = 1.

"""

def majority (A):
    """
    Given an array A of integer numbers, finds the number that occurs a
    majority of the time in the array (if it exists) and returns it.  If it
    doesn't exists returns None.

    """

    if A == []:  # there is no majority element in an empty array
        return None

    count = 0
    current = A[0]

    for new_elem in A:
        if new_elem == current:
            count += 1
        else:
            count -= 1
        if count == 0:
            current = new_elem
            count = 1

    """ now the current element is a majority element, if a majority exists
        We need to confirm that the current element is indeed the majority
        element.
        We just need to count the repetitions of the current element
    """
    count = 0

    for elem in A:
        if elem == current:
            count += 1

    if count > len(A) / 2:
        return current

    return None


def test_majority ():
    def test (A, expected):
        m = majority (A)
        print ("calculated=", m, "expected=", expected, m == expected)

    print("\n Task 7")
    print("Test majority function")
    test ([3, 3, 1, -4, 0, 3, 3, 3, 7, -5, 3, 3, -5, 3, -20, 25, 3], 3)
    test ([2,2,3,2,2,3,2,2,3,2,2,3,2,2,3,2,2,3,2,2,3,2,2,3,3,3,3], 2)
    test ([2,3,2,3,2,3,2,3,2,3,4,4,4,4,4,4], None)
    test ([2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3], None)
    test ([2,2,1,2,3,2,3,2,3], 2)
    test ([1, 2, 3], None)
    test ([], None)
    test ([1], 1)

test_majority ()

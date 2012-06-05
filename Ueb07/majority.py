def majority (A):
    if A == []:  # there is no majority element in an empty array
        return None

    count = 0
    current = A[0]

    assert len(A) > 0 and 0 <= count <= len(A)
    for new_elem in A:
        assert len(A) > 0 and 0 <= count <= len(A)
        if new_elem == current:
            count += 1
        else:
            count -= 1
        if count == 0:
            current = new_elem
            count = 1

    assert len(A) > 0 and 0 <= count <= len(A)

    count = 0

    for elem in A:
        if elem == current:
            count += 1

    if count > len(A) / 2:
        return current

    return None


def majority_while(A):
    if A == []:  # there is no majority element in an empty array
        return None

    count = 0
    current = A[0]

    ind = 0

    assert len(A) > 0 and 0 <= ind <= len(A) and 0 <= count <= len(A)
    while ind < len(A):
        assert len(A) > 0 and 0 <= ind <= len(A) and 0 <= count <= len(A)
        if A[ind] == current:
            count += 1
        else:
            count -= 1
        if count == 0:
            current = A[ind]
            count = 1

        ind += 1

    assert len(A) > 0 and 0 <= ind <= len(A) and 0 <= count <= len(A)

    count = 0

    for elem in A:
        if elem == current:
            count += 1

    if count > len(A) / 2:
        return current

    return None

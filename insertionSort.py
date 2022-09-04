def insertion_sort(A):
    """Returns sorted version of A
    Inputs:
    A -- The given list of entries.
    Returns:
    A -- The sorted version of A
    """
    if len(A) == 1:                             # checking if there are more than one element
        return A
    for i in range(1, len(A)):                  # Iterating over all the elements except the 0th one
        entry = A[i]
        for j in reversed(range(i)):            # running loop in reversed order
            if entry < A[j]:
                A[j+1] = A[j]
                A[j] = entry
    return A

def insertion_sort2(A):
    """Returns sorted version of A
    Inputs:
    A -- The given list of entries.
    Returns:
    A -- The sorted version of A
    """
    if len(A) == 1:                             # checking if there are more than one element
        return A
    for i in range(1, len(A)):                  # Iterating over all the elements except the 0th one
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j - 1], A[j] = A[j], A[j -1]
            j -=1
    return A




####
if __name__ == "__main__":
    A = [1,3,5,6,9,6,4,3,2,100,8,89,67,0,34,-1]
    print(insertion_sort2(A))
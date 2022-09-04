"""Module: Sort
Contains:
arraySort
"""
def arraySort(A: list) -> list:
    """Implements  Sort Alogrithm to sort a given array.
    Input:
    A -- A list of comparable numbers.
    Returns:
    A -- list of sorted numbers, in non decreasing order.
    """
    for k in range(1, len(A)):                  # start from the second element
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j -1]
            j -= 1
        A[j] = cur
    return A
            
        
######### ----------- Testing -------------- ##################
if __name__ == "__main__":
    A = [3,5,6,7,9,2,3]
    print(arraySort(A))
    B = []
    print(arraySort(B))
    C = [5]
    print(arraySort(C))

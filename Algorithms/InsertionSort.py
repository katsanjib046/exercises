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

# import positional list
import sys
sys.path.append('../')
from DataStructures.LinkedLists.doubleLinkedLists import *


def positionalListSort(L : PositionalList) -> PositionalList:
    """Sort PositionalList of comparable elements into non-decreasing order."""
    if len(L) > 1:
        marker = L.first()                  # point to the first element
        while marker !=  L.last():
            pivot = L.after(marker)         # next item called pivot
            value = pivot.element()
            if value > marker.element():    # already sorted
                marker = pivot              # New marker is the pivot
            else:
                walk = marker               # to compare with the lest element
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)    
            
        
######### ----------- Testing -------------- ##################
if __name__ == "__main__":
    pList = PositionalList()
    pList.add_first(3)
    pList.add_last(1)
    pList.add_before(pList.last(), 7)
    sortedpList = positionalListSort(pList)
    print(pList.first().element())
    print(pList.last().element())

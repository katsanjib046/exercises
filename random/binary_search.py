import random
def binary_search(data, target, low, high): #sequential serach is of O(n), binary search is log(n)
    """Implements binary search algorithm recursively to check if target is in the data, 
    within the interver[low,high] of index. Return True if target is found."""
    if low > high:
        return False # this means the search is exhausted
    mid = (low + high) // 2
    if data[mid] == target: # checking the mid-point
        return True
    elif target < data[mid]: #searching lower half
        low = low
        high = mid - 1
        return binary_search(data, target, low, high)
    else: # searchin upper half
        low = mid + 1
        high = high
        return binary_search(data, target, low, high)

if __name__ == "__main__":
    n = 100
    target = 10
    data = sorted([random.randint(1,1000) for i in range(n)])
    print(binary_search(data, target, 0, n))

    
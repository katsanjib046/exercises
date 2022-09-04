import time
import sys
sys.setrecursionlimit(3000)

def linear_sum(S, n):
    """Returns the sum of first n elements of a given list"""
    if n == 0:
        return 0
    return linear_sum(S, n - 1) + S[n - 1]

def binary_sum(S, start, stop):
    """Returns the sum the first stop elements of a given list using binary recursion algorithm"""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid  = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)




###
if __name__ == "__main__":
    n = 10
    p = 2000
    s = 10000
    S = list(range(s))
    total = 0
    for i in range(n):
        start = time.time()
        A = linear_sum(S, p)
        end = time.time()
        total += (end - start)

    print(f"Method 1:{A} {(total / n):.20f}")

    total = 0
    for i in range(n):
        start = time.time()
        A = binary_sum(S, 0, p)
        end = time.time()
        total += (end - start)

    print(f"Method 2:{A} {(total / n):.20f}")
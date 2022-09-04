import time
import random
def prefix_average1(S): #O(n^2)
    """Returns a list of prefix averages, A[j], for all j"""
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A

def prefix_average2(S): # O(n^2)
    """Returns a list of prefix averages, A[j], for all j"""
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j + 1]) / (j + 1)
    return A

def prefix_average3(S): # O(n)
    """Returns a list of prefix averages, A[j], for all j"""
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A

def prefix_average4(S): # O(n)
    """Returns a list of prefix averages, A[j], for all j"""
    n = len(S)
    A = [0] * n
    A[0] = S[0]
    for j in range(1,n):
        A[j] = (j * A[j-1] + S[j]) / (j + 1)
    return A

if __name__ == "__main__":
    S = [random.randint(1,100000) for i in range(20000)]
    total = 0
    n = 10
    for i in range(n):
        start = time.time()
        A = prefix_average1(S)
        end = time.time()
        total += (end - start)

    print(f"Method 1: {(total / n):.20f}")
    total = 0
    for i in range(n):
        start = time.time()
        A = prefix_average2(S)
        end = time.time()
        total += (end - start)

    print(f"Method 2: {(total / n):.20f}")
    total = 0
    for i in range(n):
        start = time.time()
        A = prefix_average3(S)
        end = time.time()
        total += (end - start)

    print(f"Method 3: {(total / n):.20f}")
    total = 0
    for i in range(n):
        start = time.time()
        A = prefix_average4(S)
        end = time.time()
        total += (end - start)

    print(f"Method 4: {(total / n):.20f}")
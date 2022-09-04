import time

def factorial(n):
    "Recursive implementation of factorial"
    if n == 0:
        return 1
    return n*factorial(n-1)

def factorial1(n):
    """Non-recursive implementation of factorial"""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    n = 3

    total = 0
    for i in range(n):
        start = time.time()
        A = factorial(900)
        end = time.time()
        total += (end - start)

    print(f"Method 1: {A}\n {(total / n):.20f}")

    for i in range(n):
        start = time.time()
        A = factorial1(900)
        end = time.time()
        total += (end - start)

    print(f"Method 2: {A}\n {(total / n):.20f}")
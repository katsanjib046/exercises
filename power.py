import time
import sys
limit = sys.getrecursionlimit()
print(limit) #usually this is 1000
sys.setrecursionlimit(1100)

def power(x, n):
    """Returns the nth power of x using recursion"""
    if n == 0:
        return 1
    return x * power(x, n - 1)

def power_eff(x, n):
    """Returns the nth power of x using recusion efficiently"""
    if n == 0:
        return 1
    partial = power_eff(x, n // 2)
    if n % 2 == 0:
        return partial * partial
    else:
        return x * partial * partial


#####
if __name__ == "__main__":
    n = 100
    x = 5

    total = 0
    for i in range(n):
        start = time.time()
        A = power(x, n)
        end = time.time()
        total += (end - start)
    print(f"Method 1: {A} {(total / n):.20f}")

    total = 0
    for i in range(n):
        start = time.time()
        A = power_eff(x, n)
        end = time.time()
        total += (end - start)
    print(f"Method 1: {A} {(total / n):.20f}")
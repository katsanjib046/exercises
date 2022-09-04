import time
def bad_fibonacci(n):
    """Implements recursive algorithm for fibonacci sequence which is not that good"""
    if n < 2:
        return n
    return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)

def good_fibonacci(n):
    """Implements recursive algorithm for fibonacci sequence which is good. Returns a pair of fibonacci numbers"""
    if n < 2:
        return (n,0)
    (a,b) = good_fibonacci(n - 1)
    return (a + b, a)

if __name__ == "__main__":
    n = 10
    p = 35

    total = 0
    for i in range(n):
        start = time.time()
        A = bad_fibonacci(p)
        end = time.time()
        total += (end - start)

    print(f"Method 1: {(total / n):.20f}")

    total = 0
    for i in range(n):
        start = time.time()
        A = good_fibonacci(p)
        end = time.time()
        total += (end - start)

    print(f"Method 2: {(total / n):.20f}")
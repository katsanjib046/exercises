import random
import time
def unique1(S):
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            if S[i] == S[j]:
                return False
    return True

def unique2(S):
    temp = sorted(S)
    for i in range(1,len(S)):
        if temp[i] == temp[i - 1]:
            return False
    return True


if __name__ == "__main__":
    S = [random.randint(1,100000) for i in range(1000)]

    n= 10

    total = 0
    for i in range(n):
        start = time.time()
        A = unique1(S)
        end = time.time()
        total += (end - start)
    print(f"Method 1:{A} {(total / n):.20f}")

    total = 0
    for i in range(n):
        start = time.time()
        A = unique2(S)
        end = time.time()
        total += (end - start)
    print(f"Method 1:{A} {(total / n):.20f}")
import random

def find(S, val):
    """Find the smalles index of val, if available, or else returns -1"""
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j
        j += 1
    return -1


if __name__ == "__main__":
    S = [random.randint(1,1000) for i in range(1000)]
    print(find(S,10))
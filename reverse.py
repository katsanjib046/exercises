def reverse(S, start, stop):
    """Reverses a given list S"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


if __name__ == "__main__":
    s = 100
    S = list(range(s))
    print(S)
    reverse(S, 0, s)
    print(S)

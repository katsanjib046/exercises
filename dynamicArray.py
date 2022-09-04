import sys

data = []

for k in range(25):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0: 3d}; Size = {1: 4d}".format(a,b))
    data.append(None)
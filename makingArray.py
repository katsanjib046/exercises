import ctypes                                           # provides low level array implementation

class DynamicArray:
    """A dynamic array akin to a simplified python list"""

    def __init__(self):
        """Create an empty array"""
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array

    def __len__(self):
        """Returns the number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k <= self._n:
            raise IndexError("invalid index")
        return self._A[k]                               # retrieve from array

    def append(self, obj):
        """Add object to the end of an array"""
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # double the capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                               # non-public utility
        """Resize internal array to capacity c"""
        B = self._make_array(c)                         # new bigger array
        for k in range(self._n):                        # for each existing value
            B[k] = self._A[k]
        self._A = B                                     # using the bigger array
        self._capacity = c

    def _make_array(self, c):                           # non-public utility
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()                 # using ctypes.py_object


if __name__ == "__main__":
    lst = DynamicArray()
    lst.append(1)
    lst.append(2)
    print(lst[1])



    
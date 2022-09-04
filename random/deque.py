# File: deque.py Implementing ADT for double ended queue
"""
Model: deque Implementing double ended queue using circular array"""

class Empty(Exception):
    """Empty class for raising error"""
    pass

class ArrayDeque:
    """Implementing doule ended queue using circular array"""
    DEFAULT_SIZE = 10                                           # fixing an initial size of the deque

    def __init__(self):
        """Initializing an abstract array."""
        self._data = [None] * ArrayDeque.DEFAULT_SIZE
        self._front = 0                                         # front of the deque
        self._size = 0                                          # size is kept zero at the beginning

    def __len__(self):
        """Returns the number of elements in the deque"""
        return self._size

    def is_empty(self):
        """Returns True if no elements in the deque, or else False"""
        return len(self) == 0

    def first(self):
        """Returns the first element of the deque for reference only without removing it"""
        return self._data[self._front]

    def last(self):
        """Returns the last element of the deque for reference only without removing it"""
        return self._data[((self._front + self._size - 1) % len(self._data))]       # modular arithmetic

    def _resize(self, cap):
        """Resizes the internal array so as to make its length cap"""
        old = self._data                                    # the original data
        self._data = [None] * cap                           # size is now cap
        walk = self._front                                  # this is the front
        for k in range(self._size):
            self._data[k] = old[(walk + k) % len(old)]      # keeping the elements in new array
        self._front = 0

    def add_first(self, e):
        """Add the element e to the first of deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))         # resize the array if it is full
        self._data[self._front - 1] = e
        self._front = (self._front - 1) % len(self._data)   # modular arithmetic
        self._size += 1

    def add_last(self, e):
        """Add the element e to the last of deque"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._front + self._size) % len(self._data)] = e        # modular arithmetic
        self._size += 1

    def delete_first(self):
        """Returns and deletes the first element"""
        if self.is_empty():
            raise Empty("Deque is empty")
        frontValue = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < (len(self._data) // 4):
            self._resize(len(self._data) // 2)
        return frontValue

    def delete_last(self):
        """Returns and deletes the last element"""
        if self.is_empty():
            raise Empty("Deque is empty")
        lastValue = self._data[(self._front + self._size - 1) % len(self._data)]
        self._data[(self._front + self._size - 1) % len(self._data)] = None
        self._size -= 1
        if 0 < self._size < (len(self._data) // 4):
            self._resize(len(self._data) // 2)
        return lastValue

############## Testing ###############
if __name__ == "__main__":
    D = ArrayDeque()
    D.add_last(5)
    D.add_first(3)
    D.add_first(7)
    print(D.first())
    print(D.delete_last())
    print(len(D))
    print(D.delete_last())
    print(D.delete_last())
    D.add_first(6)
    print(D.last())
    D.add_first(8)
    print(D.is_empty())
    print(D.last())

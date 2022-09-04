# File queue.py Implementing a queue
"""
Module: queue Implementation of a queue with list as internal storage. Using a finite list to implement it.
"""

class Empty(Exception):
    """If its empty, returns error"""
    pass                                # We don't want it to do anything specific

class ArrayQueue:
    """Gives a Queue that implements FIFO."""
    DEFAULT_SIZE = 10                   # Defining a defualt max size

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_SIZE   # an empty array
        self._front = 0                                 # the first in queue is set to 0
        self._n = 0                                     # length or size is set to 0

    def __len__(self):
        """Returns the number of elements in the Queue."""
        return self._n

    def is_empty(self):
        """Returns True if there are no elements, or else False"""
        return self._n == 0

    def first(self):
        """Returns the first element in queue without removing it.
        Raises error if its emepty"""
        if self.is_empty():
            raise Empty("Empty Queue")
        return self._data[self._front]

    def dequeue(self):
        """Returns and remove the first element in the queue.
        Raises error if its empty"""
        if self.is_empty():
            raise Empty("Empty Queue")
        front_val = self._data[self._front]
        self._data [self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._n -= 1
        if 0 < self._n < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return front_val

    def _resize(self, cap):
        """Resizes the internal list for queue to maximum capacity cap."""
        old = self._data                                    # saving the old list
        self._data = [None] * cap                           # New data with size cap
        walk = self._front                                  # keeping track of the front
        for k in range(self._n):
            self._data[k] = old[(walk + k) % len(old)]
        self._front = 0                                     # setting this to 0

    def enqueue(self, e):
        """Adds e at the end of queue. Resizes the queue if necessary"""
        if self._n == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._n) % len(self._data)
        self._data[avail] = e
        self._n += 1


############## Testing ############
if __name__ == "__main__":
    queue = ArrayQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.first())
    print(len(queue))
    print(queue.dequeue())
    print(queue.first())
    print(len(queue))
    print(queue.dequeue())
    print(len(queue._data))
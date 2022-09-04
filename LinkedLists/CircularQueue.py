class Empty(Exception):
    """Empty exception."""
    pass


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    #------------------ nested _Node Class -------------------------------
    class _Node:
        """Leight Weight, nonpublic class for storing a single linked node."""
        __slots__ = '_element', '_next'                     # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty Queue."""
        self._tail = None                                   # Will represent the tail of a queue
        self._size = 0                                      # number of queue elements

    def __len__(self):
        """Returns the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return but do not remove the element at the front of the queue.
        Raise an exception if the queue is impty.
        """
        if self.is_empty():
            raise Empty("Queue is Empty.")
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is Empty.")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next                    # Bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest                               # Pointing to itself
        else:
            newest._next = self._tail._next                     # Pointing to the next head
            self._tail._next = newest                           # old tail points to new node
        self._tail = newest                                     # new node becomes the tail
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next 


# -------------- Testing ----------------------
if __name__ == "__main__":
    cQueue = CircularQueue()
    cQueue.enqueue(1)
    print(cQueue.first())
    cQueue.enqueue(2)
    print(cQueue.first())
    print(cQueue.dequeue())
    print(cQueue.first())


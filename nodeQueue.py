class Empty(Exception):
    pass

class LinkedQueue:
    """FIFO Queue implementation using singly linked list"""

#------------ Nested _Node Class -----------------------
    class _Node:
        """Lightweight, nonpublic node for singly linked list"""
        def __init__(self, element, next):
            """Initializing a node"""
            self._element = element
            self._next = next

#--------------- Queue Methods -------------------------
    def __init__(self):
        """Empty Queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Returns the size"""
        return self._size

    def is_empty(self):
        """Returns true if Queue is empty, else False"""
        return self._size == 0

    def first(self):
        """Returns first element for reference without removing it"""
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of Queue.
        Raise exception if its empty
        """
        if self.is_empty():
            raise Empty("Queue is Empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

#------------- Check -------------------
if __name__ == "__main__":
    queue = LinkedQueue()
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.first())
    print(queue.dequeue())
    print(queue.dequeue())
    
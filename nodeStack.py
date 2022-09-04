class Empty(Exception):
    """To raise an exception for empty class"""
    pass

class LinkedStack:
    """LIFO stack implementation using linked node"""
    
    # -------------- Nested _Node class -----------------------
    class _Node:
        """A non-public class for node. Light Weight."""
        __slots__ = '_element', '_next'                   # streamlined memory usage
        def __init__(self, element, next):
            """Initializing node's field"""
            self._element = element
            self._next = next

    # -------------- Stack methods -------------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None                           # reference to empty head
        self._size = 0                              # size of empty stack

    def __len__(self):
        """Length of the stack"""
        return self._size

    def is_empty(self):
        """Returns True if size is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Returns the top element for reference, without deleting it.
        Raises an exception if empty."""
        if self.is_empty():
            raise Empty("Stack is Empty.")
        return self._head._element                      # top of the stack is the head

    def pop(self):
        """Returns and deletes the top element.
        Raises an exception if empty."""
        if self.is_empty():
            raise Empty("Stack is Empty.")
        headValue = self._head._element
        self._head = self._head._next                    # Bypass the former node
        self._size -= 1
        return headValue

# -------------- Testing --------------------
if __name__ == "__main__":
    ls = LinkedStack()
    ls.push(1)

    
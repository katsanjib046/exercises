class _DoublyLinkedBase:
    """A Base class providing a double linked list representation."""

    #------------- Node structure for Double Linked List --------------
    class _Node:
        """Lightweight, non-public class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'        # Streamline memory

        def __init__(self, element, prev, next):
            """Initializing node's field."""
            self._element = element
            self._prev = prev
            self._next = next

    # -------------- Implementing Doubly Linked List ---------------------
    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)             # Called Sentinal node
        self._trailer = self._Node(None, None, None)            # Called Sentinal node
        self._header._next = self._trailer                      # Conect the header and trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)          # Linking it to neighbors
        predecessor._next = newest
        sucessor._prev = newest                                 # neighbors linked to it
        self._size += 1

    def _delete_node(self, node):
        """Delete non-sentinal node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                                 # element to be returned
        node._prev = node._next = node._element = None          # deleting node
        return element



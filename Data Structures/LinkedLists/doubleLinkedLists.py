""" Module: doubleLinkedLists 
Implementation of a base for doubly linked list along with some of its application.
Consists of classes:
_DoublyLinkedBase
LinkedDeque
PositionalList
"""

######### --------- Empty Exception -------------------------##############
class Empty(Exception):
    """Raises an error when the lists are empty."""
    pass

######### -------- Base for Doubly Linked List -------------- ##############

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
        successor._prev = newest                                 # neighbors linked to it
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


############# ------------- Deque with a doubly linked list ----------------- ###################

class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list. Inhertance of the base class."""

    # Extra __init__ not required

    def first(self):
        """Returns but doesn't remove the first element."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        """Returns but doesn't remove the last item."""
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the end of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Removes and returns the first element of the deque.
        Raises an exception if it is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Removes and returns the last element of the deque.
        Raises an exception if it is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty.")
        return self._delete_node(self._trailer._prev)


############ ----- Testing --------- ##########################
if __name__ == "__main__":
    deque = LinkedDeque()
    print(deque.is_empty())
    deque.insert_first("a")
    deque.insert_last("b")
    print(len(deque))
    print(deque.delete_first())
    print(len(deque))
    print(deque.first())


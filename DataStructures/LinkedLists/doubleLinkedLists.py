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


########### ------- Positional List -------- #################
class PositionalList(_DoublyLinkedBase):
    """A sequential cotainer of elements allowing positional access."""

    #---------------- nested Position class --------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position."""
            return self._node._element

        def __eq__(self, other):
            """Return True of other is a postion representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)                      # Opposite of __eq__

    # ----------------------- utility method -------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container.")
        if p._node._next is None:
            raise ValueError("p is no longer valid.")
        return p._node

    # ---------------------- utility method --------------------------------
    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinal)"""
        if node is self._header or node is self._trailer:
            return None                                     # Boundaries
        else:
            return self.Position(self, node)                # other position

    # ---------------------- accessors -------------------------------------
    def first(self):
        """Return the first Position in the list """
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just before Position p."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # --------------- mutators -----------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the end of the list and return new position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into the list before Position p and return new position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into the list after Position p and return new position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value


    





############ ----- Testing --------- ##########################
if __name__ == "__main__":
    pList = PositionalList()
    print(f"Is empty? {pList.is_empty()}")
    print(f"Length = {len(pList)}")
    pList.add_first("a")
    pList.add_last("z")
    print(pList.first().element())
    pList.add_before(pList.last(), "y")
    print(pList.before(pList.last()).element())


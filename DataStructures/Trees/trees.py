from abc import ABCMeta, abstractmethod
# defining an abstract base class for trees

class Tree:
    """Abstract base class representing a tree structure"""

    #------------------- nested Position class -------------------
    class Position:
        """An abstraction representing the location of a single element"""

        @abstractmethod
        def element(self):
            """Return the element stored at this position"""
            pass

        @abstractmethod
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            pass

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not self == other

    #---------------------- abstract methods that concrete subclass must support -----------
    @abstractmethod
    def root(self):
        """Return Position representing the tree's root (or None if empty)"""
        pass

    @abstractmethod
    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        pass

    @abstractmethod
    def num_children(self, p):
        """Return the number of children that Position p has"""
        pass

    @abstractmethod
    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        pass

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree"""
        pass

    #----------------- Concrete methods implemented in this class -------------
    def is_root(self, p):
        """Return True if Position representing p represents the root of the tree"""
        return self.root == p

    def is_leaf(self, p):
        """Return True if Position p doesn not have any children."""
        return self.num_children == 0

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0

    


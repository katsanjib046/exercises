from abc import ABCMeta, abstractmethod #necessary imports
class Sequence(metaclass = ABCMeta):
    """Our own version of collections.Sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Return the jth item in the sequence"""

    def __contains__(self, value):
        """Return True if value found in sequence, or else False"""
        for j in range(len(self)):
            if self[j] == value:
                return True
        return False

    def index(self, value):
        """Returns the left most index at which a value is found, or raises ValueError"""
        for i in range(len(self)):
            if self[i] == value:
                return i
        raise ValueError("The value not found in Sequence")

    def count(self, value):
        """Returns the number of element equal to value"""
        k = 0
        for i in range(len(self)):
            if self[i] == value:
                k +=1 
        return k


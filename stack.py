# File stack.py Implements a python class for ADT stack called ArrayStack
"""
Implements ADT Stack using List.
Defines a class of excepton for empty stack.
"""

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """Defines Stack using list as inherent container."""
    def __init__(self):
        """Create an empty stack"""
        self._data = []                             # empty list as the container for stack

    def push(self,e):
        """Add element e as the top most element of the stack."""
        self._data.append(e)

    def __len__(self):
        """Returns the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Returns True if the stack is empty."""
        return len(self._data) == 0

    def pop(self):
        """Returns the top most element and removes it. 
        Raises error if it is empty."""
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data.pop()

    def top(self):
        """Returns the top most element without deleting it.
        Raises error if it is empty."""
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data[-1]
        
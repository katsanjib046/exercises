class Progression:
    """Iterator producing a generic progression
    By default it produces whole numbers 0, 1, 2, ...
    """
    def __init__(self, start= 0):
        """Initizlize the give value to the first iterated value"""
        self._current = start

    def _advance(self):
        """
        Update self._current to a new value
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, it means the end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise the StopIteration Error"""
        if self._current is None: # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current #current value
            self._advance() #preparing for next step
            return answer #return the current value

    def __iter__(self):
        """By convention, an iterator must return itself"""
        return self

    def print_progression(self,n):
        """Print the next n values of a progression"""
        
        print(" ".join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    """Defines sub-class of Arithmetic progression from the default progression class"""
    def __init__(self, increment = 1, start = 0):
        """Instance for the class with default start = 0 and increment = 1
        increment: step for increment
        start:      starting value
        """
        super().__init__(start) #initiating using the base class
        self._increment = increment

    def _advance(self):
        """
        Advances the progression with the increment
        """
        self._current += self._increment


class GeometricProgression(Progression):
    """Defines sub-class of Arithmetic progression from the default progression class"""
    def __init__(self, base = 1, start = 1):
        """Instance for the class with default start = 0 and base = 1
        base: step for base
        start: starting value
        """
        super().__init__(start) #initiating using the base class
        self._base = base

    def _advance(self):
        """
        Advances the progression with the base
        """
        self._current *= self._base

class FibonacciProgression(Progression):
    """Specializes the progression class to Fibonacci Progression"""
    def __init__(self, first = 0, second = 1):
        """Instance of the Fibonacci Progression
        first is the first one in the sequence and 
        second is the second one in the sequence
        """
        super().__init__(first)
        self._second = second

    def _advance(self):
        """Returns the next entry in the Fibonacci Sequence"""
        self._current, self._second = self._second, self._current + self._second

#### Testing ######
if __name__ == "__main__" : 
    print( "Default progression:" ) 
    Progression().print_progression(10)
    print( "Arithmetic progression with increment 5: ") 
    ArithmeticProgression(5).print_progression(10)
    print( "Arithmetic progression with increment 5 and start 2: ") 
    ArithmeticProgression(5, 2).print_progression(10)
    print( "Geometric progression with default base: ") 
    GeometricProgression().print_progression(10)
    print( "Geometric progression with base 3: ") 
    GeometricProgression(3).print_progression(10)
    print( "Fibonacci progression with default start values: ") 
    FibonacciProgression().print_progression(10)
    print( "Fibonacci progression with start values 4 and 6: ")
    FibonacciProgression(4, 6).print_progression(10)
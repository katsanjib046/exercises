class Vector:
    """Represents a vector in a multidimensional space"""
    def __init__(self,d):
        """Create d-dimensional zero vector"""
        self._coords = [0] * d

    def __len__(self):
        """Returns the dimension of a vector"""
        return len(self._coords)

    def __getitem__(self,j):
        """Returns the jth coordinate of a vector"""
        return self._coords[j]

    def __setitem__(self,j,val):
        """Set the jth coordinate equal to val"""
        self._coords[j] = val

    def __add__(self, other):
        """Adds two vectors self and the other"""
        if len(self) != len(other):
            raise ValueError("Two dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros of the necessary dimension
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if two vectors are same"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if two vectors are not equal"""
        return not self == other # relying on existing definitions of vectors

    def __str__(self):
        """Returns string representation of vector"""
        return "<" + str(self._coords)[1:-1] + ">" #[1:-1] is done so as not to include
                                                    # the brackets in the list


######### Testing ############
if __name__ == "__main__":
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    total = 0
    for entry in v: #implicit iteration via __len__ and __getitem__
        total += entry
    print(total)
    print(str(v))

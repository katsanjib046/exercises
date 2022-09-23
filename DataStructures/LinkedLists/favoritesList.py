from doubleLinkedLists import PositionalList

class FavoriteList:
    """List of elements ordered from most frequently accessed to least"""

    #------------- nested _item class ----------------------------
    class _item:
        __slots__ = '_value', '_count'                 # Streamline memory usage
        def __init__(self, e):
            self._value = e
            self._count = 0


    #-------------- non-public unitilities ---------------------
    def _find_position(self, e):
        """Search for element e and return its position (or None if not found)"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count"""
        if p != self._data.first():                         # Consider moving...
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:                 # Must shift forward
                while (walk != self._data.first() and
                       cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p)) 

    #---------------- public methods ---------------------------
    def __init__(self):
        """Create an empty list of favorites"""
        self._data = PositionalList()                       # will be list of _item instances

    def __len__(self):
        """Return number of entries on favorites list"""
        return len(self._data)

    def is_empty(self):
        """Return True if list is empty"""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count"""
        p = self._find_position(e)                          # try to locate existing element
        if p is None:
            p = self._data.add_last(self._item(e))          # if new, place at end
        p.element()._count += 1                             # always increment count
        self._move_up(p)                                    # consider moving forward

    def remove(self, e):
        """Remove element e from the list of favorites"""
        p = self._find_position(e)                          # try to locate existing element
        if p is not None:
            self._data.delete(p)                            # delete, if found

    def top(self, k):
        """Generate sequence of top k elements in terms of access count"""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()                           # element of list is _item
            yield item._value                               # report user's element
            walk = self._data.after(walk)

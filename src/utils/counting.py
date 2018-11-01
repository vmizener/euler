from collections import Counter

class NegativeCounter(Counter):
    """
    Same as a regular counter, but will do natural subtraction (resulting in negative counts)
    Removes multiset behavior!
    """
    def __sub__(self, other):
        result = self.copy()
        for key, val in other.items():
            result[key] -= val
        return result

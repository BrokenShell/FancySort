""" Creating Sortable Classes
To make a custom class Sortable all we need to do is implement the "less-than"
dunder method. This method should take one input (typically another object like
the one being defined) and return a boolean that indicates if this one is less
than the other one. This works with polymorphic hierarchies of classes not just
exact matches.
"""
from Fortuna import shuffle


# Edit ValueType class so that it is sortable.


class ValueType:

    def __init__(self, value: int):
        self.value = value

    def __lt__(self, other):
        """ This method makes this object sortable """
        return self.value < other.value

    def __repr__(self):
        return f"ValueType({self.value})"


if __name__ == '__main__':
    arr = [ValueType(i) for i in range(5)]
    shuffle(arr)
    sorted_arr = sorted(arr)
    print(arr)
    print(sorted_arr)

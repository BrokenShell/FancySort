def odd_before_even(value: int) -> bool:
    """ Returns False if the value is odd, and True if it is even. We can
    count on the natural ordering of Booleans to use this as a `key` parameter
    in either of the sort procedures. False is like 0, and True is like 1, so
    this means odd numbers will be placed at the front of the list. """
    return value % 2 == 0


arr_4 = [2, 9, 1, 8, 3, 7, 4, 6, 5]
arr_4.sort(key=odd_before_even)
print(arr_4)

""" If we want even numbers to be up front, then we have two choices. 
Either we can write a new function `even_before_odd` where we invert the logic,
or we can use `odd_before_even` with the `reverse=True` parameter """


def even_before_odd(value: int) -> bool:
    """ Returns True if the value is odd, and False if it is even. We can
    count on the natural ordering of Booleans to use this as a `key` parameter
    in either of the sort procedures. False is like 0, and True is like 1, so
    this means even numbers will be placed at the front of the list. """
    return value % 2 != 0


arr_4.sort(key=even_before_odd)
print(arr_4)

arr_4.sort(key=odd_before_even, reverse=True)
print(arr_4)

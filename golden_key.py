""" The Golden Key
The `key` parameter is a function, method or lambda that will serve as means to
convert un-sortable objects into sortable objects, on the fly. It can also be
used to sort items by unusual criteria, like sorting all odd numbers to the
front of a list.

Signatures
```Sorted: sorted(Iterable, key: Optional[Callable]) -> List```

```Sort: List.sort(key: Optional[Callable]) -> None```

```key: Callable(Any) -> Sortable```

A Sortable is any object that supports the less-than operator via a special
dunder method aka magic method. We'll see how to implement this magic method on
a custom class later in this workshop. """


# 1. Sort `items` by their lookup value
items = ["Sword", "Axe", "Hammer"]
lookup = {
    "Sword": 60,
    "Axe": 40,
    "Hammer": 20,
}
items.sort(key=lookup.get)
print(items)

# 2. Sort `user_data` by last_name, first_name and then age
user_data = [
    {"first_name": "John", "last_name": "Smith", "age": 42},
    {"first_name": "Jane", "last_name": "Smith", "age": 38},
    {"first_name": "Jane", "last_name": "Smith", "age": 17},
    {"first_name": "Jimmy", "last_name": "Smith", "age": 12},
    {"first_name": "Oscar", "last_name": "Addams", "age": 38},
]
user_data.sort(key=lambda x: (x["last_name"], x["first_name"], x["age"]), reverse=True)
print(user_data)

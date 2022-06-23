# Fancy Sort, DS Workshop - Step by Step


## 0. Introduction and Motivation
Let's say we have a list of users that we get from some database, and our job is to sort them. Sounds simple, right? The trick is that our manager wants us to sort first by one field then by another and so on without using Pandas. Maybe by age then last name then first name. Or if we're building a game it might be that we need to sort monsters by level then type or name. How do we do this elegantly and efficiently in "vanilla" Python?

This workshop will walk through a sophisticated sorting procedure using Python's builtin `sort` method and `sorted` function. This lesson is not so much about the underlying sorting algorithm, but rather how to use Python's builtin sorting tools to their ultimate potential. The star of the show is the `key` parameter. But we will also discuss how to build classes that produce instance objects that are sortable by default - without using the `key` parameter.


## 1. Sorted vs. Sort
In this step we'll introduce Python's builtin sorting tools: `sort` and `sorted`. They both will sort a list and they both support the `key` parameter, we'll come back to the `key` parameter later on. Sort and Sorted are very similar but have subtle distinctions that can be very important. Sort is a method on the list object, where Sorted is a free function. But this isn't the only difference. Sort will destructively alter the list it is called on, where Sorted will return a new sorted list, non-destructively.

In this context "destructive" does not mean the list may be deleted or items removed. It simply means rearranging the items in a list is a destructive operation. Nothing is deleted.

In our example it doesn't matter which one we use - altering the list is perfectly fine because nothing in the rest of the app is relying on the original order of the list. However, this is not always the case. Occasionally we'll need to produce a new sorted list and retain the original order. When the original order doesn't matter - the Sort method is preferred due to its lower memory requirements as it does the sorting "in-place" and doesn't make a copy where the Sorted function produces a copy and thus uses more memory. In either case the builtin sorting tools are considerably (several orders of magnitude) faster than anything we could write ourselves in Python.

Method: List.sort() - Modifies the list (Destructive)
Function: sorted(Iterable) - Returns a new sorted list from any iterable (Non-destructive)

### See `code/intro.py` for the code

### Check for Understanding
1. What are the similarities between Sort and Sorted?
2. What are the differences between Sort and Sorted?
3. What does destructive mean in this context? Does it mean items may be removed from the list?

## 2. The `key` Parameter
The `key` parameter is a function, method or lambda that will serve as means to convert un-sortable objects into sortable objects, on the fly. It can also be used to sort items by unusual criteria, like sorting all odd numbers to the front of a list.

### See `code/odd_before_even.py` for the code.

### Signatures
```Sorted: sorted(Iterable, key: Optional[Callable]) -> List```

```Sort: List.sort(key: Optional[Callable]) -> None```

```key: Callable(Any) -> Sortable```

Sortable is defined by any object that supports the less-than operator via a special dunder method aka magic method. We'll see how to implement this magic method on a custom class in the next step.

### Check for Understanding
1. What are the three types of Callables in Python?
2. What does the `reverse` parameter do in both Sort and Sorted?
3. What makes an object Sortable?

## 3. Sorting Un-sortable Class Objects
For this example we will sort a list of random Monsters. Each Monster has these fields: Level and Name, both fields are randomly generated. For this example we'll use a Lambda Callable for our `key` parameter, but it works the same way as if it was a function. The Callable may take a Sortable or Un-sortable object as input and returns a Sortable object as output. The sort procedure then uses this new Sortable object to do the sorting and produce the final order.

### See `code/monster_sort.py` for the code

### Check for Understanding
1. Is it possible to sort a list of un-sortable class objects without altering the class definition?
2. Is it possible to lexicographically sort a list on more than two fields?
3. True or False: If you have a list of un-sortable objects you must use the Sort method and not the Sorted function to sort those objects.

## 4. Sortable Custom Class
To make a custom class Sortable all we need to do is implement the "less-than" dunder method. This method should take one input (typically another object like the one being defined) and return a boolean that indicates if this one is less than the other one. This works with polymorphic hierarchies of classes not just exact matches.

*Talk a bit about Polymorphism if there are folks in the audience that need a refresher. You should also mention the many other magic methods that Python has to offer, and encourage them to dig deeper - designing magic methods is a valuable skill. You can also hint at an upcoming DS Workshop called Algebraic Data Types where we deep dive on why and how magic methods can be particularly useful for modeling mathematical data objects. One such object type that everyone should be familiar with is Python's `int` type. Explain how writing a Sortable Class is halfway to creating an Algebraic Data Type.*

### See `code/sortable_type.py` for the code

### Check for Understanding
1. How can we alter a custom class to make its instance objects Sortable.
2. Is it possible to sort a list containing more than one type?
3. What is the hallmark of an Algebraic Data Type?

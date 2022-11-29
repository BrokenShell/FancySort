# Fancy Sort Workshop

1. Sorted vs. Sort `introduction.py`
2. The Key Parameter `golden_key.py`
3. Sorting the Un-sortable `unsortable.py`
4. Sortable Custom Classes `sortable.py`

Let’s say we have a list of users that we get from some database, and our job is to sort them. Sounds simple, right? The trick is that our manager wants us to sort first by one field then by another and so on without using Pandas. Maybe by age then last name then first name. Or if we’re building a game it might be that we need to sort monsters by level then type or name. How do we do this elegantly and efficiently in “vanilla” Python? That is, without pandas.

This workshop will walk through a sophisticated sorting procedure using Python’s builtin sort method and sorted function. This lesson is not so much about the underlying sorting algorithm, but rather how to use Python’s builtin sorting tools to their ultimate potential. The star of the show is the key parameter. But we will also discuss how to build classes that produce instance objects that are sortable by default - without using the key parameter.

But first we'll have a little review to go over the differences and similarities between the list method `.sort()` and the free function `sorted()`.

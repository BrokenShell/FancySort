# Check For Understanding - Answers

### 1. CFU Answers
1. Sort and Sorted will both sort a list. They both support the `key` parameter. Both are built into Python and don't have dependencies. Both are faster than what we could write ourselves due to their low level implementation in C.
2. Sort is a method on the List object, where Sorted is a free function. Sort is destructive and Sorted is not. Sort can only be used on Lists, but Sorted can be used on any Iterable. The Sorted function generally uses more memory than the Sort method due to the fact that Sorted makes a copy of the data.
3. No, "destructive" does not mean items might be removed. It simply refers to rearranging the items in the list. Nothing is deleted - but in the end, it's not exactly the same list.

### 2. CFU Answers
1. Function, Method, Lambda
2. The `reverse` parameter, when set to True, reverses the order of a sort procedure in a more efficient way than reversing the order after running the sort procedure. This is only partially true due to Python's awesome handling of iterators. But that's a story for another time!
3. A Sortable object implements the "less-than" operator: `def __lt__(self, other) -> bool`. This means that the builtin `<` operator will work as it does with numbers or strings.

### 3. CFU Answers
1. Yes. One way is to define the `key` parameter with either of the sort procedures.
2. Yes. There is no hard limit to the number of fields used.
3. False. Both Sort and Sorted have the ability to support the `key` parameter.

### 4. CFU Answers
1. You can define the "less-than" magic method on the custom class. This method takes another object like this one as input and must return a boolean to indicate if this one should come first (True) or not (False).
2. Yes, but the objects must be polymorphic, and it should seem logical and feel natural to do this sorting. Just because we can, doesn't mean we should.
3. An object that supports Python's builtin mathematical operators such as +, -, *, /, //, % etc.

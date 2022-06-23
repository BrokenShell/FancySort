from Fortuna import shuffle


class ValueType:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"Value({self.value})"


class OtherValueType(ValueType):

    def __repr__(self):
        return f"OtherValueType({self.value})"


if __name__ == '__main__':
    print("Sorting Sortable Values")
    arr = [ValueType(i) for i in range(10)]
    shuffle(arr)
    sorted_arr = sorted(arr)
    print(arr)
    print(sorted_arr)
    print()
    print("Mixing Polymorphic Types")
    arr.append(OtherValueType(0))
    sorted_arr = sorted(arr)
    print(arr)
    print(sorted_arr)

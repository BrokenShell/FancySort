from Fortuna import shuffle


class Value:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"Value({self.value})"


if __name__ == '__main__':
    arr = [Value(i) for i in range(10)]
    shuffle(arr)
    sorted_arr = sorted(arr)
    print(arr)
    print(sorted_arr)

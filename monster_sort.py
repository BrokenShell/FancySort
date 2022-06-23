from random import randint, choice


class Monster:
    monster_names = (
        "Goblin",
        "Troll",
        "Ogre",
        "Giant",
        "Vampire",
        "Dragon",
    )

    def __init__(self):
        self.name = choice(self.monster_names)
        self.level = randint(1, 10)

    def __repr__(self):
        return f"Monster({self.name}, {self.level})"


if __name__ == '__main__':
    # How can we sort this list of random Monsters?
    monsters = [Monster() for _ in range(10)]
    print("Unsorted:")
    print(monsters)
    # print(sorted(monsters))  # Note: this doesn't work!

    print("Sorted by Level:")
    print(sorted(monsters, key=lambda x: x.level))
    print("Sorted by Name:")
    print(sorted(monsters, key=lambda x: x.name))

    # What if we want to sort first by level then within each level sort by name?
    print("Sorted by Level then Name:")
    print(sorted(monsters, key=lambda x: (x.level, x.name)))
    # The above example demonstrates that tuples are lexicographically sortable
    # The key parameter simply packages a tuple for us on the fly

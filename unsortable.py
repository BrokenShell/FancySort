""" Sorting the Unsortable
For this example we will sort a list of random Monsters. Each Monster has these
fields: Level and Name, both fields are randomly generated. For this example
we'll use a Lambda Callable for our `key` parameter, but it works the same way
as if it was a function. The Callable may take a Sortable or Un-sortable object
as input and returns a Sortable object as output. The sort procedure then uses
this new Sortable object to do the sorting and produce the final order. """
from Fortuna import random_int, random_value


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
        self.name = random_value(self.monster_names)
        self.level = random_int(1, 10)

    def __repr__(self):
        """ Repr is required for printing Monsters within a list """
        return f"Monster({self.name}, {self.level})"


if __name__ == '__main__':
    # Sort the Monsters list first by level then by name
    monsters = [Monster() for _ in range(10)]
    print(monsters)

from random import randint
from Fortuna import RandomValue, front_linear


class Monster:
    random_name = RandomValue((
        "Goblin",
        "Troll",
        "Ogre",
        "Giant",
        "Vampire",
        "Dragon",
    ), front_linear)

    def __init__(self):
        self.name = self.random_name()
        self.level = randint(1, 10)

    def __str__(self):
        output = (
            f"Name: {self.name}",
            f"Level: {self.level}",
            "",
        )
        return "\n".join(output)

    def __repr__(self):
        return f"Monster({self.name}, {self.level})"


if __name__ == '__main__':
    m = Monster()
    n = Monster()
    print(m)
    print([m, n])

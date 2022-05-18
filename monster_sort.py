from monsters import Monster

# How can we sort this?
monsters = [Monster() for _ in range(10)]
print(monsters)
# print(sorted(monsters))
print()
print(sorted(monsters, key=lambda x: x.level))
print()
print(sorted(monsters, key=lambda x: x.name))
print()
# What if we want to sort first by level then within each level sort by name?
print(sorted(monsters, key=lambda x: (x.level, x.name)))

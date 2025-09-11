# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# print()

# access set items
# set1 = {"orange", 2, 45, 67, 8.8}
# for i in set1:
#     print(i)
# print(45 in set1)

# add item in a set
# thisSet = {"aeiou", "vowels"}
# thisSet.add("consonent")
# print(thisSet)

# add items from another set into current set
# set2 = {"fruits", 'vehicles'}
# set3 = {"aplhabet"}
# set2.update(set3)
# print(set2)


# remove set items, remove() or discard()
set4 = {"upper", "lower", "middle", "left", "right"}
# set4.remove("left")
# print(set4)
# set4.discard("right")
# print(set4)
# set4.clear()
# print(set4)
# del set4
# print(set4)

# join sets
set5 = {8.9, 6.2, 90, "vehicle"}
set6 = {'cars', 'bike', 90, 6.2}
# finalSet = set5.union(set6)
# finalSet = set5.union(set4, set6)
# print(finalSet)
# set5.update(set6)
# print(set5)

# join a set and a tuple
# x = {'a', 'b', 'cd'}
# y = (1, 2, 32)
# z = x.union(y)
# print(z)

intersect = set5.intersection(set6)
print(intersect)

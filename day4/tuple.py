# A tuple is a collection which is ordered and unchangeable.

# tup1 = ('sunday', 'monday', 'tuesday', 23,4,56.7)
# tup1 = tuple(('sunday', 'monday', 'tuesday', 23,4,56.7))
# print(tup1)
# print(len(tup1))


# will give normal text as output
# tup2 = ("Krishna")
# tupple with only 1 element\
# tup2 = ("Kanha",)
# print(tup2)
# print(type(tup2))


# accesing tuple items
# print(tup1[5])
# print(tup1[-2])
# print(tup1[1:5])

# Tuples are unchangeable, meaning that you cannot change,
# add, or remove items once the tuple is created.

# to update tuple we can convert it to list , make changes
# and then again convert it to tuple
tup3 = ("Orange", 'Mango', "Chiku", "Lichi")
# l1 = list(tup3)
# l1[2] = 'watermelon'
# tuple(l1)
# print(l1)

# join two tuples
currTupple = (8, 9, 10, "fruit")
newTupple = ("mango",)
currTupple += newTupple
print(currTupple)

tup4 = (10, 9, 8, 7)
combineTuple = tup3 + tup4
print(combineTuple)

# When we create a tuple, we normally assign values to it.
# This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into
# variables.
# This is called "unpacking":
tup5 = (3, 4, 5, 6, 6, 2, 3, 4, 4, 5)
(red, green, yellow, orange) = tup4
print(red)
print(green)
print(yellow)
print(orange)
# using astrick(*) to make remaining elements as list
(red, green, *yellow) = tup5
print(red)
print(green)
print(yellow)


# tup6 = tup5*2
# print(tup6)


# count(), index()
print(tup5.count(4))
print(tup5.index(4))

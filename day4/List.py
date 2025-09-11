
l1 = ['cherry', 'banana', 'mango', 56, 7.8, 999, ['saturday', 'sunday']]
# accessing list elements
# print(l1[1])
# print(l1[6])
# print(l1[-1])

# # rangeof indexes
# print(l1[2:5])
# print(l1[:4])
# print(l1[3:])
# print(l1[-3:-1])

# check is item is present in list
# if 'mango' in l1:
#     print("'Mango' is present")

# change list item
# l1[1] = 'Guava'
# print(l1)
# l1[3:7] = ['lemon', 90, 82 ,9567.67]
# print(l1)

# using insert() function to insert without replacing
# insert takes two arguments , position and element to insert
l2 = [10, 67, 45.90, 'lemon', 'happy', 'sad']
# l2.insert(2, 'hello')
# print(l2)

# append() also use to add element take only element to insert as argument
# l2.append(45677)
# print(l2)

# To append elements from another list to the current list, use the extend()
# method.
# fruits = ['mango', 'lichi', 'watermelon']
# tropical = ['pomegranate', 'chiku']
# fruits.extend(tropical)
# print(fruits)


# remove items
# fruits.remove('lichi')
# print(fruits)

# remove from sepcified index
# fruits.pop(2)
# print(fruits)

# del keyword also use to remove using specific index and also whole list
# del fruits[0]
# The clear() method empties the list.


# list comprehension
fruits2 = ['cherry', 'mango', 'dragon fruit', 'papaya']
# newlist = []
# for x in fruits2:
#     if 'a' in x:
#         newlist.append(x)
# print(newlist)

# with list comprehension
#  syntax ,  newlist = [expression for item in iterable if condition == True]

# newlist = [x for x in fruits2 if 'a' in x]
# newlist = [x.upper() for x in fruits2]
# print(newlist)
# newlist2 = [x if x != 'mango' else 'orange' for x in fruits2]
# print(newlist2)


# sort()
numbers = [90, 1000, 16677, 45, 456, 788]
numbers.sort()
fruits2.sort()
print(numbers)
print(fruits2)
fruits2.sort(reverse=True)
print(fruits2)

# reverse(), copy()

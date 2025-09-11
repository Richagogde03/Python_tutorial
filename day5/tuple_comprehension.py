# numbers = [3, 9, 10, 45, 6.7, 35]
# squared_num = tuple(x**2 for x in numbers)
# print(squared_num)

# sq_num = (x**2 for x in range(1, 11))
# for i in range(6):
#     print(next(sq_num), end=" ")


# str1 = ['cherry', 'mango', 'watermelon', 'banana']
# upper = tuple(x.upper() for x in str1)
# print(upper)

# print()

# generator_exp = (x for x in range(10) if x % 2 == 0)
# even_num = tuple(generator_exp)
# print(even_num, end=" ")

# print()

# creating pairs using 2 list
# list1 = [1, 2, 3]
# list2 = ['apple', 'orange']
# generate_pairs = ((x, y) for x, y in zip(list1, list2))
# generate_tuple = tuple(generate_pairs)
# print(generate_tuple)


strings = ["man", "people", "fruits", "objects", "understanding"]
generate_exp = (len(s) for s in strings)
convert_tuple = tuple(generate_exp)
print(f"length of each element in given list is {convert_tuple}")

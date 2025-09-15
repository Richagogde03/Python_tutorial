from functools import reduce

# map que 1
# converting list of strings to list of integers
s = ['1', '2', '3', '4']
res1 = list(map(int, s))
print(res1)


# double the numbers of a list
def double(num):
    return num * 2


l1 = [2, 3, 4, 5]
res2 = list(map(double, l1))
print(res2)


# Que 3, map with lambda (same question as que2 but using lambda fn)
l2 = [3, 4, 5, 6]
res3 = list(map(lambda x: x ** 2, l2))
print(res3)


# Que 4, map() with multiple iterables
l3 = [8, 0, 6, 2]
l4 = [1, 7, 8, 4]
res4 = list(map(lambda x, y: x + y, l3, l4))
print(res4)

# Que5, converting string to upper case
fruits = ("carrot", "orange", "banana")
res5 = list(map(str.upper, fruits))
print(res5)


# que1, filter
def starts_with_a(word):
    return word.startswith("a")


l5 = ['apricot', 'apple', 'guava']
res6 = list(filter(starts_with_a, l5))
print(res6)


# Que2
def even(n):
    return n % 2 == 0


l6 = [10, 6, 7, 4, 2, 5]
res7 = list(filter(even, l6))
print(res7)


# que3 same as que 2 using lambda function
l7 = [4, 9, 10, 12, 46, 34, 19, 17]
res8 = list(filter(lambda x: x % 2 == 0, l7))
print(res8)

# Que4 filtering and transforming data using map and filter
# first filter even and then double it
l8 = [1, 2, 3, 4, 5, 9, 8, 10]
fil = filter(lambda x: x % 2 == 0, l8)
res9 = list(map(lambda x: x ** 2, fil))
print(res9)

# Que5 filtering strings
l9 = ["apple", "guava", "cherry", 'kiwi']
res10 = list(filter(lambda x: any(char in "aieou" for char in x), l9))
print(res10)


# Que1 reduce()
l10 = ["Aarohi", "Rathore", "Shukla"]
res = reduce(lambda x, y: x + " " + y, l10)
print(res)


# Que2. reduce with named function
def add(x, y):
    return x + y


l11 = [1, 2, 3, 4, 5]
res11 = reduce(add, l11)
print(res11)


# Que3. using reduce() with lambda function
l12 = [1, 2, 3, 4, 5]
res12 = reduce(lambda x, y: x*y, l12)
print(res12)


# Que4. using initializer also
l13 = [1, 2, 3, 4]
res13 = reduce(lambda x, y: x + y, l13, 10)
print(res13)

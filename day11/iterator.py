nums = [2, 3, 4, 5, 6]
it = iter(nums)

# it will print object of iterator
# print(it)

# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(next(it))

for i in it:
    print(i, end=" ")
print(type(it))

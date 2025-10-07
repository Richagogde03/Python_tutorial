# Sum of Elements
# very hard

def func(list1):
    count = 0
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            count = count + 1
    if count == 0:
        return len(list1)
    else:
        return len(list1) + count


print(func([[], [], []]))
print(func([[3], [2], [1, 2]]))
print(func([]))
print(func([[[]]]))
print(func([[1, 2], ["3"], ["F"]]))
print(func([[[[]]], [2], [[[[[[]]]]]]]))

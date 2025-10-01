# Finding Common Elements

def common_elements(list1, list2):
    common = []
    a = set(list1)
    b = set(list2)

    for i in a:
        if i in b:
            common.append(i)
    return common


print(common_elements([-1, 3, 4, 6, 7, 9], [1, 3]))
print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]))
print(common_elements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]))
print(common_elements([1, 2, 3, 4, 5], [10, 12, 13, 15]))

# Consecutive Numbers
# Create a function that determines whether elements in an array can be
# re-arranged to form a consecutive list of numbers where each number appears
# exactly once.

# cons([5, 1, 4, 3, 2]) ➞ True
# // Can be re-arranged to form [1, 2, 3, 4, 5]
# cons([5, 1, 4, 3, 2, 8]) ➞ False
# cons([5, 6, 7, 8, 9, 9]) ➞ False


def cons(list1):
    ans = []
    for i in list1:
        num = i
        if num+1 in list1:
            ans.append(True)
        else:
            ans.append(False)
    count = 0
    for i in ans:
        if i is not True:
            count += 1

    if count > 1:
        return False
    else:
        return True


print(cons([5, 1, 4, 3, 2]))
print(cons([5, 1, 4, 3, 2, 8]))
print(cons([5, 6, 7, 8, 9, 9]))
print(cons([-3, -2, -1, 1, 0]))

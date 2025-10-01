# Two Distinct Elements
# In each input list, every number repeats at least once, except for two.
# Write a function that returns the two unique numbers.
# Example :- return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

# medium

def return_unique(my_list):
    my_dict = {}
    for i in my_list:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    list2 = []
    for key, value in my_dict.items():
        if value == 1:
            list2.append(key)
    return list2


print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))

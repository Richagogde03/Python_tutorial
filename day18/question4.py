def lst_ele_sum(list1):
    ans = []
    for i in range(len(list1)):
        sum = 0
        for j in range(len(list1)):
            if i != j:
                sum += list1[j]
        ans.append(sum)
    return ans


print(lst_ele_sum([1, 2, 3, 2, 1]))
print(lst_ele_sum([1, 2]))
print(lst_ele_sum([1, 2, 3]))
print(lst_ele_sum([1, 2, 3, 4, 5]))
print(lst_ele_sum([10, 20, 30, 40, 50, 60]))

# All Pairs that Sum to Target
# Hard

def all_pairs(list1, sum):
    ans = []
    for i in range(len(list1)):
        for j in range(i):
            if list1[i] + list1[j] == sum:
                if list1[i] < list1[j]:
                    ans.append([list1[i], list1[j]])
                else:
                    ans.append([list1[j], list1[i]])
    return sorted(ans)


print(all_pairs([2, 4, 5, 3], 7))
print(all_pairs([5, 3, 9, 2, 1], 3))
print(all_pairs([4, 5, 1, 3, 6, 8], 9))

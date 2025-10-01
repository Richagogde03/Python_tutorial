# Mini Peaks
# Write a function that returns all the elements in an array that are strictly
# greater than their adjacent left and right neighbors.

# medium


def mini_peaks(list1):
    ans = []
    for i in range(1, len(list1) - 1):
        if list1[i] > list1[i-1] and list1[i] > list1[i+1]:
            ans.append(list1[i])
    return ans


print(mini_peaks([4, 5, 2, 1, 4, 9, 7, 2]))

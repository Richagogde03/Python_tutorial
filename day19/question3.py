from functools import reduce

# Hard
# Bridge Shuffle
# Create a function to bridge shuffle two lists. To bridge shuffle, you
# interleave the elements from both lists in an alternating fashion, like so:

# list1 = ["A", "A", "A"]
# list2 = ["B", "B", "B"]
# Shuffled List = ["A", "B", "A", "B", "A", "B"]
# List 1 = ["C", "C", "C", "C"]
# List 2 = ["D"]

# Shuffled List = ["C", "D", "C", "C", "C"]


def bridge_shuffle(list1, list2):
    ans = []
    length1 = len(list1)
    length2 = len(list2)
    max_lenth = 0
    min_length = 0

    if length1 > length2:
        max_lenth = length1
        min_length = length2
    else:
        max_lenth = length2
        min_length = length1

    for i in range(max_lenth):
        if length2 < length1:
            for j in range(min_length):
                ans.append(list1[j])
                ans.append(list2[j])
            ans.append(list1[min_length:max_lenth+1])
            break
        elif length1 < length2:
            for i in range(min_length):
                ans.append(list1[j])
                ans.append(list2[j])
            ans.append(list2[min_length:max_lenth+1])
            break
        else:
            ans.append(list1[i])
            ans.append(list2[i])

    flatten_list = reduce(lambda x, y: x + (y if isinstance(y, list) else [y]),ans, [])

    print(flatten_list)


bridge_shuffle(["A", "A", "A"], ["B", "B", "B"])
bridge_shuffle(["C", "C", "C", "C"], ["D"])
bridge_shuffle([1, 3, 5, 7], [2, 4, 6])

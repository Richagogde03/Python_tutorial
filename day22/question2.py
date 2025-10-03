# NUMBER PAIRS
# HARD

def number_pairs(string):
    l1 = string.split()

    numbers = [int(num) for num in l1[1:]]
    total_pairs = 0

    my_dict = {}
    for i in numbers:
        occ = numbers.count(i)
        my_dict[i] = occ
    print(my_dict)

    for value in my_dict.values():
        total_pairs += value // 2
    return total_pairs


print(number_pairs(" 1 2 1 2 1 3 2"))

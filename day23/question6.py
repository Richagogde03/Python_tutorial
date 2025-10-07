# Gauss's Addition
# Hard

def gauss(list1):
    list1 = sorted(list1)
    if len(list1) == 1:
        temp = list(range(1, list1[0]+1))
        return sum(temp)
    elif len(list1) == 2:
        temp = list(range(list1[0], list1[1]+1))
    return sum(temp)


print(gauss([100]))
print(gauss([5001, 7000]))
print(gauss([1975, 165]))
print(gauss([1800, 250]))

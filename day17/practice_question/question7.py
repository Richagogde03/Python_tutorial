# Given a number, return a list containing the two halves of the number. If
# the number is odd, make the rightmost number higher.

# Examples:-
# number_split(4) ➞ [2, 2]
# number_split(10) ➞ [5, 5]
# number_split(11) ➞ [5, 6]
# number_split(-9) ➞ [-5, -4]

def number_split(num):
    ans = []
    if num % 2 == 0:
        ans.append(num // 2)
        ans.append(num // 2)
    else:
        mid = num // 2
        ans.append(mid)
        ans.append((mid) + 1)
    return ans


# print(number_split(4))
# print(number_split(10))
print(number_split(11))
# print(number_split(-9))

# Create a function that takes a number as input and returns True if the sum of
# its digits has the same parity as the entire number.
# Otherwise, return False.

# parity_analysis(243) ➞ True
# # 243 is odd and so is 9 (2 + 4 + 3)

# parity_analysis(12) ➞ False
# # 12 is even but 3 is odd (1 + 2)

# medium

def check_even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


def check_sum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num //= 10
    if check_even_odd(sum):
        return True
    else:
        return False


def parity_analysis(num):
    if check_even_odd(num):
        if check_sum(num):
            return True
        else:
            return False
    else:
        if check_sum(num):
            return False
        else:
            return True


# print(parity_analysis(243))
# print(parity_analysis(12))
print(parity_analysis(3))

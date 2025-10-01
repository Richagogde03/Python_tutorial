import re

# Bitwise Operator to Check Odd,
# Regular Expression to Check Even

# hard


def is_odd(num):
    if num & 1 != 0:
        print("Number is odd!!")
    else:
        print("Number is not odd!!")


def is_even(num):
    text_match = r'[-]?[0-9]*(0|2|4|6|8)$'
    check = re.findall(text_match, num)

    if len(check) > 0:
        print("Yes, number is even")
    else:
        print("Not an even number!!")


is_odd(9)
is_odd(58)
is_even("12")
is_even("-99")
is_even("-98")

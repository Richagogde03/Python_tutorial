# 1st
# if condition
# num = 4
# if num%2 == 0:
#     print('EVEN')

# 2nd
# if else
# num = 17
# if num%2 == 0:
#     print("EVEN NUMBER")
# else :
#     print("ODD NUMBER")


# 3rd
# # if-elif-else
# x = 50
# if x % 2 == 0:
#     print(x, "is divisible by 2")
# elif x % 3 == 0:
#     print(x, "is divisible by 3")
# else:
#     print(x, "is not divisible by 2 and 3")


# Nested-if
# 4th
# i = 0
# if i != 0:
#     if i > 1 :
#         print("Positive Number")
#     elif i < 0 :
#         print("Negative Number")
# else :
#     print("Zero")


# 5th question
# ch = '42'
# if ch.isalpha():
#     if ch.lower() in ['a','i','o','u','e']:
#         print("Given Character is Vowel")
#     else:
#         print("Given Character is Consonent")
# else:
#     if ch.isdigit() :
#         print("Given Charater is Digit")
#     else :
#         print("Given Character is Special Character")


# 6th question
# n1 = '120'

# if n1.isdigit():
#     num = int(n1)
#     if num > 50 and num < 60:
#         print("Greater than 50 and less then 60")
#     elif num > 0 and num < 50:
#         print("Number is located anywhere between 1 to 50")
#     elif num > 70 and num < 100:
#         print("number is located anywhere between 70 to 100")
#     elif num >= 100 or num <= 0:
#         print("Number is outside the ranges 1-50, 51-59, or 71-99")
# else:
#     print("Input is not a numeric string.")

# 7th question
day = 'Monday'
month = '02'
year = '2000'

if day == "Monday":
    if month == "02":
        if year == "2000":
            print("all conditions satisfied")
else:
    print("Any condition is failed")

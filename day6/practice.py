# 2's table
# tableOf2 = [2*i for i in range(1, 11)]
# print(tableOf2)


# 2's table using f string
# tableOf2 = [f"2 * {i} = {2*i}" for i in range(1, 11)]
# print(('\n').join(tableOf2))


# reverse s number
# num = 12345
# rev = 0
# while num != 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print("Reversed Num =", rev)


# fibonacci series upto nth term
# a = 0
# b = 1
# for i in range(1, 10):
#     c = a + b
#     a = b
#     b = c
#     print(c, end=" ")


# perfect number
# number = 28
# sum = 0
# for i in range(1, number):
#     if number % i == 0:
#         sum = sum + i
# if sum == number:
#     print("The number is a perfect number")
# else:
#     print("The number is not a perfect number")


# code to check if two strings are anagram or not
# str1 = "listen"
# str2 = "silent"
# if len(str1) == len(str2):
#     print(f"{str1} and {str2} are not anagram")
# str1 = sorted(str1)
# str2 = sorted(str2)
# if str1 == str2:
#     print("String1 and String2 are anagrams")
# else:
#     print("String1 and Strings2 are not anagrams")


# check given string is palindrome or not
# str1 = 'nitin'
# rev = ''
# for i in str1:
#     rev = i + rev
# if rev == str1:
#     print("Palindrome string")
# else:
#     print("String is not palindrome")

# que 1
# num1 = int(input("Enter the number :"))
# if num1 < 0:
#     print("Negative Number")
# else:
#     print("Positive Number")


# que2
# num2 = int(input("Enter number :"))
# if num2 % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# que3
# num3 = int(input("Enter nth number for sum : "))
# sum = 0
# for i in range(1, num3+1):
#     sum += i
# print(f"Total = {sum}")


# Que4
# num4 = int(input("Enter first number : "))
# num5 = int(input("Enter second number : "))
# if num4 > num5:
#     print(f"{num4} is greater then {num5}")
# else:
#     print(f"{num5} is greater then {num4}")


# que5
# a, b, c = 20, 30, 10
# if a > b and a > c:
#     print(f"{a} is greater then {b} and {c}")
# elif b > c:
#     print(f"{b} is greater then {a} and {c}")
# else:
#     print(f"{c} is greater then {a} and {b}")


# Que6
# year = int(input("Entyer a year : "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 == 0):
#     print("Leap Year!!")
# else:
#     print("Ordinary Year!!")


# Que7
# num6 = int(input("Enter a number : "))


# def check_prime(num6):

#     if num6 <= 1:
#         return False
 
#     for i in range(2, num6):
#         if num6 % i == 0:
#             return False
#     return True


# if check_prime(num6):
#     print(f"{num6} is a prime number")
# else:
#     print(f"{num6} is not a prime number")


#  Que8 (prime number in a given range)
# num6 = int(input("Enter a number : "))


# def check_prime(num6):

#     if num6 <= 1:
#         return False

#     for i in range(2, num6):
#         if num6 % i == 0:
#             return False
#     return True


# def generate_prime(num6):
#     return [x for x in range(2, num6+1) if check_prime(x)]


# print("prime number between 1 to {num6} : ", generate_prime(num6))


#  Que9. sum of digits of a number
# number = input("Enter the number : ")
# sum = 0

# for i in number:
#     sum = int(i) + sum

# print(f"Sum of digit of the num {number} is :", sum)


# Que10 reverse of number
# num7 = input("Enter a number : ")
# temp = int(num7)

# string reverse
# for i in num7:
#     rev = i + rev
# print("Reversed =", rev)

# rev = 0
# while temp != 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10
# print("Reversed number :", rev)


# Que11 palindrome number
num8 = input("Enter a number : ")
temp = int(num8)
rev = 0
while temp != 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if rev == int(num8):
    print(f"{num8} is a palindrome number!")
else:
    print(f"{num8} is not a palindrome number!")


# Que12 armstrong number


# printing num from 1 to 10
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1

print()

# printing even numbers bet 1 to 20
# i = 2
# while i <= 20:
#     print(i, end=" ")
#     i += 2

# printing even numbers bet 1 to 20, 2nd method
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print()

# sum of numbers
i, total = 1, 0
while i <= 11:
    total += i
    i += 1
print("sum = ", total)

print()

# reverse a number
num = 12123
rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number :-", rev)

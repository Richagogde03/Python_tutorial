# break statement
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# print()

# arr = [10, 20, 90, 67, 45, 34, 28]
# for i in arr:
#     if i == 45:
#         print("Condition met !! Exiting the loop")
#         break
#     print(i, end=" ")

# print()


# searching a value
# We use enumerate() when we want to loop through an iterable
# (like a list, tuple, or string) and need
# both the index (position) and the value of each item in the iterable.
# num = [45, 89, 25, "cherry", 90, 8.90]
# val = 25
# for index, i in enumerate(num):
#     if i == val:
#         print(f"value found at index {index}")
#         break
#     else:
#         print(f"value not found at index {index}")


# using while loop
cnt = 6
while True:
    print(cnt)
    cnt -= 1
    if (cnt == 0):
        print("Countdown finished!! Existing the loop now.")
        break

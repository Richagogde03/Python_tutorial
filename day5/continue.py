# for i in range(1, 11):
#     if i == 6:
#         continue
#     print(i, end=" ")

# print()

# for char in "Best Peers":
#     if char == "e" or char == " ":
#         continue
#     print(char, end="")

# print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for col in row:
        if col == 3:
            print(f"found {col}, thats why skipping the iteration")
            continue
        else:
            print(col, end=" ")

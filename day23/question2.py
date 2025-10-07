# Matrix Subtraction
# hard

def subtract_matrix(mat1, mat2):

    rows = len(mat1)
    cols = len(mat1[0])
    ans = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            ans[i][j] = mat1[i][j] - mat2[i][j]
    return ans


print(subtract_matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
))
print(subtract_matrix(
    [[21]],
    [[63]]
))
print(subtract_matrix(
    [
     [1, 2],
     [4, -5]
    ],
    [
     [2, 2],
     [4, -5]
     ]
))

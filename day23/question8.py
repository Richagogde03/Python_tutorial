# Enter the Matrix
# medium

def transpose_matrix(mat):
    l_row = len(mat)
    l_col = len(mat[0])
    ans = ""
    transposed = [[0 for _ in range(l_row)] for _ in range(l_col)]
    for i in range(l_row):
        for j in range(l_col):
            transposed[j][i] = mat[i][j]
    # print(transposed)
    for row in transposed:
        ans += " ".join(row) + " "
    # print(type(ans))
    # print(ans)
    return ans


print(transpose_matrix([
    ["Enter"],
    ["the"],
    ["Matrix!"]
]))
print(transpose_matrix([
  ["The", "are"],
  ["columns", "rows."]
]))
print(transpose_matrix([
  ["You", "the"],
  ["must", "table"],
  ["transpose", "order."]
]))

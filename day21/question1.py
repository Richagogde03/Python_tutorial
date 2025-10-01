# Is it a Probability Matrix?
# medium

def is_prob_matrix(mat1):
    num_rows = len(mat1)
    num_cols = len(mat1[0]) if num_rows > 0 else 0
    for i in range(len(mat1)):
        sum = 0
        for j in range(len(mat1)):
            if mat1[i][j] < 0 or mat1[i][j] > 1:
                return False
            elif num_rows != num_cols:
                return False
            sum += mat1[i][j]
        if sum != int(1):
            return False
    return True


print(is_prob_matrix([
    [0.5, 0.5, 0.0],
    [0.2, 0.5, 0.3],
    [0.1, 0.2, 0.7]
]))
print(is_prob_matrix([
  [0.5, 0.5, 0.0],
  [0.2, 0.5, 0.3]
]))
print(is_prob_matrix([
  [2, -1],
  [-1, 2]
]))
print(is_prob_matrix([
  [0, 1],
  [1, 0]
]))
print(is_prob_matrix([
  [0.5, 0.4],
  [0.5, 0.6]
]))

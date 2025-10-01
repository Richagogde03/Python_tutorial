
# medium
# You are given a list of scores. The even-indexed numbers are your scores at
# each turn.
# The odd-indexed numbers are your opponent's scores.
# Create a function that turns this list of scores into a list of who
#  is currently winning.

# To illustrate (You - Y, Opponent - O):

def currently_winning(list1):

    y_score = []
    x_score = []
    result = []

    for i in range(len(list1)):
        if i % 2 == 0:
            y_score.append(list1[i])
        else:
            x_score.append(list1[i])

    cumulative_score_x = []
    cumulative_score_y = []
    current_sum_x = 0
    current_sum_y = 0

    for i in x_score:
        current_sum_x += i
        cumulative_score_x.append(current_sum_x)

    for i in y_score:
        current_sum_y += i
        cumulative_score_y.append(current_sum_y)

    my_dict = {x: y for x, y in zip(cumulative_score_x, cumulative_score_y)}
    # print(my_dict)

    for x, y in my_dict.items():
        if x > y:
            result.append("O")
        elif x < y:
            result.append("Y")
        else:
            result.append("T")

    return result


# ans = currently_winning([5, 15, 17, 35, 16, 40, 66, 12, 10, 9])
# ans = currently_winning([5, 1, 2, 10])
ans = currently_winning([10, 10, 5, 5, 2, 2, 1, 3, 100, 5])
print(ans)

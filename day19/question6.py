# Building a Pie Char
# HARD

def pie_chart(my_dict):
    sum = 0
    for value in my_dict.values():
        sum += value
    my_dict2 = {}
    each_part = 360/sum
    mult = 1
    for key, value in my_dict.items():
        mult = each_part * value
        if mult % 1 == 0:
            my_dict2[key] = int(mult)
        else:
            my_dict2[key] = round(mult, 1)
    print(my_dict2)


pie_chart({"a": 1, "b": 2})
pie_chart({"a": 30, "b": 15, "c": 55})
pie_chart({"a": 8, "b": 21, "c": 12, "d": 5, "e": 4})

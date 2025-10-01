# ABACABADABACABA
# medium


def my_func(string):
    ans = ""
    alphabet = ["A", "B", "C", "D", "E", "F"]
    for i in alphabet:
        ans = ans + i + ans
        if i == string:
            break

    return ans


print(my_func("A"))
print(my_func("B"))
print(my_func("C"))
print(my_func("D"))
print(my_func("E"))

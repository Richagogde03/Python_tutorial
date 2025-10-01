# double character swap

# Write a function to replace all instances of character c1 with character c2
# and vice versa.
# Examples:-
# double_swap("aabbccc", "a", "b") ➞ "bbaaccc"
# double_swap("random w#rds writt&n h&r&", "#", "&")
# ➞ "random w&rds writt#n h#r#"
# double_swap("128 895 556 788 999", "8", "9")
# ➞ "129 985 556 799 888"

# medium


# method 1
# def double_swap(string, char1, char2):
#     temp_holder = "?"
#     string = string.replace(char1, temp_holder)
#     string = string.replace(char2, char1)
#     string = string.replace(temp_holder, char2)

#     return string


# 2nd method
def double_swap(string, char1, char2):
    ans = ""
    for i in string:
        if i == char1:
            ans += char2
        elif i == char2:
            ans += char1
        else:
            ans += i
    return ans


print(double_swap("aabbccc", "a", "b"))

# Missing letters
# medium

def get_missing_letters(string):
    list1 = ["a", "b", "c", "d", "e", "f", "g",
             "h", "i", "j", "k", "l", "m", "n"
             "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z"]
    remaining = ""
    for i in list1:
        if i in list1 and i in string:
            continue
        else:
            remaining += i
    return (f'"{remaining}"')


print(get_missing_letters("abcdefgpqrstuvwxyz"))
print(get_missing_letters("zyxwvutsrq"))
print(get_missing_letters("abc"))
print(get_missing_letters("abcdefghijklmnopqrstuvwxyz"))

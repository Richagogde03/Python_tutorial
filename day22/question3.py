# All About Strings
# medium

def all_about_strings(string):
    length = len(string)
    first = string[0]
    last = string[length-1]
    ans = []
    middle = ""
    if length % 2 == 0:
        middle = string[length // 2-1: (length // 2) + 1]
    else:
        middle = string[length // 2]

    ans.append(length)
    ans.append(first)
    ans.append(last)
    ans.append(middle)
    char2 = string[1]

    if char2 in string[2: length+1]:
        index = string.index(char2, 2)
        ans.append(f"@ index {index}")
    else:
        ans.append("not found")

    print(ans)


all_about_strings("LASA")
all_about_strings("Computer")
all_about_strings("Science")
all_about_strings('programming')
all_about_strings('bad')
all_about_strings('homework')

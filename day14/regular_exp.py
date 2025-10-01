import re

# 1. To check if a string starts with a specific
#  pattern using regular expressions?
# text = "Hello World"
# pattern = r"^Hello"
# match1 = re.search(pattern, text)

# if match1:
#     print("Pattern is found!!")
# else:
#     print("Pattern not found!!")


# 2. To find all occurrences of a pattern in a string and
# return them as a list?
# text = "apple banana apple orange"
# pattern = r"apple"
# all_matches = re.findall(pattern, text)
# print(all_matches)


# 3. To match one or more occurrences of a preceding character or
# group in a regular expression?
# text1 = "aaab"
# pattern = r"a+"
# match2 = re.search(pattern, text1)
# print(match2.group())


# 4.to find all occurence of a string or char in a strig literal
# we use finditer (it is a match object)
text2 = "Hello people Hello byee hii Hello"
match3 = re.finditer(r"Hello", text2)
for match in match3:
    print(match)
    print(match.span())

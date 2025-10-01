import re

# """First character uppercase, contains lower case aplhabets, only one
# digit allowed in betwwen"""


str1 = input("Enter a pattern : ")
pattern = r"[A-Z][a-z]*[0-9][a-z]*"
if re.match(pattern, str1):
    print("It is a valid pattern!!")
else:
    print("Not a valid string!!")

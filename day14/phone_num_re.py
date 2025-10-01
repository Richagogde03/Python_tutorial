import re

pattern = r'[+][9][1][" "][89][0-9]{9}'
a = input("Enter number : ")

if re.match(pattern, a):
    print("Valid Number.")
else:
    print("Not a valid number.")

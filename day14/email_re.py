import re

email = input("Enter your email to validate :- ")
re_email = r"[a-z A-z 0-9 _ \- \.]+[@][a-z]+[\.][a-z]{2,3}"

if re.match(re_email, email):
    print("It is a valid email!!")
else:
    print("Not a valid email!!")

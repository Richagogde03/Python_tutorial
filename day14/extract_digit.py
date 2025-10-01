import re

text = """The price is $12.90, there are 5 items . i think we should
take 3 for $10"""

# it will give list of digits
digits = re.findall(r"\d", text)
digits2 = re.findall(r"\d+", text)
print(digits)
print(digits2)

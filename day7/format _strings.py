# age = 36
# text = f"My name is john, my age is {age}"
# print(text)


# placeholders and modifiers in string
# price = 45
# txt = f"The price is {price : .2f} Rs"
# print(txt)
# text2 = f"The price and discount is {price}, {price * 0.25}"
# print(text2)


# if-else in f string
# price2 = 55
# text3 = f"It is very {'Expensive' if price2 > 50 else 'cheap'}"
# print(text3)


# function in fstring
# fruits = "mango"
# text4 = f"I Love {fruits.upper()}"
# print(text4)


# user defined function in fstring
# def convert(x):
#     return x * 0.3048


# text5 = f"The plane is flying at a {convert(30000)} meter altitude"
# print(text5)


# More modifiers use a comma as a thousand seprator
# price3 = 59000
# text6 = f"The price is {price3 : ,} dollars"
# print(text6)


# using string format()
price4 = 112
text7 = "The price is {} dollars"
print(text7.format(price4))

# if we have multiple values to insert
quantity = 3
itemno = 567
price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# we can use index numbers to insert value at correct position
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# also use named indexes
myorder = "I have a {carname}, of model {model}."
print(myorder.format(carname="Ford", model="Mustang"))

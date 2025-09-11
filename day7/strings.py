# a = "hello"
# print(a)


# multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# accesing elements of strings
a = "Hello, World!"
# print(a[3])
# for i in a:
#     print(i, end="")
# print()
# print(len(a))
# text = "The best things in life are free!"
# print("free" in text)
# print("Hello" not in text)


# slicing in string
# b = "Hello people of indore"
# print(len(b))
# print(b[2:15])
# print(b[:22])
# print(b[1:])
# print(b[-13:-1])


# modify strings
str1 = "   Hey, Friends   "
# print(str1.upper())
# print(str1.lower())
# remove white space
# print(str1.strip())
# print(str1.replace("H", "8"))


# splitting in string
str2 = "Hellooo, byee, bye-bye"
# print(str2.split())
# print(str2.split(", "))

# string concatination
# a1 = "bye"
# a2 = "bye"
# a3 = a1 + " " + a2
# print(a3)


# join method
# myTuple = ("peter", "henry", "john")
# myTuple2 = (90, 78)
# myTuple3 = "#".join(myTuple)
# print(myTuple3)
# print("*".join("myTuple"))

# will give error because join() is a string method not tuple method
# print(myTuple.join(myTuple2))
# myList = ["peter", "john", "henry"]
# myList2 = [67, 78]

# will give error because join() is a string method not List method
# print(myList.join(myList2))
# using in dictionery elements
myDict = {
    "name": "john", "country": " Norway"
}

mySeparator = "#"
x_keys = mySeparator.join(myDict)
# will give key values of dictionary separated with the separator
# print(x_keys)
# x_values = mySeparator.join(myDict.values())
# print(x_values)

# combined keys and values
combined_dict = [f"{key} : {value}" for key, value in myDict.items()]

# print(combined_dict) , will give list
# x_dict_items = mySeparator.join(combined_dict)

# will give error
# x_dict_items = mySeparator.join(myDict.items())
# print(x_dict_items)
# print(mySeparator.join(f"{key} : {value}" for key, value in myDict.items()))


# formate strings
age = 36
text = f"My name is john, my age is {age}"
# print(text)
# placeholders and modifiers in string
price = 45
txt = f"The price is {price : .2f} Rs"
# print(txt)
text2 = f"The price and discount is {price}, {price * 0.25}"
# print(text2)


# escape characters in string
text3 = "Hello from \"Indore\""
# print(text3)

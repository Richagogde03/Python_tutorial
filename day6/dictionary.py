# create and print dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict["brand"])
# print(type(thisdict))


# dict1 = dict(name="John", age=78,
#              country='Norway')
# print(dict1)


# Accessing dict items
# print(thisdict["model"])
# x = thisdict.get("brand")
# print(x)


# all items of dictionary
# The items() method will return each item in a dictionary,
# as tuples in a list.
# print(thisdict.items())

# change dictionary items
dict0 = {
    'fname': 'priya',
    'lname': 'singh',
    'age': 45,
    'address': "indore"
}
# dict0['age'] = 50
# print(dict0)

# update() dictionary
# dict0.update({'age': 45})
# print(dict0)


# adding items
# dict1 = {
#     "firstname": "john",
#     "lastname": "doe",
#     'DOB': 1986
# }
# dict1["fav_color"] = "red"
# print(dict1)

# removing items
dict2 = {
    "fruit": "orange",
    "vehicle": "bike",
    "color": "yellow",
    "game": "basketball"
}
# dict2.pop("color")
# print(dict2)

# popitem() method removes the last inserted item
# dict2.popitem()
# print(dict2)


# loop through dictionary
# for key, value in dict2.items():
#     print(key, ":", value)
# print()
# get keys() :-
# print(dict2.keys())
# for x in dict2:
#     print(x)
# print()
# get values() :-
# print(dict2.values())
# for x in dict2:
#     print(dict2[x])
# print()
# for x, y in dict2.items():
#     print(x, y)


# copy a dictionary
# dict3 = {
#      "brand": "kylie-cosmetics",
#      "year": 1996,
#      "name": "john"
# }
# # copyDict = dict3.copy()
# # print(copyDict)
# copyDict = dict(dict3)
# print(copyDict)


# nested dictionary
family_tree = {
    "child1": {
        "name": 'x',
        'age': 12
    },
    "child2": {
        "name": "y",
        'age': 15
    },
    "child3": {
        "name": 'z',
        'age': 20
    }
}
# 2nd metthod
child1 = {
        "name": 'x',
        'age': 12
    }
child2 = {
        "name": "y",
        'age': 15
    }
child3 = {
        "name": 'z',
        'age': 20
    }
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
# accessing items in nested dictionary
# print(myfamily["child2"]["name"])
# # loop through nested dictionary
# for x, obj in myfamily.items():
#     print()
#     print(x)
#     for y in obj:
#         print(y, ":", obj[y])

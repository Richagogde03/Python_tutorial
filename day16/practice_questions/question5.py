# Create a function that takes a list of numbers lst, a string s and return a
# list of numbers as per the following rules:

#     "Asc" returns a sorted list in ascending order.
#     "Des" returns a sorted list in descending order.
# "None" returns a list without any modification.

def asc_des_none(list1, string):
    if string == "Asc":
        return sorted(list1)
    elif string == "Des":
        return sorted(list1, reverse=True)
    elif string == "None":
        return list1


print(asc_des_none([4, 3, 2, 1], "Asc"))
print(asc_des_none([7, 8, 11, 66], "Des"))
print(asc_des_none([1, 2, 3, 4], "None"))

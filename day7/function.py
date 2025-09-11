# def my_function():
#     print("Hello i am \"\\Function\"")


# my_function()


# function with Arguments
# def full_name(fname, lname):
#     print(f"Hello my full name is \"{fname} {lname}\"")


# full_name('John', "Doe")


# arbitrary arguments *args
# def all_kids(*kids):
#     print("All Kids Name :", kids)
#     print(type(kids))
#     print("The youngest child is :", kids[2])
#     print("The oldest child is :", kids[0])


# all_kids('neha', 'anita', 'priya')


# Keyword Arguments
# def children_name(child1, child2, child3):
#     print("3rd child name is :", child3)
#     print(f"All children name : {child1}, {child2}, {child3}")


# children_name(child3='karan', child2='krishna', child1='kapil')


# arbitary keyword arguments, **kwargs
# def my_details(**details):
#     print("My age is :", details['age'])
#     print("My first name is : " + details['fname'])


# my_details(fname="priya", lname="chauhan", age=23)


# Default parameter value
# def my_country(country="India"):
#     print("My country is " + country)


# my_country("Sweden")
# my_country()
# my_country("Brazil")


# passing a list as an argument
# def fruit_function(fruit):
#     print("My favourite fruits are :", fruit)


# fruits = ['Mango', 'Apple', 'Watermelon']


# fruit_function(fruits)


# return values
# def mult(x):
#     return 5 * x


# print(mult(2))
# print(mult(3))
# print(mult(4))


# The pass statement
def mu_func():
    pass


# table of any number
def table_func(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")


num = int(input("Enter Number to find its table : "))
table_func(num)

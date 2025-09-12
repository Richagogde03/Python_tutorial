# keyword arguments
# def add(a, b=5, c=10):
#     return (a+b+c)


# print(add(b=10, c=15, a=20))


# # positional arguments , 1st method
# def add(a, b, c):
#     return (a+b+c)


# print(add(10, 20, 30))
# # 2nd method using mix of positional and keyword argument
# print(add(10, c=30, b=20))


# *args and **kwargs
# *args example
def fun(*args):
    return sum(args)


print(fun(5, 10, 15))


# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)


fun(a=1, b=2, c=3)

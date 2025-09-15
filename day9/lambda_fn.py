# lambda function # noqa: E731
# x = lambda a: a + 10
# print(x(5))


# x1 = lambda a, b: a * b
# print(x1(5, 6))


# x2 = lambda a, b, c: a + b + c
# print(x2(3, 4, 5))

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(4))

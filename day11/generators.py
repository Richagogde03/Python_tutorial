
# basic generator fn
# def fun():
#     yield 1
#     yield 2
#     yield 3


# for val in fun():
#     print(val)


# 2nd Example
def my_generator():
    for i in range(10):
        yield i


gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
for i in gen:
    # print(i, sep='')
    print(i, end=" ")

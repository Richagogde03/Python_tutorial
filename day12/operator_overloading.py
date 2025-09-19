# without operator overloading
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def add_points(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)


# p1 = Point(1, 2)
# p2 = Point(2, 3)

# p3 = p1.add_points(p2)

# print((p3.x, p3.y))


# with operator overloading
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

# this statment calls the __add__() method
p3 = p1 + p2

print((p3.x, p3.y))

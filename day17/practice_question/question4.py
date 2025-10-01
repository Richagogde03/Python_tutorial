
from math import sqrt
# Given the radius of a circle and the area of a square, return True if the
# circumference of the circle is greater than the square's perimeter and False
# if the square's perimeter is greater than the circumference of the circle.
# medium


def circle_or_square(r_circle, a_square):
    circumference = 2 * 3.14 * r_circle
    side_of_sqaure = sqrt(a_square)

    perimeter = 4 * side_of_sqaure

    if circumference > perimeter:
        return True
    else:
        return False


# print(circle_or_square(16, 625))
# print(circle_or_square(5, 100))
print(circle_or_square(8, 144))

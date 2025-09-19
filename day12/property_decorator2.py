class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return (f"{self._width:.1f} cm")

    @property
    def height(self):
        return (f"{self._height:.1f} cm")

    @width.setter
    def width_change(self, new_width):
        print("setter method called for width!!")
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height_change(self, new_height):
        print("setter method called for height!!")
        if new_height > 0:
            self._height = new_height
        else:
            print("Width must be greater than 0")

    # @width.deleter
    # def width(self):
    #     del self._width
    #     print("Width has been deleted")

    # @height.deleter
    # def height(self):
    #     del self._height
    #     print("Height has been deleted")


rectangle = Rectangle(3, 4)

print(rectangle.width)
# rectangle.width_change = 0
rectangle.width_change = 500
# rectangle.height_change = -1
rectangle.height_change = 100

# del rectangle.width
# del rectangle.height

print(rectangle.width)
print(rectangle.height)

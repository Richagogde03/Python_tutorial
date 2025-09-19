class Duck:

    def sound(self):
        print("Quack Quack!!")


class Dog:

    def sound(self):
        print("Woof Woof!!")


class Cat:

    def sound(self):
        print("Meow Meow!!")


def all_sounds(obj):
    obj.sound()


x = Cat()
all_sounds(x)

# if we want to access the same method from all classes we can use for loop
# for i in Duck(), Dog(), Cat():
#     i.sound()

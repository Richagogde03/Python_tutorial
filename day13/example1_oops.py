
class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def speak(self):
        return (f"{self.get_name()} says Woof!")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.__color = color

    def get_color(self):
        return self.__color

    def speak(self):
        return (f"{self.get_name()} says meow!!")


# dog object
obj_dog = Dog("Harry", "bulldog")
print(obj_dog.get_name())
print(obj_dog.get_breed())
print(obj_dog.speak())


# cat object
cat_obj = Cat("Carry", "Black")
print(cat_obj.get_name())
print(cat_obj.get_color())
print(cat_obj.speak())


# polymorphism (duck typing)
animals = [obj_dog, cat_obj]
for i in animals:
    print(i.speak())

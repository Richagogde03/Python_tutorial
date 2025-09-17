class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

        # a normal function
        # will change the attribute for particular instance of the class
    # def changeCompany(cls, newCompany):
    #     cls.company = newCompany

    # it will make changes directly to class attribute not instance
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Krishan"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(e1.company)
print(Employee.company)

# it will make changes in class attributs
Employee.changeCompany("Honda")

print(Employee.company)
print(e1.company)


# 2nd example
# class MyClass:
#     class_variable = "I am a class variable"

#     @classmethod
#     def class_method(cls):
#         """A class method operates on the class itself, not an instance."""
#         print(f"This is a class method called from {cls.__name__}")
#         print(f"Accessing class variable from class method:
# {cls.class_variable}")

#     def instance_method(self):
#         """An instance method operates on an instance of the class."""
#         print(f"This is an instance method called from {self}")


# # Calling the class method using the class name
# MyClass.class_method()

# # You can also call a class method using an instance, but it's less common
# obj = MyClass()
# obj.class_method()

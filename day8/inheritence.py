# Single Inheritence Example
class Employee:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def printName(self):
        print(f"Name of Employee is {self.first_name} {self.last_name}!")


# class Manager(Employee):
#     pass
# class Manager(Employee):
#     def __init__(self, fname, lname):
#         Employee.__init__(self, fname, lname)

# class Manager(Employee):
#     def __init__(self, fname, lname, age):
#         super().__init__(fname, lname)
#         self.age = age

#     def welcome(self):
#         print("Welcome", self.first_name, self.last_name, "to the seminar!!")


# m1 = Manager("Rishi", "Kapoor", 45)
# m1.printName()
# print(m1.age)
# m1.welcome()


# Multiple Inheritance
# class Mother:
#     def mother_name(self, mname):
#         self.mname = mname


# class Father:
#     def father_name(self, fname):
#         self.fname = fname


# class Son(Mother, Father):
#     def __init__(self, mname, fname):
#         Mother.mother_name(self, mname)
#         Father.father_name(self, fname)
#         print("Father's Name :", self.fname)
#         print("Mother's Name :", self.mname)


# son = Son("Neelam Soni", "Karan Soni")


# multilevel inheritence
# class Grandf:
#     def __init__(self, gname):
#         self.gname = gname


# class Father:
#     def __init__(self, fname):
#         self.fname = fname


# class Son:
#     def __init__(self, gname, fname, sname):
#         Grandf.__init__(self, gname)
#         Father.__init__(self, fname)
#         self.sname = sname
#         print(f"My grandfather name is {gname} and father name is {fname}")


# son = Son("x", "y", "z")


# Hierarchical inheritance
class Parent:
    def func1(self):
        print("This function is in parent class")


class Child1(Parent):
    def func2(self):
        print("This function is in child1 class")


class Child2(Parent):
    def func3(self):
        print("This function is in child2 class")


c1 = Child1()
c2 = Child2()

c1.func1()
c1.func2()
c2.func1()
c2.func3()


# Hybrid Inheritance


# ambiguity in python , solved by MRO (Method resolution order)
class A:
    def greet(self):
        print("Hello from A")


class B(A):
    def greet(self):
        print("Hello from B")


class C(A):
    def greet(self):
        print("Hello from C")


class D(C, B):
    pass


obj = D()
obj.greet()

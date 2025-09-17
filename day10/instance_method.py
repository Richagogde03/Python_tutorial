# instance method without parameter / formal arguments
# class Mobile:
#     def show_model(self):
#         print("Real me x")


# mobile = Mobile()
# mobile.show_model()


# instance method with constructor
# class Mobile2:
#     def __init__(self):
#         self.model = "Real me x"

#     def show_model(self):
#         print(f"Model is {self.model}")


# mobile2 = Mobile2()
# mobile2.show_model()


# instance method with formal arguments
class Mobile3:
    def __init__(self, model):
        self.model = model

    def show(self, p):
        self.price = p
        print(f"Model name is {self.model} and its price {self.price}")


mobile3 = Mobile3("Real me x")
mobile3.show("7500 Rs")

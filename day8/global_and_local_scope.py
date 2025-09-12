# local scope
# def greet():
#     msg = "Hello from inside the function!"
#     print(msg)


# greet()


# local scope but trying to access it out of scope
# def greet():
#     msg = "Hello!"
#     print("Inside function:", msg)


# greet()
# print("Outside function:", msg)


# Global variable
msg = "Hello!!"


def display(msg):
    print(f"{msg} from inside the function!!")


display(msg)
print(f"{msg} from outside the function!!")

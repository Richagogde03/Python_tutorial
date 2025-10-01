# 1st
# def get_weather(temp):
#     if temp > 20:
#         return "Hot"
#     else:
#         return "Cold"


# 2nd
# def add(a, b):
#     return a+b


# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a // b


# 3rd
class UserManager:
    def __init__(self):
        self.user = {}

    def add_user(self, username, email):
        if username in self.user:
            raise ValueError("User already exits")
        self.user[username] = email
        return True

    def get_user(self, username):
        return self.user.get(username)

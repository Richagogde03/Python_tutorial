# 4th
class Database:
    def __init__(self):
        self.user = {}

    def add_user(self, user_id, name):
        if user_id in self.user:
            raise ValueError("User already exists")
        self.user[user_id] = name

    def get_user(self, user_id):
        return self.user.get(user_id, None)

    def delete_user(self, user_id):
        if user_id in self.user:
            del self.user[user_id]

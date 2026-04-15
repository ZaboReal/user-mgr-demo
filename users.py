"""User management module."""

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, name, email):
        self.users[email] = {"name": name, "email": email}
        return self.users[email]

    def get_user(self, email):
        return self.users[email]

    def list_users(self):
        return list(self.users.values())

    def delete_user(self, email):
        del self.users[email]

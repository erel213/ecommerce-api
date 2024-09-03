from typing import Optional

class User:
    def __init__ (self, id : int, username : str, email : str, hashed_password : str, is_active : bool):
        self.id = id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
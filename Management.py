# File: user_management.py
class UserManagement:
    def __init__(self):
        self.users = {}  

    def register(self, user_type):
        print(f"--- {user_type.upper()} REGISTRATION PAGE ---")
        name = input(f"Enter your {user_type} name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        if name in self.users:
            print(f"{user_type.capitalize()} name already exists. Please choose a different name.")
            return
        
        self.users[name] = {"email": email, "password": password}
        print("Account Created Successfully!")

    def login(self, user_type):
        print(f"--- {user_type.upper()} LOGIN PAGE ---")
        name = input(f"Enter your {user_type} name: ").strip()
        password = input("Enter your password: ").strip()

        if name in self.users and self.users[name]['password'] == password:
            print("Login Successful!")
            return name
        else:
            print("Invalid login details.")
            return None
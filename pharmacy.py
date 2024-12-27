
# File: pharmacy.py
from Management import UserManagement
from stock import StockManagement

class Pharmacy:
    def __init__(self):
        self.user_manager = UserManagement()
        self.stock_manager = StockManagement()

    def pharmacy_menu(self):
        while True:
            print("\n--- PHARMACY MANAGEMENT ---")
            print("1. New Registration")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.user_manager.register("pharmacy")
            elif choice == '2':
                user = self.user_manager.login("pharmacy")
                if user:
                    self.pharmacy_dashboard(user)
            elif choice == '3':
                print("Exiting Pharmacy Management...")
                break
            else:
                print("Invalid choice, try again.")

    def pharmacy_dashboard(self, user):
        while True:
            print("\n--- PHARMACY DASHBOARD ---")
            print("1. View Stock")
            print("2. Add Stock")
            print("3. Request Medicine from Company")
            print("4. Logout")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                self.stock_manager.show_stock()
            elif choice == '2':
                self.stock_manager.add_stock()
            elif choice == '3':
                self.stock_manager.request_medicine(user)
            elif choice == '4':
                print("Logging out...")
                break
            else:
                print("Invalid choice, try again.")
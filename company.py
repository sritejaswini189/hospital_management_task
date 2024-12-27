# File: company.py
from Management import UserManagement
from stock import StockManagement

class Company:
    def __init__(self):
        self.user_manager = UserManagement()
        self.stock_manager = StockManagement()

    def company_menu(self):
        while True:
            print("\n--- COMPANY MANAGEMENT ---")
            print("1. New Registration")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.user_manager.register("company")
            elif choice == '2':
                user = self.user_manager.login("company")
                if user:
                    self.company_dashboard()
            elif choice == '3':
                print("Exiting Company Management...")
                break
            else:
                print("Invalid choice, try again.")

    def company_dashboard(self):
        while True:
            print("\n--- COMPANY DASHBOARD ---")
            print("1. View Stock")
            print("2. Add Stock")
            print("3. View Hospital Requests")
            print("4. View Pharmacy Requests")
            print("5. Logout")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.stock_manager.show_stock()
            elif choice == '2':
                self.stock_manager.add_stock()
            elif choice == '3':
                self.stock_manager.show_requests()
            elif choice == '4':
                self.stock_manager.show_requests()
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice, try again.")







# File: main.py
from company import Company
from hospital import Hospital
from pharmacy import Pharmacy

class DrugManagementSystem:
    def __init__(self):
        self.company = Company()
        self.hospital = Hospital()
        self.pharmacy = Pharmacy()

    def main_menu(self):
        while True:
            print("\n*** WELCOME TO DRUG MANAGEMENT SYSTEM ***")
            print("1. Company Management")
            print("2. Hospital Management")
            print("3. Pharmacy Management")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.company.company_menu()
            elif choice == '2':
                self.hospital.hospital_menu()
            elif choice == '3':
                self.pharmacy.pharmacy_menu()
            elif choice == '4':
                print("Exiting Drug Management System... Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    dms = DrugManagementSystem()
    dms.main_menu()

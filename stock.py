
# File: stock_management.py
class StockManagement:
    def __init__(self):
        self.stocks = {}  # Store medicine stock
        self.requests = []  # Store medicine requests

    def show_stock(self):
        print("Current stock:", self.stocks)

    def add_stock(self):
        medicine = input("Enter medicine name: ").strip()
        quantity = int(input("Enter quantity: "))
        self.stocks[medicine] = self.stocks.get(medicine, 0) + quantity
        print("Stock added successfully!")

    def request_medicine(self, requester):
        medicine = input("Enter medicine name: ").strip()
        quantity = int(input("Enter quantity: "))
        self.requests.append({"requester": requester, "medicine": medicine, "quantity": quantity})
        print("Request added successfully!")

    def show_requests(self):
        print("Pending Requests:", self.requests)
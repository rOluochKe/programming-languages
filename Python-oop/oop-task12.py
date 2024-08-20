"""
Title: Customer Loyalty System

Description:
The provided code demonstrates a customer loyalty system that allows tracking and managing loyalty points earned by customers. The system is designed using class inheritance to categorize customers and store their transaction history.

#####

Customer Class:
The base class `Customer` represents a customer and stores their unique `customer_id` and `name`. It serves as a foundation for customer-related functionality.

###

LoyaltyPoints Class:
The `LoyaltyPoints` class encapsulates the logic for managing loyalty points. It tracks the number of points earned by a customer using the `points` attribute. The class provides methods to earn points, redeem points, and retrieve the current points balance.

###

VIPCustomer Class:
The `VIPCustomer` class inherits from both the `Customer` and `LoyaltyPoints` classes. It combines the customer information with loyalty points functionality. The class is initialized with a `customer_id` and `name` inherited from the `Customer` class.

###

Transaction Class:
The `Transaction` class represents a specific transaction made by a customer. It stores a `transaction_id`, a reference to the `customer` involved in the transaction, and the transaction `amount`.

###

TransactionHistory Class:
The `TransactionHistory` class manages the collection of transactions. It provides methods to add transactions to the history and display the transaction details.

#####

Outside your classes, an instance of the `VIPCustomer` class named `vip_customer` is created with a customer ID of "VIP123" and the name "John." The customer earns 100 loyalty points and redeems 50 points.

Two transactions, `transaction1` and `transaction2`, are created using the `Transaction` class. They associate the `vip_customer` with specific transaction IDs and amounts.

A `TransactionHistory` instance named `transaction_history` is created to store and manage the transactions. The two transactions are added to the transaction history.

The transaction history is displayed, showing the transaction IDs, customer names, and amounts for each transaction.

The points balance of the `vip_customer` is retrieved using the `get_points_balance()` method, and it is printed along with the customer ID and name.

This code demonstrates a simple loyalty system where customers can earn and redeem loyalty points. It provides a structured approach to managing customer data and transaction history, facilitating the tracking of customer activities and points balance.
"""


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class LoyaltyPoints:
    def __init__(self):
        self.points = 0

    def earn_points(self, amount):
        self.points += amount

    def redeem_points(self, amount):
        if self.points >= amount:
            self.points -= amount
        else:
            print("Not Enough Points!")

    def show_point_balance(self):
        return self.points


class VIPcustomer(Customer, LoyaltyPoints):
    def __init__(self, customer_id, name):
        Customer.__init__(self, customer_id, name)
        LoyaltyPoints.__init__(self)


class Transaction:
    def __init__(self, transaction_id, customer, amount):
        self.transaction_id = transaction_id
        self.customer = customer
        self.amount = amount


class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transactions(self, transaction):
        self.transactions.append(transaction)

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction.transaction_id,
                  transaction.customer.name, transaction.amount)


vip = VIPcustomer("VIP001", "Josh")
vip.earn_points(40000)
vip.redeem_points(12500)

transaction1 = Transaction("T-001", vip, "+40000")
transaction2 = Transaction("T-002", vip, "-12500")

transaction_history = TransactionHistory()
transaction_history.add_transactions(transaction1)
transaction_history.add_transactions(transaction2)

transaction_history.show_transactions()

balance = vip.show_point_balance()

print(f"Customer ID: {vip.customer_id}")
print(f'Customer Name: {vip.name}')
print(f'Loyalty Point Balance: {balance}')

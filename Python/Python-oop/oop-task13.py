"""
Title: Online Shopping System

Description:
The provided code represents an online shopping system where users can interact as customers and sellers. The system is designed using class inheritance to differentiate between customers and sellers, each with their specific functionalities.

#####

User Class:
The base class `User` represents a generic user and stores their username and email.

-It provides the fundamental attributes and methods that are inherited by both customers and sellers.

###

Customer Class:
The `Customer` class inherits from the `User` class and adds additional functionality specific to customers.

-It introduces 4 methods!

-A cart to store products list, manage the cart, such as adding products, removing products, and viewing the cart methods

-The class also includes a method to save the cart to a file.

We need to use (with open() as file for this step)

###

Seller Class:
The `Seller` class also inherits from the `User` class and provides functionality specific to sellers.

-It introduces a list of products for sale and methods to add products, remove products, and view the products.

-The class includes a method to save the list of products to a file.

###

Product Class:
The `Product` class represents a product with attributes such as name and price.

-It includes a method to display information about the product.

###

Outside your classes, a customer and a seller are instantiated as objects of their respective classes. Two products, a shirt and shoes, are also created as instances of the `Product` class.

The customer adds the products to their cart using the `add_to_cart()` method and views the contents of the cart using the `view_cart()` method. The customer then saves the cart to a file using the `save_cart_to_file()` method. One of the products is removed from the cart using the `remove_from_cart()` method, and the cart is viewed again.

The seller adds the products to their list of products using the `add_product()` method and views the available products using the `view_products()` method. The seller then saves the list of products to a file using the `save_products_to_file()` method.

This code simulates a basic online shopping system, allowing customers to add products to their cart and sellers to manage their list of products for sale. It demonstrates the use of class inheritance and file handling to facilitate interactions between customers, sellers, and products in an e-commerce environment.
"""


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_to_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            print("Item not in your cart!")

    def view_cart(self):
        print("Items in cart:")
        for product in self.cart:
            print(product.name)

    # filename.txt

    def save_cart(self, filename):
        with open(filename, "w") as file:
            for product in self.cart:
                file.write(f'{product.name}, {product.price}\n')
        print(f'Cart saved to {filename}')


class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print(f'Product Not Found!')

    def view_products(self):
        print(f'List of Products:')
        for product in self.products:
            print(product.name)

    def save_products(self, filename):
        with open(filename, "w") as file:
            for product in self.products:
                file.write(f'{product.name}, {product.price}\n')
        print(f'Products saved to {filename}')


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def basic_info(self):
        print(f'Product: {self.name}')
        print(f'Price: {self.price}')


customer = Customer("BillyBob123", "billy@hooloo.com")
seller = Seller("SarahJane88", "jane@yahoo.com")

product1 = Product("Shoes", 65.00)
product2 = Product("Ring", 125.00)
product3 = Product("T-Shirt", 28.00)

customer.add_to_cart(product1)
customer.add_to_cart(product2)
customer.add_to_cart(product3)

customer.view_cart()

customer.save_cart("customer_cart.txt")

customer.remove_to_cart(product2)

customer.view_cart()


seller.add_product(product1)
seller.add_product(product2)
seller.add_product(product3)

seller.view_products()

seller.save_products("seller_products.txt")

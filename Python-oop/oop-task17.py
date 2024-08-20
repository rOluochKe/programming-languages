"""
Description:
Cryptocurrency management system. It defines classes such as `Crypto`, `Bitcoin`, and `Ethereum` to represent cryptocurrencies, their properties, and operations. The code allows users to create cryptocurrency objects, compare them, combine them, set prices, retrieve prices, and calculate the total value of cryptocurrency holdings. It also showcases specialized methods for Bitcoin mining and Ethereum token minting.


Heads up -> In this challenge you will use the hasattr() python function
This function is used smiliar to the isinstance() function

hasattr() => Used to check if a Class has a certain Property


1. The code introduces the `Crypto` class, which serves as a foundation for creating and manipulating various cryptocurrencies. It includes several essential methods:
   - The `__init__` method initializes a `Crypto` object with a given `name`.
   - The `__str__` method returns a string representation of the `Crypto` object, describing it as a cryptocurrency.
   - The `__eq__` method enables comparison between two `Crypto` objects based on their names.
   - The `__add__` method allows the merging of two `Crypto` objects, combining their names into a new cryptocurrency.
   - The `set_price` method assigns a price to the `Crypto` object.
   - The `get_price` method retrieves the assigned price of the `Crypto` object, if set.
   - The `calculate_total_value` method calculates the total value of a given quantity of the `Crypto` object, based on its assigned price.

2. Two subclasses of `Crypto` are defined:
   - The `Bitcoin` subclass represents the Bitcoin cryptocurrency. It inherits from `Crypto` and includes a `mine` method that simulates the mining process.
   - The `Ethereum` subclass represents the Ethereum cryptocurrency. It also inherits from `Crypto` and includes a `mint` method that simulates the creation of Ethereum tokens.

3. In the usage example:
   - Instances of the `Crypto`, `Bitcoin`, and `Ethereum` classes are created, each with their respective names.
   - Various methods of the classes are demonstrated:
     - Printing the string representation of a `Crypto` object.
     - Comparing two `Crypto` objects for equality.
     - Combining the names of two `Crypto` objects into a new cryptocurrency.
     - Setting the price of a `Crypto` object and retrieving the assigned price.
     - Invoking specialized methods (`mine` and `mint`) unique to the `Bitcoin` and `Ethereum` subclasses, respectively.
     - Evaluating the total value of cryptocurrencies in a portfolio, using a list of dictionaries containing the `Crypto` objects and corresponding quantities.
"""


class Crypto:
    def __init__(self, name):
        self.name = name
        self.price = 0

    def __str__(self):
        return f"This is {self.name} a cryptocurrency"

    def __eq__(self, other):
        if isinstance(other, Crypto):
            return self.name == other.name
        return False

    def __add__(self, other):
        if isinstance(other, Crypto):
            combo = self.name + " " + other.name
            return Crypto(combo)
        else:
            raise ValueError("Can not preform addtion between them!")

    def set_price(self, price):
        self.price += price

    def get_price(self):
        if hasattr(self, "price"):
            return self.price
        else:
            print("Price not set")

    def calc_value(self, quantity):
        if hasattr(self, "price"):
            return self.price * quantity
        else:
            print("Price not set!")


class Bitcoin(Crypto):
    def __init__(self):
        Crypto.__init__(self, "Bitcoin")

    def __str__(self):
        return f"Bitcoin is decentralized!"

    def mine(self):
        return f"Mining the next Block..."


class Ethereum(Crypto):
    def __init__(self):
        Crypto.__init__(self, "Ethereum")

    def __str__(self):
        return f"Ethereum uses smart contracts!"

    def mine(self):
        return f"Minting tokens..."


crypto1 = Crypto("Solana")
crypto2 = Crypto("Cardano")
crypto3 = Crypto("Bitcoin")

bitcoin = Bitcoin()
ether = Ethereum()


print(ether + crypto2)

ether.set_price(1750)
bitcoin.set_price(28000)
crypto1.set_price(16.50)


portfolio = [
    {"crypto": bitcoin, "quantity": 5},
    {"crypto": ether, "quantity": 32},
    {"crypto": crypto1, "quantity": 25}
]

for asset in portfolio:
    crypto = asset["crypto"]
    quantity = asset["quantity"]

    total = crypto.calc_value(quantity)
    print(
        f'The total value of {crypto.name} with your amount of {quantity} is {total}')

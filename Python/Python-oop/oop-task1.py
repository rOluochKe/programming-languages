"""
Try to recreate the Class we saw during the introduction of this new topic!

Some key things to remember
    1. Class App
    2. init has 3 properties.  users,storage, username
    3. There are 2 additional methods. (login and increase_capacity)
    4. login method -> Checks if the username is "owner" and users is not empty
        -if true, It will welcome the user and print their storage number
    5. increase_capacity method -> This accepts a number and add this to the current storage value
        -Then printing out the updated amount
    6. Create two objects.  Each object calls both methods.  Be creative

    BONUS:

    Create a bonus method:

    1. Checks, if users is greater than storage.  A upgrade amount is asked, this amount it added to the current storage
    2. Otherwise, Print off the remaining storage left
"""


class App:
    def __init__(self, users, storage, username):
        self.users = users
        self.storage = storage
        self.username = username

    def login(self):
        if self.username == "owner" and self.users >= 1:
            print("Welcome,", self.username)
            print("Your storage is:", self.storage)
        else:
            print("You are not a user!")

    def increase_capacity(self, number):
        self.storage += number
        print("Updated storage:", self.storage)

    def check_upgrade(self):
        if self.users >= self.storage:
            upgrade_amt = int(input("Upgrade amount: "))
            self.storage += upgrade_amt
        else:
            print("You still have:", str(
                self.storage - self.users), "spaces open!")


product_one = App(35, 256, "owner")


product_one.login()
product_one.increase_capacity(44)
print()

product_two = App(12, 128, "josh")
product_two.login()
product_two.check_upgrade()

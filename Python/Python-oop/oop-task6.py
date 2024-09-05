"""
Title: Animal Passport and Clinic Database

Description:
Welcome to the Animal Passport and Clinic Database! This code allows us to gather information about different animals, store their details, and search for specific species based on regions. Let's explore the functionality and purpose of each class in this code.

Animal Class:
The Animal class serves as the foundation for creating instances of various animals. It has the following attributes:
- "region": Represents the geographic region where the animal is found.
- "animal_type": Specifies the species or type of animal.
- "color": Describes the color of the animal.
- "lethal": Indicates whether the animal is dangerous or not, with a value of True or False.

The class contains an "animal_bio()" method, which displays an animal's passport-like information. This method prints the animal's region, species, color, and whether it is dangerous or not.

Clinic Class (Child Class of Animal):
The Clinic class inherits from the Animal class, representing a specialized clinic or database for animals. It introduces two additional methods:
- "animal_info()": This method provides a brief summary of the animal, mentioning its species and region.
- "search(animals)": The search method prompts the user to enter a region and then searches the list of animals passed as a parameter. It matches the entered region with the animals' regions and prints the species of animals found in that region.

The Main Code:
The main code utilizes the Animal and Clinic classes to create an interactive animal database. It follows these steps:
1. Requests the user to input the number of animals to be added to the database.
2. In a loop, it prompts for the animal's region, species, color, and whether it is dangerous.
3. Creates an Animal instance with the provided information and adds it to the "animals" list.
4. Instantiates a Clinic object named "clinic" with default values: region ("Asia"), species ("tiger"), color ("orange"), and dangerous (True).
5. Invokes the "animal_bio()" method on the "clinic" object to display its passport-like information.
6. Calls the "animal_info()" method on the "clinic" object to provide a summary of the animal.
7. Executes the "search(animals)" method on the "clinic" object, allowing the user to search for animals in a specific region. It iterates over the "animals" list, matches the entered region, and prints the species of animals found.

With this code, we can explore the Animal Passport and Clinic Database, learn about different animals, and search for species based on regions. It facilitates organization and retrieval of information about animals, contributing to the study and conservation of diverse wildlife populations. Enjoy your journey into the fascinating world of animals!
"""


class Animal:
    def __init__(self, region, animal_type, color, lethal):
        self.region = region
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal

    def animal_bio(self):
        print("Animal Passport:")
        print(f'Found in: {self.region}')
        print(f'Species: {self.animal_type}')
        print(f'Color: {self.color}')
        print(f'Dangerous: {self.lethal}')


class Clinic(Animal):
    def animal_info(self):
        print(f'This is a {self.animal_type} from {self.region}')

    def search(self, animals):
        region = input("Enter a region: ").lower()
        for animal in animals:
            if animal.region == region:
                print(f'Species: {animal.animal_type}')


animals = []
amt_animals = int(input("Enter number of animals: "))
for i in range(amt_animals):
    region = input("Enter a region: ").lower()
    species = input("Enter a species: ").lower()
    color = input("Enter a color: ").lower()
    lethal = input("Is it dangerous: ").lower()
    lethal = lethal == 'yes'

    animal = Animal(region, species, color, lethal)

    animals.append(animal)

clinic = Clinic("asia", "tiger", "orange", True)

clinic.animal_bio()
clinic.animal_info()
clinic.search(animals)

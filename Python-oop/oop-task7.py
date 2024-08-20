"""
Title: Superhero and Flying Superhero Adventure

Description:
This code is all about superheroes and their incredible abilities! Let's dive into the exciting world of superheroes explained in simpler terms.

#####

Regular Superheroes (Superclass):
The code begins with a class called "Superhero." Each superhero has a special name and a unique power. Imagine superheroes like Superman or Spider-Man!

-The use_power() method shows how a superhero demonstrates their power. It prints a message telling us about the superhero and the power they have.

-The intro() method introduces the superhero, sharing their name and power with us. The save_the_day() method emphasizes the superhero's mission to save people and make the world a better place.
-The calculate_power_level() method calculates a numerical power level based on the length of the superhero's power.

#####

Flying Superheroes (Child Class):
Now, let's take superheroes to the next level with the "FlyingSuperhero" class. These superheroes can fly!

-They inherit all the attributes and methods of regular superheroes, but with an added flying speed.

-The use_power() method for flying superheroes shows how they use their power to fly through the sky at a specific speed. It's like Iron Man soaring through the air!

-The calculate_flying_distance(flight_time) method calculates how far a flying superhero can travel based on their flying speed and the time they spend flying.

#####

Outside your classes, we create a flying superhero named "Starwing." They have the power of flight and can fly at an incredible speed of 500 mph. We get to know Starwing through their introduction, and we see them in action using their power to fly. We calculate Starwing's power level based on the length of their power and find out how far they can fly in a given amount of time.

So, this code lets us explore the exciting world of superheroes! We learn about their powers, get introduced to their characters, and witness their incredible abilities to save the day and fly through the sky. It's like being a part of a thrilling superhero adventure! Get ready to unleash your imagination and join these extraordinary superheroes on their heroic quests
"""


class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def use_power(self):
        print(f'{self.name} is using {self.power} power!')

    def intro_hero(self):
        print(f'I am {self.name} and I have the power {self.power}')

    def save_day(self):
        print(f'{self.name} has saved the day!')

    def power_level(self):
        length = len(self.power)
        level = length*10
        return level


class Flying(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed

    def use_power(self):
        print(f'{self.name} is flying at the speed of {self.speed} miles per hour')

    def calc_distance(self, flight_time):
        distance = self.speed * flight_time
        return distance


batman = Superhero("Batman", "Strength")
batman.intro_hero()
print(batman.power_level())

print()
superman = Flying("Clark Kent", "Flight", 250)
superman.intro_hero()
superman.use_power()

flight_dist = 30
attack = superman.calc_distance(flight_dist)
print(f'{superman.name} can fly a distance of {attack} miles in {flight_dist} hours')

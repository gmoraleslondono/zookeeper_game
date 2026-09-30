from animals import Lion, Monkey, Cow
from zookeeper import Zookeeper
from zoo import Zoo
from game import run


print("""
********************************
*                              *
*           Zoo Game           *
*                              *
********************************

Instructions:
You are a zookeeper. Choose your name and start playing.
The animals in the Zoo need to be fed, played with, and left to rest.
You have limited energy, so some rest is needed too.
You have limited coins to buy food, use them wisely.

When you win:
- You get 100 points from taking care of the animals in the Zoo.

When you lose:
- An animal gets so hungry that it runs away from the zoo (hunger = 100).
- You run out of food (food = 0) and don't have enough coins to buy more (coins < 5).

NOTE: every action during the game makes the animals more tired and hungrier.
""")

user_name = input("What is your name?: ")

zookeeper = Zookeeper(user_name)
leo = Lion("Leo")
momo = Monkey("Momo")
bella = Cow("Bella")

zoo = Zoo(zookeeper, [leo, momo, bella])

run(zoo)

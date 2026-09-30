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
- Your score reaches 100.

When you lose:
- An animal gets so hungry that it runs away (hunger = 100).
- An animal gets so tired that it collapses (energy = 0).
- You run out of food and can't afford more (food = 0 and coins < 8).

NOTE: every action makes all the animals hungrier (+8) and more tired (-8 energy).
Feeding earns the most points. Playing earns the most coins.
Sleeping restores an animal, but they wake up hungrier.
""")

user_name = input("What is your name?: ")

zookeeper = Zookeeper(user_name)
leo = Lion("Leo")
momo = Monkey("Momo")
bella = Cow("Bella")

zoo = Zoo(zookeeper, [leo, momo, bella])

run(zoo)

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

Look after 🦁 Leo the Lion, 🐵 Momo the Monkey, and 🐮 Bella the Cow until your score reaches 100.

Each action makes every animal hungrier (+8) and more tired (-8).
They run away at hunger 100, and collapse at energy 0.
With no food and fewer than 8 coins, the game ends.
""")

user_name = input("Pick your zookeeper name: ")

zookeeper = Zookeeper(user_name)
leo = Lion("Leo")
momo = Monkey("Momo")
bella = Cow("Bella")

zoo = Zoo(zookeeper, [leo, momo, bella])

run(zoo)

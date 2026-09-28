class Animal:
    def __init__(self, name, hunger, energy):
        self.name = name
        self.hunger = hunger
        self.energy = energy

    def eat(self, animal):
        # hunger = -30
        print(f"{animal} eat!!!!")

    def sleep(self, animal):
        # energy = +40
        # hunger = +10
        print(f"{animal} sleep!!!")

    def play(self, animal):
        # hunger = +15
        # energy = -20
        print(f"{animal} play")

    def make_sound(self, animal):
        print(f"{animal} make sound!!!")

    def __str__(self):
        return f"{self.name}: hunger={self.hunger}, energy={self.energy}"


class Lion(Animal):
    def make_sound(self):
        return f"{self.name} says ROAR!"

class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} says OOH OOH AAH AAH!"

class Cow(Animal):
    def make_sound(self):
        return f"{self.name} says MUU!"

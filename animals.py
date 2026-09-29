class Animal:
    def __init__(self, name, hunger=50, energy=50):
        self.name = name
        self.hunger = hunger
        self.energy = energy

    def eat(self):
        if self.hunger == 0:
            raise ValueError(f"{self.name} is full and doesn't want to eat!")
        self.hunger = max(0 , self.hunger - 30) # min 0

    def sleep(self):
        if self.energy == 100:
            raise ValueError(f"{self.name} is not tired!")
        self.energy = min(100, self.energy + 40) # max 100
        self.hunger = min(100, self.hunger + 10) # max 100

    def play(self):
        if self.energy < 20:
            raise ValueError(f"{self.name} is too tired to play!")
        self.energy = max(0, self.energy - 20) # min 0
        self.hunger = min(100, self.hunger + 15) # max 100

    def make_sound(self):
        return f"{self.name} makes a sound!!!"

    # An animal waiting gets hungrier and more tired
    def wait(self):
        self.hunger = min(100, self.hunger + 5)
        self.energy = max(0, self.energy - 5)

    def __str__(self):
        return f"{self.name}: hunger={self.hunger}, energy={self.energy}"


class Lion(Animal):
    def make_sound(self):
        return f"{self.name} says ROAR!"

class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} says OOH-OOH AH-AH!"

class Cow(Animal):
    def make_sound(self):
        return f"{self.name} says MOO!"

class Fox(Animal):
    def make_sound(self):
        return f"{self.name} says Gering-ding-ding-ding-dingeringeding!"


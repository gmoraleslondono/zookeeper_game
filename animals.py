class Animal:
    def __init__(self, name, hunger, energy):
        self.name = name
        self.hunger = hunger
        self.energy = energy

    def eat(self, animal):
        print(f"{animal} eat!!!!")

    def sleep(self, animal):
        print(f"{animal} sleep!!!")

    def play(self, animal):
        print(f"{animal} play")

    def make_sound(self, animal):
        print(f"{animal} make sound!!!")

    def __str__(self):
        return f"{self.name}: hunger={self.hunger}, energy={self.energy}"

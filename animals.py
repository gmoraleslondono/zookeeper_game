import colors

class Animal:
    def __init__(self, name, hunger=45, energy=60):
        self.name = name
        self.hunger = hunger
        self.energy = energy

    def eat(self):
        if self.hunger == 0:
            print()
            raise ValueError(f"{colors.RED}{self.name} is full and doesn't want to eat!{colors.RESET}")
        self.hunger = max(0, self.hunger - 40) # min 0

    def sleep(self):
        if self.energy == 100:
            print()
            raise ValueError(f"{colors.RED}{self.name} is not tired!{colors.RESET}")
        self.energy = min(100, self.energy + 50) # max 100
        self.hunger = min(100, self.hunger + 10) # max 100

    def play(self):
        self.energy = max(0, self.energy - 20) # min 0
        self.hunger = min(100, self.hunger + 12) # max 100

    def make_sound(self):
        return f"{self.name} makes a sound!!!"

    # An animal waiting gets hungrier and more tired
    def wait(self):
        self.hunger = min(100, self.hunger + 8)
        self.energy = max(0, self.energy - 8)

    def hunger_mood(self):
        if self.hunger >= 80:
            return "starving"
        if self.hunger >= 55:
            return "hungry"
        if self.hunger >= 25:
            return "ok"
        if self.hunger == 0:
            return "full"
        return "satisfied"

    def energy_mood(self):
        if self.energy <= 20:
            return "exhausted"
        if self.energy <= 45:
            return "tired"
        if self.energy <= 75:
            return "ok"
        return "lively"

    def __str__(self):
        emojis = {
            "Lion": "🦁",
            "Monkey": "🐵",
            "Cow": "🐮",
        }
        emoji = emojis.get(self.__class__.__name__, "")
        name = self.name.ljust(5)
        hunger = str(self.hunger).rjust(3)
        hunger_mood = self.hunger_mood().ljust(10)
        energy = str(self.energy).rjust(3)
        return f"{emoji} {name} hunger {hunger}  {hunger_mood} energy {energy}  {self.energy_mood()}"


class Lion(Animal):
    def make_sound(self):
        return f"{self.name} says ROAR!"

class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} says OOH-OOH AH-AH!"

class Cow(Animal):
    def make_sound(self):
        return f"{self.name} says MOO!"

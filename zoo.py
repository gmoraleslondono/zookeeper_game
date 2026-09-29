class Zoo:
    def __init__(self, zookeeper, animals=None):
        self.zookeeper = zookeeper
        self.animals = animals if animals is not None else []

    def add_animal(self, animal):
        self.animals.append(animal)

    def pass_time(self):
        for animal in self.animals:
            animal.wait()

    def check_game_over(self):
        # If you get score 100 -> WIN
        if self.zookeeper.score >= 100:
            return "You win!"
        # If any animal gets hunger 100 -> LOOSE
        for animal in self.animals:
            if animal.hunger >= 100:
                return f"{animal.name} ran away. Game over!"
        # If food is 0 and coins less than 5 -> LOOSE
        if self.zookeeper.food == 0 and self.zookeeper.coins < 5:
            return "No food and no coins. Game over!"
        # Else keep playing
        return None

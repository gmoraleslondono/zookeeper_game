import colors
from zookeeper import WIN_SCORE

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
        if self.zookeeper.score >= WIN_SCORE:
            return f"{colors.GREEN}You win! The zoo is thriving 🎉 Score: {self.zookeeper.score}.{colors.RESET}"
        for animal in self.animals:
            if animal.hunger >= 100:
                return f"{colors.GREEN}{animal.name} was too hungry and ran away  😱  Game over!{colors.RESET}"
            if animal.energy <= 0:
                return f"{colors.GREEN}{animal.name} collapsed from exhaustion  💔  Game over!{colors.RESET}"
        if self.zookeeper.food == 0 and self.zookeeper.coins < self.zookeeper.FOOD_PRICE:
            return f"{colors.GREEN}No food and not enough coins to buy more  ☹️  Game over!{colors.RESET}"
        return None

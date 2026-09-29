class Zookeeper():
    def __init__(self, name, energy=100, coins=20, score=0):
        self.name = name
        self.energy = energy
        self.coins = coins
        self.score = score

    def spend_energy(self, amount):
        if self.energy < amount:
            raise ValueError(f"{self.name} is too tired.")

    def gain_energy(self, amount):
        self.energy = min(100, self.energy + amount)

    def gain_points(self, amount):
        self.score += amount

    def gain_coins(self, amount):
        self.coins += amount

    def spend_coins(self, amount):
        if self.coins < amount:
            raise ValueError(f"{self.name} doesn't have enough coins.")
        self.coins -= amount

    def __str__(self):
        return f"{self.name}: energy={self.energy}, coins={self.coins}, score={self.score}"

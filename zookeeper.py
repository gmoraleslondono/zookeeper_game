class Zookeeper():
    def __init__(self, name, energy = 100, coins = 20, score = 0):
        self.name = name
        self.energy = energy
        self.coins = coins
        self.score = score

    def __str__(self):
        return f"{self.name}: energy={self.energy}, coins={self.coins}, score={self.score}"

class Zookeeper():
    def __init__(self, name, energy = 100, coins = 20, score = 0):
        self.name = name
        self.energy = energy
        self.coins = coins
        self.score = score

    def feed(self, animal):
        # energy = -5
        # points = +10
        # coins = +5
        # food = -1
        return f"Feeding {animal}"

    def play(self, animal):
        # energy = -10
        # points = +8
        #coins = +3
        return f"Playing with {animal}"

    def send_sleep(self, animal):
        # energy = -5
        # points = +5
        #coins = +2
        return f"Sending to sleep {animal}"

    def buy_food(self):
        #coins = -5
        # food = +1
        return f"Buying food!"

    def rest(self):
        # energy = +30
        return f"Resting!"

    def __str__(self):
        return f"{self.name}: energy={self.energy}, coins={self.coins}, score={self.score}"

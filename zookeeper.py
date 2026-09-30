class Zookeeper():
    def __init__(self, name, energy=100, coins=20, score=0, food=3):
        self.name = name
        self.energy = energy
        self.coins = coins
        self.score = score
        self.food = food

    def spend_energy(self, amount):
        if self.energy < amount:
            raise ValueError(f"{self.name} is too tired.")
        self.energy -= amount

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

    def feed(self, animal):
        if self.food == 0:
            raise ValueError("No food left.")
        if self.energy < 5:
            raise ValueError(f"{self.name} is too tired.")
        animal.eat()
        self.spend_energy(5)
        self.food -= 1
        self.gain_points(10)
        self.gain_coins(5)
        return f"{animal.name} eats! +10 points, +5 coins"

    def play(self, animal):
        if self.energy < 10:
            raise ValueError(f"{self.name} is too tired.")
        animal.play()
        self.spend_energy(10)
        self.gain_points(8)
        self.gain_coins(3)
        return f"{self.name} plays with {animal.name}! +8 points, +3 coins"

    def send_sleep(self, animal):
        if self.energy < 5:
            raise ValueError(f"{self.name} is too tired.")
        animal.sleep()
        self.spend_energy(5)
        self.gain_points(5)
        self.gain_coins(2)
        return f"{animal.name} goes to sleep! +5 points, +2 coins"

    def listen(self, animal):
        self.spend_energy(1)
        sound = animal.make_sound()
        self.gain_points(2)
        self.gain_coins(1)
        return sound

    def buy_food(self):
        self.spend_coins(5)
        self.food += 1
        return f"{self.name} buys food. -5 coins, +1 food"

    def rest(self):
        self.gain_energy(30)
        return f"{self.name} takes a break and feels refreshed! +30 energy"

    def __str__(self):
        return f"{self.name}: energy={self.energy}, coins={self.coins}, score={self.score}, food={self.food}"

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
        self.spend_energy(5)
        animal.eat()
        self.food -= 1
        self.gain_points(10)
        self.gain_coins(5)

    def play(self, animal):
        self.spend_energy(10)
        animal.play()
        self.gain_points(8)
        self.gain_coins(3)

    def send_sleep(self, animal):
        self.spend_energy(5)
        animal.sleep()
        self.gain_points(5)
        self.gain_coins(2)

    def listen(self, animal):
        self.spend_energy(1)
        sound = animal.make_sound()
        self.gain_points(2)
        self.gain_coins(1)
        return sound

    def buy_food(self):
        self.spend_coins(5)
        self.food += 1

    def rest(self):
        self.gain_energy(30)

    def __str__(self):
        return f"{self.name}: energy={self.energy}, coins={self.coins}, score={self.score}"

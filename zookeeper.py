import colors

WIN_SCORE = 100

class Zookeeper():
    FOOD_PRICE = 8

    def __init__(self, name, energy=80, coins=16, score=0, food=3):
        self.name = name
        self.energy = energy
        self.coins = coins
        self.score = score
        self.food = food

    def spend_energy(self, amount):
        if self.energy < amount:
            raise ValueError(f"{colors.RED}{self.name} is too tired.{colors.RESET}")
        self.energy -= amount

    def gain_energy(self, amount):
        self.energy = min(100, self.energy + amount)

    def gain_points(self, amount):
        self.score += amount

    def gain_coins(self, amount):
        self.coins += amount

    def spend_coins(self, amount):
        if self.coins < amount:
            raise ValueError(f"{colors.RED}{self.name} doesn't have enough coins.{colors.RESET}")
        self.coins -= amount

    def feed(self, animal):
        if self.food == 0:
            raise ValueError(f"{colors.RED}No food left.{colors.RESET}")
        if self.energy < 10:
            raise ValueError(f"{colors.RED}{self.name} is too tired.{colors.RESET}")
        animal.eat()
        self.spend_energy(10)
        self.food -= 1
        self.gain_points(20)
        self.gain_coins(4)
        return f"{colors.YELLOW}{animal.name} eats! +20 points, +4 coins{colors.RESET}"

    def play(self, animal):
        if self.energy < 12:
            raise ValueError(f"{colors.RED}{self.name} is too tired.{colors.RESET}")
        animal.play()
        self.spend_energy(12)
        self.gain_points(15)
        self.gain_coins(6)
        return f"{colors.YELLOW}{self.name} plays with {animal.name}! +15 points, +6 coins{colors.RESET}"

    def send_sleep(self, animal):
        if self.energy < 8:
            raise ValueError(f"{colors.RED}{self.name} is too tired.{colors.RESET}")
        animal.sleep()
        self.spend_energy(8)
        self.gain_points(10)
        self.gain_coins(2)
        return f"{animal.name} goes to sleep and will wake up hungrier. +10 points, +2 coins"

    def listen(self, animal):
        self.spend_energy(2)
        sound = animal.make_sound()
        self.gain_points(5)
        self.gain_coins(2)
        return f"{colors.YELLOW}{sound} +5 points, +2 coins{colors.RESET}"

    def buy_food(self):
        self.spend_coins(self.FOOD_PRICE)
        self.food += 1
        return f"{colors.YELLOW}{self.name} buys food. -{self.FOOD_PRICE} coins, +1 food{colors.RESET}"

    def rest(self):
        self.gain_energy(40)
        return f"{self.name} takes a break and feels refreshed! +40 energy"

    def __str__(self):
        return (
            f"🙂 {self.name}   energy {self.energy}   coins {self.coins}   "
            f"food {self.food}   score {self.score}/{WIN_SCORE}"
        )

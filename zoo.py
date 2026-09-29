class Zoo:
    def __init__(self, zookeeper, food=3, animals=None):
        self.zookeeper = zookeeper
        self.food = food
        self.animals = animals if animals is not None else []

    def order_food(self):
        # food = +1
        if self.zookeeper.coins < 5:
            raise ValueError("Not enough coins to buy food.")
        self.zookeeper.coins =  self.zookeeper.coins - 5
        self.food = self.food + 1
        print("Ordering food")

    def pass_time(self):
        for animal in self.animals:
            animal.wait()

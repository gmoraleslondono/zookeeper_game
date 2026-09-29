def show_status(zoo):
    print(zoo.zookeeper)
    for animal in zoo.animals:
        print(animal)

def show_menu():
    print("Hi dear zookeeper, what do you want to do today? ")
    return input("(1)Feed, (2)Play, (3)Send to sleep, (4)Listen, (5)Buy food, (6)Rest, (7)Quit: ")

def choose_animal(zoo):
    for position, animal in enumerate(zoo.animals, start=1):
        print(f"{position}. {animal}")

    text = input("What animal do you want to visit (write a number): ")

    if not text.isdigit():
        raise ValueError("You should type a number.")

    number = int(text)

    if number > len(zoo.animals) or number <= 0:
        raise ValueError("You should choose an animal from the list.")

    return zoo.animals[number-1]

def run():
    # it should run the program and make the validations
    pass

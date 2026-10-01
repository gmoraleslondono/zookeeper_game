def show_status(zoo):
    print()
    print(zoo.zookeeper)
    print()
    for animal in zoo.animals:
        print(animal)

def show_menu():
    print()
    print("1 Feed   2 Play   3 put to sleep   4 Listen   5 Buy food   6 Rest   7 Quit")
    text = input("> ")

    if not text.isdigit():
        print()
        raise ValueError("Type a number from 1 to 7.")

    number = int(text)

    return number

def choose_animal(zoo):
    print()
    print("Who is getting a visit? Pick a number:")
    for position, animal in enumerate(zoo.animals, start=1):
        print(f"{position} {animal.name}   ", end= " ")

    text = input("\n> ")

    if not text.isdigit():
        print()
        raise ValueError("Type a number from 1 to 3.")

    number = int(text)

    if number > len(zoo.animals) or number <= 0:
        print()
        raise ValueError("Choose an animal from the list by typing a number.")

    return zoo.animals[number-1]

def run(zoo):
    run = True

    while run == True:
        try:
            show_status(zoo)
            choice = show_menu()

            if choice == 7:
                print("--------------------------------")
                print("Game over! Goodbye 👋 ")
                print("--------------------------------")
                run = False
                continue

            #(1)Feed, (2)Play, (3)Send to sleep, (4)Listen, (5)Buy food, (6)Rest
            if choice == 1:
                animal = choose_animal(zoo)
                message = zoo.zookeeper.feed(animal)
                print(" ")
                print(message)
            elif choice == 2:
                animal = choose_animal(zoo)
                message = zoo.zookeeper.play(animal)
                print(" ")
                print(message)
            elif choice == 3:
                animal = choose_animal(zoo)
                message = zoo.zookeeper.send_sleep(animal)
                print(" ")
                print(message)
            elif choice == 4:
                animal = choose_animal(zoo)
                sound = zoo.zookeeper.listen(animal)
                print(" ")
                print(sound)
            elif choice == 5:
                message = zoo.zookeeper.buy_food()
                print(" ")
                print(message)
            elif choice == 6:
                message = zoo.zookeeper.rest()
                print(" ")
                print(message)
            else:
                print()
                print("Invalid option.")
                continue

            zoo.pass_time()

        except ValueError as error:
            print(error)
            continue

        message = zoo.check_game_over()
        if message is not None:
            print()
            print("--------------------------------------------")
            print(message)
            print("--------------------------------------------")
            print()
            run = False


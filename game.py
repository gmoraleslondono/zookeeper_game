def show_status(zoo):
    print(" ")
    print("-----------------------------------------------")
    print(zoo.zookeeper)
    print("-----------------------------------------------")
    for animal in zoo.animals:
        print(animal)
    print("--------------------------------")

def show_menu(zoo):
    print(" ")
    print(f"Hi {zoo.zookeeper.name} what do you want to do? ")
    text = input("(1)Feed, (2)Play, (3)Send to sleep, (4)Listen, (5)Buy food, (6)Rest, (7)Quit: ")

    if not text.isdigit():
        raise ValueError("You should type a number.")

    number = int(text)

    return number

def choose_animal(zoo):
    print(" ")
    for position, animal in enumerate(zoo.animals, start=1):
        print(f"{position}. {animal}")

    text = input("What animal do you want to visit (write a number): ")

    if not text.isdigit():
        raise ValueError("You should type a number.")

    number = int(text)

    if number > len(zoo.animals) or number <= 0:
        raise ValueError("You should choose an animal from the list.")

    return zoo.animals[number-1]

def run(zoo):
    run = True

    while run == True:
        try:
            show_status(zoo)
            choice = show_menu(zoo)

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
                zoo.zookeeper.rest()
            else:
                print("Invalid option")
                continue

            zoo.pass_time()

        except ValueError as error:
            print(error)
            continue

        message = zoo.check_game_over()
        if message is not None:
            print(message)
            run = False


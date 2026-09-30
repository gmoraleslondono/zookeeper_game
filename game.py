def show_status(zoo):
    print(zoo.zookeeper)
    for animal in zoo.animals:
        print(animal)

def show_menu():
    print("Hi dear zookeeper, what do you want to do today? ")
    text = input("(1)Feed, (2)Play, (3)Send to sleep, (4)Listen, (5)Buy food, (6)Rest, (7)Quit: ")

    if not text.isdigit():
        raise ValueError("You should type a number.")

    number = int(text)

    return number

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

def run(zoo):
    run = True

    while run == True:
        show_status(zoo)
        choice = show_menu()

        if choice == 7:
            print("Game over! Goodbye 👋 ")
            run = False
            continue

        try:
            #(1)Feed, (2)Play, (3)Send to sleep, (4)Listen, (5)Buy food, (6)Rest
            if choice == 1:
                animal = choose_animal(zoo)
                zoo.zookeeper.feed(animal)
            elif choice == 2:
                animal = choose_animal(zoo)
                zoo.zookeeper.play(animal)
            elif choice == 3:
                animal = choose_animal(zoo)
                zoo.zookeeper.send_sleep(animal)
            elif choice == 4:
                animal = choose_animal(zoo)
                zoo.zookeeper.listen(animal)
            elif choice == 5:
                zoo.zookeeper.buy_food()
            elif choice == 6:
                zoo.zookeeper.rest()
            else:
                print("Invalid option")
                continue

            zoo.pass_time()

        except ValueError as error:
            print(error)

        message = zoo.check_game_over()
        if message is not None:
            print(message)
            run = False


# Zoo Game

A small command-line game written in Python. You play as a zookeeper looking after three animals: Leo the lion, Momo the monkey, and Bella the cow. Feed them, play with them, and let them rest before they get too hungry or too tired.

You earn points and coins for taking care of the animals. Reach 100 points to win.

## Requirements

- Python 3

The game uses only the Python standard library. There is nothing to install.

## Run it locally

1. Clone this repository and open a terminal in the project folder.

```bash
https://github.com/gmoraleslondono/zookeeper_game
```

2. Start the game:

```bash
python3 main.py
```

3. Type your name when asked, then choose actions by typing a number.

4. To stop early, choose option `7` (Quit).

## How to play

Each turn the game shows your status and the status of every animal, then asks what you want to do.

| Choice | Action                  | What it costs       | What you gain         |
| ------ | ----------------------- | ------------------- | --------------------- |
| 1      | Feed an animal          | 5 energy and 1 food | 10 points and 5 coins |
| 2      | Play with an animal     | 10 energy           | 8 points and 3 coins  |
| 3      | Send an animal to sleep | 5 energy            | 5 points and 2 coins  |
| 4      | Listen to an animal     | 1 energy            | 2 points and 1 coin   |
| 5      | Buy food                | 5 coins             | 1 food                |
| 6      | Rest                    | nothing             | 30 energy (up to 100) |
| 7      | Quit                    | —                   | ends the game         |

After every action except Quit, time passes. Every animal gets a little hungrier (`+5` hunger) and a little more tired (`-5` energy).

You start with:

- **Zookeeper:** 100 energy, 20 coins, 0 points, 3 food
- **Each animal:** 50 hunger, 50 energy

Hunger and energy stay between 0 and 100.

Some actions are refused if they do not make sense. For example, a full animal will not eat, a tired animal will not play, and you cannot buy food without 5 coins. The game prints the reason and lets you try again.

## Winning and losing

**You win** when your score reaches 100.

**You lose** when any of these happen:

- An animal's hunger reaches 100. It runs away.
- An animal's energy reaches 0. It gets sick.
- You have no food left and fewer than 5 coins, so you cannot buy more.

## Project layout

| File           | Role                                                             |
| -------------- | ---------------------------------------------------------------- |
| `main.py`      | Starts the game, asks for your name, and creates the zoo         |
| `game.py`      | The turn loop: status, menu, and win or loss checks              |
| `zookeeper.py` | The player's energy, coins, score, food, and actions             |
| `zoo.py`       | The list of animals, the passing of time, and the end conditions |
| `animals.py`   | Shared animal behavior. The lion, monkey, and cow                |

## License

MIT. See [LICENSE](LICENSE).

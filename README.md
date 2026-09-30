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

| Choice | Action                  | What it costs       | What you gain          |
| ------ | ----------------------- | ------------------- | ---------------------- |
| 1      | Feed an animal          | 10 energy and 1 food | 20 points and 4 coins |
| 2      | Play with an animal     | 12 energy           | 15 points and 6 coins  |
| 3      | Send an animal to sleep | 8 energy            | 10 points and 2 coins  |
| 4      | Listen to an animal     | 2 energy            | 5 points and 2 coins   |
| 5      | Buy food                | 8 coins             | 1 food                 |
| 6      | Rest                    | nothing             | 40 energy (up to 100)  |
| 7      | Quit                    | —                   | ends the game          |

Feeding is the best way to score. Playing is the best way to earn coins. A meal fills an animal a lot (`-40` hunger). Play tires them out (`-20` energy, `+12` hunger) and they need at least 35 energy to join in. Sleep restores 50 energy, and they wake up a little hungrier (`+10` hunger).

After every action except Quit, time passes. Every animal gets hungrier (`+8` hunger) and more tired (`-8` energy).

You start with:

- **Zookeeper:** 80 energy, 16 coins, 0 points, 3 food
- **Each animal:** 45 hunger, 60 energy

Hunger and energy stay between 0 and 100. The status line shows a mood as well as the number: hunger goes from satisfied to ok, hungry, and starving; energy goes from lively to ok, tired, and exhausted. Your score is shown against the goal, like `score=40/100`.

Some actions are refused if they do not make sense. For example, a full animal will not eat, a tired animal will not play, and you cannot buy food without 8 coins. The game prints the reason and lets you try again.

## Winning and losing

**You win** when your score reaches 100.

**You lose** when any of these happen:

- An animal's hunger reaches 100. It runs away.
- An animal's energy reaches 0. It collapses.
- You have no food left and fewer than 8 coins, so you cannot buy more.

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

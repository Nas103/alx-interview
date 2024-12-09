# Prime Game

## Description
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game. They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, this project determines who the winner of each game is.

## Getting Started

### Prerequisites
- Python 3.4.3 or higher
- pip

### Installing
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/alx-interview.git
    cd alx-interview/0x0A-primegame
    ```

2. Install any required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Game
To determine the winner of the game, use the `isWinner` function.

### Usage
```python
from prime_game import isWinner

x = 5
nums = [2, 5, 1, 4, 3]
winner = isWinner(x, nums)
print("Winner:", winner)

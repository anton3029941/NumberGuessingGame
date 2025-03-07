Number Guessing Game

# Description

Number Guessing Game is a command-line game where the player must guess a number between 1 and 100 within a limited number of attempts.
The game supports difficulty selection and saves the best results.  
Project for roadmap.sh https://roadmap.sh/projects/number-guessing-game

Game Rules

The computer randomly selects a number between 1 and 100.

Depending on the chosen difficulty, you have 10, 5, or 3 attempts.

After each attempt, the game provides a hint whether the number is higher or lower.

In the last 2 attempts, the game provides a range where the number is located.

If you guess correctly, the game saves your result.

If you run out of attempts, the game ends and reveals the correct number.

# Record System

After winning, your result is saved in records.json. The following records are tracked:

Best Time (shortest time to guess).

Fewest Attempts (quickest correct guess).

Overall Best Result (both fastest and fewest attempts).

# Requirements

Python 3.x

# License

MIT License


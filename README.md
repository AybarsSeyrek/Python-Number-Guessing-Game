# Python-Number-Guessing-Game
This is a terminal-based Python number guessing game. The game lets players choose a difficulty level, guess a randomly generated number, receive hints, track attempts, and save high scores using JSON file storage. This project demonstrates core Python programming skills such as functions, loops, conditionals, input validation, random number generation, JSON file handling, error handling, sorting, and modular program organization.

---

## Features

- Main menu system
- Player name input
- Difficulty levels:
  - Easy: 1 to 50, 10 attempts
  - Medium: 1 to 100, 7 attempts
  - Hard: 1 to 200, 5 attempts
- Random number generation
- Limited attempts based on difficulty
- Input validation for menu choices, difficulty selection, and guesses
- Too high / too low feedback
- Hint system based on how close the guess is
- Score calculation based on attempts used
- High-score saving using JSON
- Option to view previous high scores
- Play-again option
- High scores saved in `number_guessing_scores.json`
- Main game code stored in `number_guessing_game.py`

---

## Project Structure

```text
Python-Number-Guessing-Game/
│
├── number_guessing_game.py
├── number_guessing_scores.json
└── README.md
```

### `number_guessing_game.py`

The main Python file that contains the game logic, including the menu system, difficulty selection, random number generation, guess checking, scoring, high-score saving, and high-score viewing.

### `number_guessing_scores.json`

Stores saved player scores. This file is created automatically after a player completes a game.

### `README.md`

Explains the project, features, structure, and Python concepts demonstrated.

---

## How to Run

Make sure `number_guessing_game.py` is in your project folder.

Run the program with:

```bash
python number_guessing_game.py
```

or:

```bash
python3 number_guessing_game.py
```

---

## How the Game Works

1. The player starts at the main menu.
2. The player chooses to start the game, view high scores, or exit.
3. If the player starts a game, they enter their name.
4. The player chooses a difficulty level.
5. The computer randomly generates a secret number within the selected range.
6. The player guesses numbers until they guess correctly or run out of attempts.
7. The game gives feedback such as “too high,” “too low,” and hints based on how close the guess is.
8. If the player guesses correctly, the game calculates a score based on how many attempts were used.
9. The result is saved to `number_guessing_scores.json`.
10. The player can choose to play again or exit.

---

## Technical Concepts Demonstrated

### Functions and Modular Code Organization

The program is divided into functions such as `display_menu()`, `choose_difficulty()`, `play_game()`, `save_high_score()`, and `view_high_scores()`.

This keeps the code organized, easier to read, and easier to update.

### Random Number Generation

The game uses Python’s `random.randint()` function to generate a secret number within the selected difficulty range.

```python
answer = random.randint(lowest_num, highest_num)
```

This demonstrates how randomness can be used to create a different game experience each time the program runs.

### Difficulty Levels

The game changes the number range and maximum attempts based on the selected difficulty.

For example:

```python
return "Easy", 1, 50, 10
```

This demonstrates how function return values can be used to control game settings.

### Input Validation

The game checks user input to make sure the player enters valid menu choices, difficulty choices, and number guesses.

For example, guesses must be numeric and inside the allowed range.

```python
if guess.isdigit():
    guess = int(guess)
```

This prevents invalid input from crashing the program or being accepted incorrectly.

### Loops and Game Flow

The game uses `while` loops to keep the program running until the player exits and to continue a round until the player wins or runs out of attempts.

```python
while attempts_used < max_attempts:
```

This demonstrates how loops can control repeated gameplay actions.

### Conditional Statements

The program uses `if`, `elif`, and `else` statements to compare the player’s guess to the correct answer.

```python
if guess < answer:
    print("Too low! Try again.")
elif guess > answer:
    print("Too high! Try again.")
else:
    print("Correct!")
```

This demonstrates decision-making logic in Python.

### Hint System

The game gives hints based on how close the player’s guess is to the correct answer.

```python
difference = abs(answer - guess)
```

The `abs()` function is used to calculate the distance between the guess and the answer.

This demonstrates arithmetic, comparison logic, and conditionals.

### Score Calculation

The game calculates a score based on how many attempts the player used.

```python
score = int(((max_attempts - attempts_used + 1) / max_attempts) * 100)
```

This rewards players for guessing the number in fewer attempts and demonstrates arithmetic operations and score tracking.

### JSON High-Score Saving

The game saves player results to `number_guessing_scores.json`.

Each saved score includes:

- Player name
- Difficulty
- Score
- Attempts used
- Maximum attempts
- Result
- Date and time

```python
json.dump(high_scores, file, indent=4)
```

This demonstrates file handling and saving data after the program ends.

### Viewing and Sorting High Scores

The game can load previous scores and display them from highest to lowest.

```python
sorted_scores = sorted(
    high_scores,
    key=lambda score_data: score_data["score"],
    reverse=True
)
```

This demonstrates sorting a list of dictionaries and using a lambda function.

### Error Handling

The program uses `try` and `except` blocks when reading the JSON score file.

```python
try:
    with open(HIGH_SCORE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
except json.JSONDecodeError:
    return []
```

This prevents the program from crashing if the file is empty or incorrectly formatted.

### Date and Time Tracking

The game records when each score was saved using Python’s `datetime` module.

```python
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

This adds useful information to each high-score entry.

---

## Python Concepts Practiced

This project demonstrates the following Python concepts:

- Variables
- Constants
- Functions
- Loops
- Conditional statements
- User input
- Input validation
- Random number generation
- Arithmetic operations
- File handling
- JSON reading and writing
- Error handling with `try` and `except`
- Lists
- Dictionaries
- Sorting with `sorted()`
- Lambda functions
- Date and time with the `datetime` module
- Modular project organization

---

## Standard Libraries Used

This project only uses Python standard libraries.

```python
import random
import json
import os
from datetime import datetime
```

### `random`

Used to generate the secret number.

### `json`

Used to save and load high scores.

### `os`

Used to check whether the high-score file exists before opening it.

### `datetime`

Used to save the date and time of each game result.

---

## What I Learned

While building this project, I practiced creating a complete terminal-based Python game with organized code and persistent score storage.

I learned how to use functions to structure a program, validate user input, generate random numbers, create difficulty settings, calculate scores, save results with JSON, and handle possible file errors safely.

# Python Number Guessing Game
# It includes a menu, difficulty levels, limited attempts, hints,
# score saving, and high-score viewing.

import random
import json
import os
from datetime import datetime


# This file will store the player's previous scores.
HIGH_SCORE_FILE = "number_guessing_scores.json"


def display_menu():
    # This is the main menu the player sees when the program starts.
    print("=" * 45)
    print("        PYTHON NUMBER GUESSING GAME")
    print("=" * 45)
    print("1. Start Game")
    print("2. View High Scores")
    print("3. Exit")
    print("=" * 45)


def get_menu_choice():
    # Keep asking until the player chooses a valid menu option.
    while True:
        choice = input("Choose an option: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("Invalid choice. Please enter 1, 2, or 3.")


def get_player_name():
    # The player's name is saved with their score.
    while True:
        name = input("Enter your name: ").strip()

        if name:
            return name

        print("Name cannot be empty.")


def choose_difficulty():
    # Each difficulty changes the number range and the number of attempts.
    print("\nChoose a difficulty:")
    print("1. Easy   - Guess 1 to 50, 10 attempts")
    print("2. Medium - Guess 1 to 100, 7 attempts")
    print("3. Hard   - Guess 1 to 200, 5 attempts")

    while True:
        choice = input("Enter difficulty number: ").strip()

        if choice == "1":
            return "Easy", 1, 50, 10
        elif choice == "2":
            return "Medium", 1, 100, 7
        elif choice == "3":
            return "Hard", 1, 200, 5

        print("Invalid choice. Please enter 1, 2, or 3.")


def get_valid_guess(lowest_num, highest_num):
    # This function makes sure the player enters a real number
    # and that the number is inside the allowed range.
    while True:
        guess = input(f"Enter your guess ({lowest_num}-{highest_num}): ").strip()

        if guess.isdigit():
            guess = int(guess)

            if lowest_num <= guess <= highest_num:
                return guess
            else:
                print(f"Out of range. Please choose between {lowest_num} and {highest_num}.")
        else:
            print("Invalid input. Please enter a number.")


def give_hint(answer, guess):
    # This gives the player a small clue based on how close their guess is.
    difference = abs(answer - guess)

    if difference <= 5:
        print("Hint: You are very close!")
    elif difference <= 15:
        print("Hint: You are getting close.")
    else:
        print("Hint: You are far away.")


def calculate_score(attempts_used, max_attempts):
    # The fewer attempts the player uses, the higher their score will be.
    score = int(((max_attempts - attempts_used + 1) / max_attempts) * 100)
    return score


def play_game():
    # This function controls one full round of the game.
    player_name = get_player_name()
    difficulty, lowest_num, highest_num, max_attempts = choose_difficulty()

    # The computer randomly chooses the secret number.
    answer = random.randint(lowest_num, highest_num)

    attempts_used = 0
    won_game = False

    print("\nGame Started!")
    print(f"I am thinking of a number between {lowest_num} and {highest_num}.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    # The game continues until the player wins or runs out of attempts.
    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used
        print(f"Attempts left: {attempts_left}")

        guess = get_valid_guess(lowest_num, highest_num)
        attempts_used += 1

        if guess < answer:
            print("Too low! Try again.")
            give_hint(answer, guess)

        elif guess > answer:
            print("Too high! Try again.")
            give_hint(answer, guess)

        else:
            # The player guessed the correct number.
            won_game = True
            score = calculate_score(attempts_used, max_attempts)

            print("\nCorrect!")
            print(f"The answer was {answer}.")
            print(f"You guessed it in {attempts_used} attempt(s).")
            print(f"Score: {score}%")

            save_high_score(player_name, difficulty, score, attempts_used, max_attempts, won_game)
            break

        print()

    # This runs only if the player uses all attempts without guessing correctly.
    if not won_game:
        score = 0
        print("\nGame Over!")
        print(f"You ran out of attempts. The correct answer was {answer}.")
        save_high_score(player_name, difficulty, score, attempts_used, max_attempts, won_game)


def load_high_scores():
    # If the score file does not exist yet, start with an empty list.
    if not os.path.exists(HIGH_SCORE_FILE):
        return []

    try:
        with open(HIGH_SCORE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    # If the JSON file is empty or broken, avoid crashing the program.
    except json.JSONDecodeError:
        return []


def save_high_score(player_name, difficulty, score, attempts_used, max_attempts, won_game):
    # Load old scores first so we do not erase them.
    high_scores = load_high_scores()

    # Store the current game's result as a dictionary.
    new_score = {
        "name": player_name,
        "difficulty": difficulty,
        "score": score,
        "attempts_used": attempts_used,
        "max_attempts": max_attempts,
        "result": "Won" if won_game else "Lost",
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Add the new score to the list of previous scores.
    high_scores.append(new_score)

    # Save the updated score list back into the JSON file.
    with open(HIGH_SCORE_FILE, "w", encoding="utf-8") as file:
        json.dump(high_scores, file, indent=4)

    print(f"\nScore saved to {HIGH_SCORE_FILE}.")


def view_high_scores():
    # This displays saved scores from the JSON file.
    high_scores = load_high_scores()

    if not high_scores:
        print("\nNo high scores found yet.")
        return

    # Sort scores from highest to lowest.
    sorted_scores = sorted(
        high_scores,
        key=lambda score_data: score_data["score"],
        reverse=True
    )

    print("\n" + "=" * 45)
    print("              HIGH SCORES")
    print("=" * 45)

    # Only show the top 10 scores so the list does not get too long.
    for index, score_data in enumerate(sorted_scores[:10], start=1):
        print(f"{index}. {score_data['name']}")
        print(f"   Difficulty: {score_data['difficulty']}")
        print(f"   Score: {score_data['score']}%")
        print(f"   Attempts: {score_data['attempts_used']}/{score_data['max_attempts']}")
        print(f"   Result: {score_data['result']}")
        print(f"   Date: {score_data['date_time']}")
        print("-" * 45)


def ask_play_again():
    # Ask the player if they want another round after finishing a game.
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False

        print("Please enter yes or no.")


def main():
    # This is the main program loop.
    # It keeps the game running until the player chooses to exit.
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            play_game()

            if not ask_play_again():
                print("\nThanks for playing!")
                break

        elif choice == "2":
            view_high_scores()

        elif choice == "3":
            print("\nGoodbye!")
            break


# This makes sure the game starts only when this file is run directly.
if __name__ == "__main__":
    main()

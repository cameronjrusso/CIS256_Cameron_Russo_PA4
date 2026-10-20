# Cameron Russo
# CIS256 Fall 2026
# Programming Assignment 4

import random

# The computer picks one of these words at the start of each game.
WORDS = ["banana", "python", "planet", "garden", "puzzle", "laptop"]
MAX_ATTEMPTS = 6


def choose_word():
    """Pick a random word from our list."""
    return random.choice(WORDS)


def check_guess(word, letter):
    """Return True when the guessed letter is in the word."""
    return letter in word


def display_word(word, guessed_letters):
    """Show guessed letters and hide the others with underscores."""
    # Checking each position also reveals letters that appear more than once.
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game():
    """Run the game until the player wins or uses all six wrong guesses."""
    secret_word = choose_word()
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("Welcome to Guess the Word!")
    print(f"You can make {MAX_ATTEMPTS} incorrect guesses.")

    while attempts_left > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Incorrect guesses left:", attempts_left)
        guess = input("Guess one letter: ").strip().lower()

        # Ignore invalid input without taking away an attempt.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter just one letter.")
            continue

        # A repeated guess should not count as a new incorrect attempt.
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if check_guess(secret_word, guess):
            print("Good guess! That letter is in the word.")

            # The order of guesses does not matter, only whether all letters are found.
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\nCongratulations! You guessed the word: {secret_word}")
                return
        else:
            attempts_left -= 1
            print("Sorry, that letter is not in the word.")

    print(f"\nGame over! The word was: {secret_word}")


# This keeps the game from starting when pytest imports this file.
if __name__ == "__main__":
    play_game()

"""
Mystery Word – A simple word‑guessing game 🎯
-------------------------------------------------
Final Project for Code in Place 2025
Author: <your‑name‑here>
Date: June 2025

How to play
-----------
• The computer randomly chooses a secret English word.
• You have 8 wrong guesses to uncover every letter.
• Type one letter per turn (A‑Z).  Repeats don’t cost lives.
• If you reveal every letter before your guesses run out – you win!

This project shows off:
• Lists, sets, strings, and control flow ❤︎
• Random selection from a list of words
• Cleanly‑factored functions and constants
• Clear console UI that works in the Code in Place IDE or any terminal

Extensions you could add
------------------------
✓ A graphical version using the CIP graphics library.
✓ A "hints" command that reveals a random unrevealed letter.
✓ Saving high‑scores to a file.
✓ Allowing whole‑word guesses for extra risk/reward.
✓ Colourful ANSI escape sequences for a fancier console.
"""

import random
import string

# --- Game configuration constants -------------------------------------------
MAX_WRONG_GUESSES = 8
WORD_LIST = [
    "PYTHON", "STANFORD", "KAREL", "COMPUTER", "PROGRAM", "FUNCTION",
    "VARIABLE", "LOOP", "STRING", "DICTIONARY", "GRAPHICS", "ROBOT",
    "DEBUG", "ALGORITHM", "CS106A", "HACKATHON", "KEYBOARD", "MONITOR",
    "SOFTWARE", "HARDWARE"
]

# ----------------------------------------------------------------------------

def choose_secret_word() -> str:
    """Return a random word in UPPER‑CASE from WORD_LIST."""
    return random.choice(WORD_LIST)


def initialise_display(secret: str) -> list[str]:
    """Return a list of dashes (one per letter) to show game progress."""
    return ["-" for _ in secret]


def update_display(secret: str, display: list[str], guess: str) -> None:
    """Reveal all positions of *guess* found in *secret* by editing *display*."""
    for index, letter in enumerate(secret):
        if letter == guess:
            display[index] = guess


def formatted_display(display: list[str]) -> str:
    """Return the current display list as a single spaced string, e.g. "A - – R"."""
    return " ".join(display)


def get_valid_guess(used: set[str]) -> str:
    """Prompt the player until they provide a single unused alphabetic letter."""
    while True:
        guess = input("Type a single letter here, then press Enter: ").strip().upper()
        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("⚠️  Please type *one* English letter (A–Z). Try again.")
            continue
        if guess in used:
            print("🔁 You already guessed that letter. It won’t cost you, but pick another.")
            continue
        return guess


def play_round() -> None:
    """Plays one complete game round, then asks the player if they want to replay."""
    secret = choose_secret_word()
    display = initialise_display(secret)
    used_letters: set[str] = set()
    wrong_guesses_left = MAX_WRONG_GUESSES

    print("\n🎉 Welcome to Mystery Word! 🎉\n")

    while wrong_guesses_left > 0 and "-" in display:
        print(f"The word now looks like this: {formatted_display(display)}")
        print(f"You have {wrong_guesses_left} wrong guess{'es' if wrong_guesses_left != 1 else ''} left")
        print(f"Used letters: {' '.join(sorted(used_letters)) if used_letters else '(none)'}")
        guess = get_valid_guess(used_letters)
        used_letters.add(guess)

        if guess in secret:
            print("✅ That guess is correct!\n")
            update_display(secret, display, guess)
        else:
            wrong_guesses_left -= 1
            print("❌ Sorry, that letter is not in the word.\n")

    # --- Round finished ------------------------------------------------------
    if "-" not in display:
        print(f"🏆 Congratulations! You guessed the word: {secret}")
    else:
        print(f"💀 Out of guesses. The word was: {secret}")


def main() -> None:
    """Entry‑point that lets the player play multiple rounds if desired."""
    while True:
        play_round()
        again = input("Play again? (Y/N): ").strip().upper()
        if again != "Y":
            print("Thanks for playing Mystery Word. Goodbye!")
            break


# Run the game when executed directly ----------------------------------------
if __name__ == "__main__":
    main()

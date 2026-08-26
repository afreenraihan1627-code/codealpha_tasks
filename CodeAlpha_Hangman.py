import random

# Predefined list of words
WORDS = ["python", "hangman", "computer", "keyboard", "program"]

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]


def choose_word():
    """Randomly pick a word from the list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("       WELCOME TO HANGMAN!")
    print("=" * 40)
    print(f"The word has {len(word)} letters. You have {MAX_ATTEMPTS} wrong guesses allowed.\n")

    while wrong_guesses < MAX_ATTEMPTS:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: ", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
        print(f"Wrong guesses remaining: {MAX_ATTEMPTS - wrong_guesses}\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️  You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.\n")

    else:
        # Loop ended because wrong_guesses reached MAX_ATTEMPTS
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"💀 Game Over! You've run out of attempts. The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("\nThanks for playing Hangman! Goodbye 👋")


if __name__ == "__main__":
    main()     
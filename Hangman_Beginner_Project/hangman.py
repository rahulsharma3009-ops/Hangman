import random

# Hangman game - a simple beginner project

def show_hangman(wrong_guesses):
    stages = [
        """
          _______
          |     |
                |
                |
                |
                |
        =========
        """,
        """
          _______
          |     |
          O     |
                |
                |
                |
        =========
        """,
        """
          _______
          |     |
          O     |
          |     |
                |
                |
        =========
        """,
        """
          _______
          |     |
          O     |
         /|     |
                |
                |
        =========
        """,
        """
          _______
          |     |
          O     |
         /|\\    |
                |
                |
        =========
        """,
        """
          _______
          |     |
          O     |
         /|\\    |
         /      |
                |
        =========
        """,
        """
          _______
          |     |
          O     |
         /|\\    |
         / \\    |
                |
        =========
        """
    ]
    print(stages[wrong_guesses])


def choose_word():
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            words = [word.strip().lower() for word in file if word.strip().isalpha()]
        words = [word for word in words if 4 <= len(word) <= 10]
        if words:
            return random.choice(words)
    except FileNotFoundError:
        pass

    # Backup words in case words.txt is missing
    words = ["python", "computer", "garden", "school", "planet", "pencil"]
    return random.choice(words)


def play_game():
    secret_word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n=== HANGMAN GAME ===")
    print("Guess the hidden word one letter at a time.")
    print("You can make up to 6 wrong guesses.\n")

    while wrong_guesses < max_attempts:
        show_hangman(wrong_guesses)

        # Show guessed letters and blanks for letters not guessed yet
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter.upper() + " "
            else:
                display_word += "_ "
        print("Word:", display_word.strip())
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print("Wrong guesses left:", max_attempts - wrong_guesses)

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter just one letter (A-Z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Sorry, that letter is not in the word.\n")

        # Check if all letters have been guessed
        if all(letter in guessed_letters for letter in secret_word):
            show_hangman(wrong_guesses)
            print("Word:", " ".join(secret_word.upper()))
            print("Congratulations! You guessed the word!")
            return

    show_hangman(wrong_guesses)
    print("Game over! The word was:", secret_word.upper())


if __name__ == "__main__":
    play_game()

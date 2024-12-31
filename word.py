import random

def word_guess_game():
    """A simple word guessing game."""
    print("Welcome to the Word Guess Game!")
    print("Guess the correct word letter by letter.")

    # List of words to guess
    words = ['python', 'photography', 'developer', 'software', 'company']
    secret_word = random.choice(words)  # Randomly select a word
    guessed_word = ['_'] * len(secret_word)  # Placeholder for guessed letters

    attempts = len(secret_word) + 3  # Allow extra attempts
    guessed_letters = set()

    print(f"The word has {len(secret_word)} letters: {' '.join(guessed_word)}")

    while attempts > 0 and '_' in guessed_word:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

        print(f"Word: {' '.join(guessed_word)}")
        print(f"Attempts remaining: {attempts}")

    if '_' not in guessed_word:
        print(f"Congratulations! You guessed the word: {''.join(guessed_word)}")
    else:
        print(f"Game over! The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    word_guess_game()

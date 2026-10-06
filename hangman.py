import random

# List of predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Maximum wrong guesses
wrong_guesses = 0

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 wrong guesses.")

while wrong_guesses < 6 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses)

    guess = input("Guess a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    # Check the guessed letter
    if guess in word:

        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:

        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
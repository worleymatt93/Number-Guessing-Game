from random import randint


# Returns number of lives based on difficulty level
def get_lives(level):
    return 10 if level == "easy" else 5


# Game intro
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
# Chooses a random number between 1 and 100 to be guessed
GAME_NUMBER = randint(1, 100)

# Get difficulty and set lives accordingly
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = get_lives(difficulty)

# Main game loop
while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    if guess == GAME_NUMBER:
        print(f"You got it! The answer was {GAME_NUMBER}.")
        break  # Exit loop if guessed correctly
    else:
        lives -= 1  # Deduct a life for incorrect guesses
        print("Too high." if guess > GAME_NUMBER else "Too low.")
        if lives == 0:
            print("You've run out of guesses. Game over.")
        else:
            print("Guess again.")

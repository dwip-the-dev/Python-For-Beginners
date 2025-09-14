import random

def number_guessing_game():
    """Plays a number guessing game with the user."""
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    won = False

    while attempts < max_attempts:
        try:
            guess_str = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")
            guess = int(guess_str)

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue # Skip incrementing attempts for invalid range input

            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                won = True
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            # Do not increment attempts for invalid input type

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
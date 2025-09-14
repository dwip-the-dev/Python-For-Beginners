import random

def play_game():
    """Plays a single round of Rock, Paper, Scissors."""
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Validate player input
    while player_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    play_game()
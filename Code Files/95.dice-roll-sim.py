import random

def roll_dice():
  """Simulates rolling a single six-sided die."""
  return random.randint(1, 6)

# Example of how to use the function
if __name__ == "__main__":
  print("Welcome to the Dice Rolling Simulator!")
  while True:
    input("Press Enter to roll the dice or 'q' to quit: ").strip()
    if input("q"):
      print("Goodbye!")
      break
    else:
      result = roll_dice()
      print(f"You rolled a: {result}")
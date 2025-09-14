import time

countdown_value = 5

while countdown_value > 0:
    print(countdown_value)
    countdown_value -= 1  # Decrement the countdown value
    time.sleep(1)  # Pause for 1 second

print("Blast off!")
from datetime import datetime
import time
from playsound import playsound # You need to install playsound: pip install playsound

def set_alarm():
    """Sets an alarm based on user input and plays a sound when triggered."""
    alarm_time_str = input("Enter alarm time in HH:MM:SS format (24-hour): ")

    try:
        # Parse the input string into a time object
        alarm_hour, alarm_minute, alarm_second = map(int, alarm_time_str.split(':'))
        
        while True:
            current_time = datetime.now().time()
            
            # Check if current time matches the alarm time
            if (current_time.hour == alarm_hour and
                current_time.minute == alarm_minute and
                current_time.second == alarm_second):
                
                print("Alarm! Time to wake up!")
                # Replace 'alarm_sound.mp3' with your actual sound file path
                playsound('alarm_sound.mp3') 
                break # Exit the loop once the alarm is triggered
            
            time.sleep(1) # Check every second
            
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
    except FileNotFoundError:
        print("Alarm sound file not found. Make sure 'alarm_sound.mp3' exists.")

if __name__ == "__main__":
    set_alarm()
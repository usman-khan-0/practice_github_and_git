import time
import sys
import threading
import random

def display_time():
    sys.stdout.write("Reminder System started at: " + time.strftime("%H:%M:%S"))
    sys.stdout.flush()
    while not stop_event.is_set():
        sys.stdout.write("\rReminder System started at: " + time.strftime("%H:%M:%S"))
        sys.stdout.flush()
        time.sleep(1)  # Update every second

def task_reminder():
    tasks = ["Drink water", "Stretch your legs", "Check emails", "Take a deep breath"]
    num_reminders = 5

    print()  # Move to next line after starting time
    for i in range(num_reminders):
        delay = random.randint(3, 10)  # Random delay between 3 and 10 seconds
        print(f"Reminder {i+1}/{num_reminders}: Waiting {delay} seconds before next task...")
        time.sleep(delay)
        print(f"Reminder {i+1}/{num_reminders}: {random.choice(tasks)}")
    stop_event.set()  # Signal to stop time display
    print("\nAll reminders completed!")

# Global stop event for thread control
stop_event = threading.Event()

# Start time display in a separate thread
time_thread = threading.Thread(target=display_time)
time_thread.start()

# Run task reminders in the main thread
task_reminder()

# Wait for the time thread to finish
time_thread.join()
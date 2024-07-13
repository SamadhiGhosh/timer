import time
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import threading

def play_sound():
    # Play a sound using afplay
    for _ in range(5):
        subprocess.call(['afplay', '/System/Library/Sounds/Ping.aiff'])

def show_popup(root):
    # Show the popup message
    messagebox.showinfo("Time's Up", "The timer has ended!")
    root.destroy()

def start_timer():
    # Initialize the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user for the timer duration
    timer_duration = simpledialog.askinteger("Input", "Enter the timer duration in seconds:", minvalue=1)

    if timer_duration:
        # Wait for the specified time
        time.sleep(timer_duration)

        # Start the sound thread
        sound_thread = threading.Thread(target=play_sound)
        sound_thread.start()

        # Show the popup
        root.after(0, lambda: show_popup(root))

        root.mainloop()

if __name__ == "__main__":
    start_timer()

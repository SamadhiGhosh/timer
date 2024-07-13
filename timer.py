import time
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess 

def start_timer():
    # Initialize the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user for the timer duration
    timer_duration = simpledialog.askinteger("Input", "Enter the timer duration in seconds:", minvalue=1)

    if timer_duration:
        
        time.sleep(timer_duration)
        i = 0
        while i < 5:

            # Play a sound
            subprocess.call(['afplay', '/System/Library/Sounds/Ping.aiff'])
            i += 1
            time.sleep(1)

        # Popup message
        messagebox.showinfo("Time's Up", "The timer has ended!")

    # Destroy the main window after the popup is closed
    root.destroy()

if __name__ == "__main__":
    start_timer()

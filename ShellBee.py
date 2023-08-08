import tkinter as tk
import time
from threading import Thread
from pynput.keyboard import Controller

class KeyboardSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Keyboard Simulator")

        self.cycle_labels = ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4"]
        self.cycle_entries = []
        self.delay_entries = []

        self.keyboard = Controller()  # Pynput keyboard controller

        self.create_ui()

    def create_ui(self):
        for i in range(4):
            cycle_label = tk.Label(self.master, text=self.cycle_labels[i])
            cycle_label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            cycle_entry = tk.Entry(self.master)
            cycle_entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.cycle_entries.append(cycle_entry)

            delay_label = tk.Label(self.master, text="Delay (s)")
            delay_label.grid(row=i, column=2, padx=10, pady=5, sticky="e")

            delay_entry = tk.Entry(self.master)
            delay_entry.grid(row=i, column=3, padx=10, pady=5, sticky="w")
            self.delay_entries.append(delay_entry)

        start_button = tk.Button(self.master, text="Start", command=self.start_simulation)
        start_button.grid(row=4, columnspan=4, padx=10, pady=10)

    def simulate_keystrokes(self, keystrokes, delay):
        time.sleep(delay)
        for key in keystrokes:
            # Simulate pressing key using pynput keyboard controller
            self.keyboard.press(key)
            self.keyboard.release(key)
            time.sleep(0.1)  # Simulated keypress time
        time.sleep(1)  # Pause between cycles

    def start_simulation(self):
        for i in range(4):
            cycle_text = self.cycle_entries[i].get()
            delay_text = self.delay_entries[i].get()
            if cycle_text and delay_text:
                keystrokes = cycle_text.split()
                delay = float(delay_text)
                t = Thread(target=self.simulate_keystrokes, args=(keystrokes, delay))
                t.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyboardSimulator(root)
    root.mainloop()

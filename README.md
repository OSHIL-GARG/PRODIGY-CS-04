# 🔐 Keylogger with GUI – Python Project

A **keylogger** (short for *keystroke logger*) is a program that captures and records every keystroke made on a keyboard. It is widely used in **cybersecurity education** to demonstrate how keylogging attacks work and how systems can be monitored or exploited if not properly secured.

This project presents a **simple keylogger built using Python**, featuring a **Graphical User Interface (GUI)** created with Tkinter. The program uses the `pynput` library to listen for keyboard events and stores the keystrokes in a local file (`keylogs.txt`). The GUI includes buttons to **start** and **stop** the logging process, making it user-friendly and interactive.

---

## ⚙️ Technologies Used

- 🐍 **Python**: Programming language used to build the application.
- 🖼️ **Tkinter**: Built-in Python module for creating GUI applications.
- ⌨️ **pynput**: External library used to monitor and capture keyboard inputs.
- 🔄 **Threading**: Used to run the keylogging process in the background while keeping the GUI responsive.

---

## ⚙️ How the Code Works

### 1️⃣ Keyboard Listener (pynput)

- Uses `pynput.keyboard.Listener` to listen for keypress events.
- Each keystroke is captured via the `on_press()` method.
- Printable characters (`key.char`) are logged directly.
- Special keys (like Enter, Ctrl, etc.) are converted using `str(key)` for logging.

---

### 2️⃣ Logging to a File

- All keypresses are appended to a file named `keylogs.txt`.
- Uses standard Python file I/O to ensure logs persist even after application shutdown.

---

### 3️⃣ Threading for Background Logging

- The keylogger runs in a **separate thread** to ensure the Tkinter GUI remains responsive.
- Without threading, the GUI would freeze as soon as logging starts.

---

### 4️⃣ Tkinter GUI for Start/Stop

The GUI provides two main buttons:

- ▶️ **Start Logging**: Initializes and starts the keyboard listener.
- ⏹️ **Stop Logging**: Stops the listener safely and disables further logging.

🔐 It also includes safe shutdown behavior using the `WM_DELETE_WINDOW` event handler.

---

## 🚀 To Run This Project

### 📦 Install Required Package

```bash
pip install pynput

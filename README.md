# 🟩 WrdGuess (Tkinter GUI Version)

A graphical recreation of the popular word-guessing game "Wordle", built entirely in **Python** using the **Tkinter** GUI library.

## 🎮 Gameplay Overview

You have **six attempts** to guess a secret five-letter word. After each guess, the tiles change color to provide feedback:

- 🟩 **Green**: The letter is in the word and in the correct spot.
- 🟨 **Yellow**: The letter is in the word but in the wrong spot.
- ⬜ **Gray**: The letter is not in the word at all.

The game features a visual keyboard tracker to help you keep track of which letters you have already used.

## 🚀 Features

- **Full GUI**: No terminal typing required; interact with a clean, centered window.
- **Visual Feedback**: Real-time tile updates and an on-screen keyboard tracker.
- **Custom Assets**: Includes custom icons, victory trophies, and error screens.
- **Robust Dictionary**: Validates guesses against a 5-letter word list (`wrdguessdictionary.txt`).
- **Replayability**: "Play Again" functionality included on both Win and Loss screens.

## 🛠 Prerequisites

- **Python 3.x**
- **Pillow** (for image rendering)

Install the required library using pip:
```bash
pip install Pillow
```

## 🏃 How to Run

### Option 1: Run Locally
1. Ensure all files (`wrdguess.py`, `wrdguessdictionary.txt`, and the `images/` folder) are in the same directory.
2. Open your terminal in that directory.
3. Run the script:
   ```bash
   python wrdguess.py
   ```

### Option 2: Run with Docker 🐳
If you want to run the app in an isolated container, use the provided `Dockerfile`.

**1. Build the image:**
```bash
docker build -t wrdguess .
```

**2. Run the container (Linux/X11):**
```bash
xhost +local:docker
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix wrdguess
```

**3. Run the container (Windows):**
*Requires an X-Server like VcXsrv running on your host.*
```bash
docker run -it --rm -e DISPLAY=host.docker.internal:0.0 wrdguess
```

## 📁 Project Structure
- `wrdguess.py`: The main game logic and GUI code.
- `wrdguessdictionary.txt`: The text file containing all valid 5-letter words.
- `images/`: Folder containing all UI elements and icons.
- `Dockerfile`: Configuration for containerized execution.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
Created by [tharungopinath](https://github.com/tharungopinath)

# 🟩 Wordle (Tkinter GUI Version)

This is a graphical recreation of the popular Wordle game, built using Python and the Tkinter GUI library. Instead of typing in a terminal, players interact with an easy-to-use graphical interface featuring color-coded tiles, feedback messages, and a visual on-screen keyboard.

## 🧠 Gameplay Overview

Players have **six attempts** to guess a secret five-letter word. After each guess, feedback is provided to guide the next attempt:

- 🟩 **Green** – Correct letter in the correct position  
- 🟨 **Yellow** – Correct letter in the wrong position  
- ⬜ **Grey** – Letter not in the word  

The game ends when you either guess the word or run out of attempts.

## 🎮 Features

- Full graphical user interface (GUI) using **Tkinter**
- Visual tile grid that updates based on each guess
- On-screen **keyboard tracker** that updates to show which letters are:
  - 🟩 correct and in the right place
  - 🟨 correct but in the wrong place
  - ⬜ incorrect
- Pop-up windows for:
  - Incorrect word length
  - Invalid words (not in the dictionary)
  - Victory screen with trophy graphic 🎉
  - Game over screen with the correct answer revealed
- Restart button for replayability
- Centered window on launch with custom icon and background images

> ⚠️ Note: The on-screen keyboard is **not clickable**—it acts purely as a visual aid showing the status of letters used.


All assets (`wordledictionary.txt` and the `images/` folder) must be placed in the same directory as `wordle.py` for the game to function properly.

## 🛠 Requirements

- Python 3.x
- [`Pillow`](https://pypi.org/project/Pillow/) library for image rendering

To install Pillow:

```bash
pip install Pillow
```
---

## 🚀 Running the Game

1. Make sure you have these files in the **same folder**:
   - `wordle.py`
   - `wordledictionary.txt`
   - `images/` folder with:
     - `WordleTitleScreen.png`
     - `wordletrophy.png`
     - `wordleincorrect.png`
     - `iconimage.ico`

2. Open a terminal or command prompt in that folder.

3. Run the game using:

```bash
python wordle.py
```
4. The game window will launch. Type your 5-letter guesses into the entry box and click **Enter**.

Enjoy!

# Snake-Water-Gun Game

## Introduction
The Snake-Water-Gun game is a simple Python-based game where a player competes against the computer. The game follows the traditional rules:
- **Snake** beats **Water**
- **Water** beats **Gun**
- **Gun** beats **Snake**
- If both choices are the same, it's a draw.

## How to Play
### Command-Line Version
1. Run the Python script.
2. Enter your choice when prompted:
   - `s` for Snake
   - `w` for Water
   - `g` for Gun
3. The computer will randomly select its choice.
4. The result will be displayed on the screen, showing both choices and the game outcome.

### GUI Version
1. Run the Python script with the graphical user interface (GUI).
2. Click the buttons (`Snake`, `Water`, or `Gun`) to select your choice.
3. The computer will randomly select its choice.
4. The result, including both choices and scores, will be displayed in a separate window.

## Requirements
- Python 3.x
- `tkinter` (built-in in Python) is required for the GUI version.

## Installation & Execution
### Running the Command-Line Version
1. Download or copy the `snake_water_gun.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using:
   ```bash
   python snake_water_gun.py
   ```

### Running the GUI Version
1. Download or copy the `snake_water_gun_gui.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using:
   ```bash
   python snake_water_gun_gui.py
   ```

## Code Versions
### Command-Line Version (`snake_water_gun.py`)
```python
import random

computer=random.choice([1,-1,0])
yourChoice=input("Enter your choice: ")
yourDict={'s':1,'w':-1,'g':0}
reverseDict={1:'Snake',-1:'Water',0:'Gun'}
you=yourDict[yourChoice]

print(f'You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}')

if (computer==you):
    print("It's a draw.")
else:
    if (computer==-1 and you==1):
        print('You win!')
    elif (computer==-1 and you==0):
        print('You lose!')
    elif (computer==1 and you==0):
        print('You win!')
    elif (computer==1 and you==-1):
        print('You lose!')
    elif (computer==0 and you==1):
        print('You lose!')
    elif (computer==0 and you==-1):
        print('You win!')
```

### GUI Version (`snake_water_gun_gui.py`)
```python
import random
import tkinter as tk
from tkinter import Label, Toplevel, messagebox

# Mapping dictionaries
yourDict = {'s': 1, 'w': -1, 'g': 0}
reverseDict = {1: 'Snake', -1: 'Water', 0: 'Gun'}

# Score tracking
player_score = 0
computer_score = 0

# Function to display results in a custom window
def show_result(player_choice, computer_choice, result_text):
    result_window = Toplevel(root)
    result_window.title("Game Result")
    result_window.geometry("300x200")
    result_window.configure(bg="#FFE4B5")
    
    Label(result_window, text=f"You chose: {reverseDict[player_choice]}", font=("Arial", 12, "bold"), bg="#FFE4B5", fg="#8B0000").pack(pady=5)
    Label(result_window, text=f"Computer chose: {reverseDict[computer_choice]}", font=("Arial", 12, "bold"), bg="#FFE4B5", fg="#00008B").pack(pady=5)
    Label(result_window, text=result_text, font=("Arial", 14, "bold"), bg="#FFE4B5", fg="#006400").pack(pady=10)
    Label(result_window, text=f"Scores:\nYou: {player_score} | Computer: {computer_score}", font=("Arial", 12, "bold"), bg="#FFE4B5", fg="#8B008B").pack(pady=10)

# Function to play one round
def play(choice):
    global player_score, computer_score
    
    computer = random.choice([1, -1, 0])
    you = yourDict[choice]
    result = ""
    
    if computer == you:
        result = "It's a draw."
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result = "You win!"
        player_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    show_result(you, computer, result)

root = tk.Tk()
root.title("Snake-Water-Gun Game")
root.geometry("400x300")
root.configure(bg="#ADD8E6")

label = tk.Label(root, text="Choose your move:", font=("Times New Roman", 18, "bold"), bg="#ADD8E6", fg="#00008B")
label.pack(pady=15)

btn_snake = tk.Button(root, text="Snake", font=("Times New Roman", 12, "bold"), bg="#FFD700", fg="#8B0000", width=10, command=lambda: play('s'))
btn_snake.pack(pady=5)

btn_water = tk.Button(root, text="Water", font=("Times New Roman", 12, "bold"), bg="#00FA9A", fg="#00008B", width=10, command=lambda: play('w'))
btn_water.pack(pady=5)

btn_gun = tk.Button(root, text="Gun", font=("Times New Roman", 12, "bold"), bg="#FF4500", fg="#FFFFFF", width=10, command=lambda: play('g'))
btn_gun.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", font=("Times New Roman", 12, "bold"), bg="#DC143C", fg="#FFFFFF", width=10, command=root.quit)
btn_exit.pack(pady=15)

root.mainloop()
```
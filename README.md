# Tic-Tac-Toe

A Tic-Tac-Toe game implemented in Python using tkinter for the GUI. The game allows the player to choose between playing against a computer or another player. The player can also choose the difficulty level of the computer opponent.

## Requirements

- Python 3.x
- tkinter (should come with Python)

## How to Run

1. Download or clone the repository
2. Navigate to the directory containing the files
3. Run `python3 app.py`

## Gameplay

- The game starts with X's turn
- To make a move, click on an empty space on the game board
- The game can be reset at any time by clicking the "Reset" button
- The player can toggle whether they are playing against a computer or another player using the "VS Computer" button
- The player can also toggle the difficulty level of the computer opponent using the "Difficulty" button

## AI

The computer uses the minimax algorithm to decide its next move. The difficulty level can be set to one of four levels: Easy, Normal, Hard, or Insane. The higher the difficulty, the deeper the minimax search tree will be, making the computer a tougher opponent.

## File Descriptions

- `app.py` - Main file that runs the game
- `tic_tac_toe.py` - Contains functions for determining available moves, deciding the computer's next move, and implementing the minimax algorithm. 
If run, it is a command-line version of the game against an unbeatable AI.

## Notes

- The game board is a 3x3 grid where the top left space is indexed as (0,0), the top middle as (0,1), etc.
- The minimax algorithm has a depth parameter that determines how deep the search tree will be. A deeper search tree will result in a tougher opponent, but will also take longer to calculate the next move.

from tic_tac_toe import initialize_board, minimax
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        # create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Tic-Tac-Toe")

        # create the game board
        self.board = []
        for row in range(3):
            self.board.append([])
            for col in range(3):
                self.board[row].append(tk.Button(self.main_window,
                                                 text=" ", font=('TkDefaultFont', 30), height=5, width=10,
                                                 command=lambda row=row, col=col: self.make_move(row, col)))
                self.board[row][col].grid(row=row, column=col)

        # create the reset button
        self.reset_button = tk.Button(
            self.main_window, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=2)

        # create the toggle button for vs computer
        self.vs_button = tk.Button(
            self.main_window, text="VS Computer: On", command=self.toggle_vs)
        self.vs_button.grid(row=3, column=1)

        self.x_turn = True
        self.vs_computer = True

    def make_move(self, row, col):
        # check if the space is already occupied
        if self.board[row][col]["text"] != " ":
            return

        # determine which player's turn it is
        player = "X" if self.x_turn else "O"

        # make the move
        self.board[row][col]["text"] = player

        # check if the player has won
        if self.has_won(player):
            messagebox.showinfo("Congratulations!",
                                f"Player {player} has won!")
            self.reset()
            return

        # check if the game is a draw
        if self.is_draw():
            messagebox.showinfo("Game Over", "The game is a draw!")
            self.reset()
            return

        # switch turns
        self.x_turn = not self.x_turn

        if self.vs_computer:
            self.make_computer_move()

    def make_computer_move(self):
        (row, col) = minimax(self.board_to_2Darray(), 4, self.x_turn)[1]

        # determine which player's turn it is
        player = "X" if self.x_turn else "O"

        # make the move
        self.board[row][col]["text"] = player

        # check if the player has won
        if self.has_won(player):
            messagebox.showinfo("Congratulations!",
                                f"Player {player} has won!")
            self.reset()
            return

        # check if the game is a draw
        if self.is_draw():
            messagebox.showinfo("Game Over", "The game is a draw!")
            self.reset()
            return

        # switch turns
        self.x_turn = not self.x_turn

    def board_to_2Darray(self):
        board = initialize_board()
        for row in range(3):
            for col in range(3):
                board[row][col] = self.board[row][col]["text"]
        return board

    def has_won(self, player):
        # check for a win by checking all rows, columns, and diagonals
        for row in range(3):
            if self.board[row][0]["text"] == player and self.board[row][1]["text"] == player and self.board[row][2]["text"] == player:
                return True
        for col in range(3):
            if self.board[0][col]["text"] == player and self.board[1][col]["text"] == player and self.board[2][col]["text"] == player:
                return True
        if self.board[0][0]["text"] == player and self.board[1][1]["text"] == player and self.board[2][2]["text"] == player:
            return True
        if self.board[0][2]["text"] == player and self.board[1][1]["text"] == player and self.board[2][0]["text"] == player:
            return True
        return False

    def is_draw(self):
        # check if the game is a draw by checking if there are any empty spaces on the board
        for row in range(3):
            for col in range(3):
                if self.board[row][col]["text"] == " ":
                    return False
        return True

    def reset(self):
        # Reset the game here
        self.x_turn = True

        for row in range(3):
            for col in range(3):
                self.board[row][col]["text"] = " "

    def toggle_vs(self):
        if self.vs_computer:
            self.vs_computer = False
            self.vs_button["text"] = "VS Computer: Off"
        else:
            self.vs_computer = True
            self.vs_button["text"] = "VS Computer: On"


# create the game and start the main loop
game = TicTacToe()
game.main_window.mainloop()

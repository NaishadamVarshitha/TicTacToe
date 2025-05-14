# to setup Ui at highlevel 
# for GUI we use tkinter library and the total game runs in a window of this standard library
import tkinter as tk
from tkinter import messagebox  # to show win/draw messages

# to create class
class TicTacToe:
    def __init__(self):  # Init method used to initialize the elements of the class
        self.currentplayer = "X"  # to keep track of current player
        # to create board
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.window = tk.Tk()  # To create a window using tkinter
        self.window.title("Tic Tac Toe")

        self.buttonsgrid = []  # to create a list of buttons
        for i in range(3):  # to create three rows
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=20, height=10,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttonsgrid.append(row)  # to add the buttons to the grid

    def make_move(self, row, col):
        if self.board[row][col] == "":  # to check if the cell is empty
            self.board[row][col] = self.currentplayer
            self.buttonsgrid[row][col].config(text=self.currentplayer, state=tk.DISABLED)  # update button text

            if self.check_winner(self.currentplayer):
                messagebox.showinfo("Game Over", f"Player {self.currentplayer} wins!")
                self.disable_all_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.disable_all_buttons()
            else:
                self.currentplayer = "O" if self.currentplayer == "X" else "X"

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def disable_all_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttonsgrid[i][j].config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()

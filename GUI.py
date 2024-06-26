"""From the engine I build a GUI here using Tkinter.
"""

__author__ = "Albin Nilsson"
__copyright__ = "Copyright 2023, Kth"
__license__ = "CC0"

import random
import tkinter as tk
from tkinter import ttk
import time

class Support:
    """Class consisting of GUI support functions for I/O"""
    def input(prompt=''):
        """This method overwrites the terminal input for the GUI"""
        win= tk.Tk()

        label= tk.Label(win, text=prompt)
        label.pack()

        userinput= tk.StringVar(win)
        entry= tk.Entry(win, textvariable=userinput)
        entry.pack()

        # pressing the button should stop the mainloop
        button= tk.Button(win, text="ok", command=win.quit)
        button.pack()

        # block execution until the user presses the OK button
        win.mainloop()

        # mainloop has ended. Read the value of the Entry, then destroy the GUI.
        userinput= userinput.get()
        win.destroy()

        return userinput

    def print(prompt=''):
        """This method overwrites the terminal print for the GUI"""
        win= tk.Tk()

        label= tk.Label(win, text=prompt)
        label.pack()

        # pressing the button should stop the mainloop
        button= tk.Button(win, text="ok", command=win.quit)
        button.pack()

        # block execution until the user presses the OK button
        win.mainloop()

        # mainloop has ended. Read the value of the Entry, then destroy the GUI.
        win.destroy()

class Chessboard:
    """Builds functions for the chessboard and game logic for how the knight moves upon it.

    Attributes:
        board

    """
    def __init__(self):
        """Initializes the instance by creating a chessboard as a nested list of integers

        Args:
            board (list): 12x12 matrix filled with empty spaces (zeroes) for "real 8x8 board", while squares outside of this are set to -1

        Returns:
            None
        """
        self.board = [[-1] * 12 for _ in range(12)] # Create a 12x12 matrix and initialize with -1 for the entire board

        for r in range(2, 10): # Set the inner part of the board to 0
            for c in range(2, 10):
                self.board[r][c] = 0

        self.max_steps = 0

    def valid_moves(self, current_row, current_col):
        """Calculates valid moves based on current position and board characteristics.

        Args:
            row (int): Input row
            col (int): Input column

        Returns:
            valid_moves (list): List of valid moves computed from input position
        """
        valid_moves_list = []
        steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for r, c in steps:
            new_row, new_col = current_row + r, current_col + c
            if 2 <= new_row <= 9 and 2 <= new_col <= 9 and self.board[new_row][new_col] == 0: # Knight only allowed
                # to go to squares that is within the board, and previously unvisited
                valid_moves_list.append((new_row, new_col))
        return valid_moves_list



    def move_knight_random(self, start_row, start_column, update_callback=None):
        """Moves the knight by checking that the move is valid, and ticks up a move counter.
        Alters board by adding this move counter to corresponding position.

        Args:
            start_row (int): Input row
            start_column (int): Input column
            update_callback (callable): Callback function to update the GUI after each step.

        Returns:
            None
        """
        self.__init__() # Clean board before proceeding
        move_number = 1
        self.board[start_row][start_column] = move_number # We represent the squares the knight has visited with its number

        while True:
            valid_moves = self.valid_moves(start_row, start_column)

            if not valid_moves:
                self.max_steps = move_number
                break # Exit loop when there are no more valid squares to visit

            chosen_move = random.choice(valid_moves) # Randomly chooses a move from permitted moves
            move_number += 1
            self.board[chosen_move[0]][chosen_move[1]] = move_number

            start_row, start_column = chosen_move # The chosen move becomes input for the next loop

            if update_callback:
                update_callback(self.board)  # Call the callback function to update the GUI
                time.sleep(0.3)  # Introduce a 0.3-second delay

    def move_knight_input(self, start_row, start_column, update_callback=None):
        """Moves the knight by prompting user, checks if move is valid, and ticks up a move counter.
        Alters board by adding this move counter to corresponding position.

        Args:
            start_row (int): Input row
            start_column (int): Input column

        Returns:
            None
        """
        self.__init__()  # Clean board before proceeding
        move_number = 1
        self.board[start_row][start_column] = move_number  # We represent the squares the knight has visited with its number

        if update_callback:
            update_callback(self.board)  # Call the callback function to update the GUI
            time.sleep(0.3)  # Introduce a 0.3-second delay

        while True:
            valid_moves = self.valid_moves(start_row, start_column)

            if not valid_moves:
                self.max_steps = move_number
                break  # Exit loop when there are no more valid squares to visit

            chosen_move = Support.input(f"Input a square for move {move_number + 1}")
            chosen_start_column, chosen_start_row = parse_start_position(chosen_move)

            if (chosen_start_row, chosen_start_column) in valid_moves:
                move_number += 1
                self.board[chosen_start_row][chosen_start_column] = move_number
            else:
                translated = chr(ord("A") + (chosen_start_column - 2)) + str(chosen_start_row - 1) # Translates tuple to chessboard square
                Support.print(f"Invalid move: {translated}")
                self.max_steps = move_number
                break

            start_row = chosen_start_row
            start_column = chosen_start_column # The chosen move becomes input for the next loop

            if update_callback:
                update_callback(self.board)  # Call the callback function to update the GUI
                time.sleep(0.3)  # Introduce a 0.3-second delay

def save_high_score(steps):
    """Reads high_score.txt and writes the steps to it if steps surpass the current high score.

    Args:
        steps (int): The number of steps from one knight walk in main program

    Returns:
        None
    """
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read().strip())
    except FileNotFoundError:
        high_score = float('inf')

    if steps > high_score:
        Support.print(f"New high score! {steps} steps is higher than the previous high score of {high_score} steps.")
        with open("high_score.txt", "w") as file:
            file.write(str(steps))


def parse_start_position(input_text):
    """Parses the input text to extract start column and start row.

    Args:
        input_text (str): Text containing the start position.

    Returns:
        tuple: Tuple containing start column and start row, e.g., (2, 3).
    """
    input_text = input_text.upper()
    start_column = ord(input_text[0]) - ord('A') + 2
    start_row = int(input_text[1]) + 1
    return start_column, start_row


class ChessboardGUI:
    """Creates a GUI for the chessboard and knight's tour.

    Attributes:
        master (tk.Tk): The main window of the GUI.
        chessboard (Chessboard): The instance of the Chessboard class.

    """
    def __init__(self, master):
        """Initializes the ChessboardGUI.

        Args:
            master (tk.Tk): The main window of the GUI.

        Returns:
            None
        """
        self.master = master
        self.master.title("Knight's Tour")
        self.chessboard = Chessboard()

        self.create_widgets()

    def create_widgets(self):
        """Creates widgets for the GUI.

        Returns:
            None
        """
        self.board_frame = ttk.Frame(self.master)
        self.board_frame.grid(row=0, column=0, padx=10, pady=10)
        self.canvas = tk.Canvas(self.board_frame, width=400, height=400)
        self.canvas.pack()
        self.draw_chessboard()

        self.control_frame = ttk.Frame(self.master)
        self.control_frame.grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(self.control_frame, text="Random Walk", command=self.start_random_walk).pack(pady=5)
        ttk.Button(self.control_frame, text="Input Own Walk", command=self.start_user_input).pack(pady=5)

    def draw_chessboard(self):
        """Draws the chessboard on the canvas.

        Returns:
            None
        """
        for row in range(8):
            for col in range(8):
                x0, y0 = col * 50, row * 50
                x1, y1 = x0 + 50, y0 + 50
                color = "#eeeed2" if (row + col) % 2 == 0 else "#769656"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

                # Display row numbers and column names
                if col == 0:
                    self.canvas.create_text(x0 + 10, y0 + 10, text=str(8 - row), font=("Helvetica", 8, "bold"))
                if row == 7:
                    col_name = chr(ord('A') + col)
                    self.canvas.create_text(x0 + 40, y0 + 40, text=col_name, font=("Helvetica", 8, "bold"))

    def update_board(self, board):
        """Updates the chessboard GUI based on the current state of the board.

        Args:
            board (list): The current state of the chessboard.

        Returns:
            None
        """
        self.canvas.delete("knight")
        for r in range(2, 10):
            for c in range(2, 10):
                if board[r][c] != 0:
                    x, y = (c - 2) * 50, (9 - r) * 50  # Drawn board starts at 0 while matrix starts at 2, and tkinter orientation starts upper left.
                    self.canvas.create_text(x + 25, y + 25, text=str(board[r][c]),
                                            font=("Helvetica", 10, "bold"), tags="knight")
        self.master.update()

    def start_random_walk(self):
        """Method that initializes the random walk"""
        self.canvas.delete("knight")  # Reset board
        self.handle_random_walk(Support.input("Enter starting square for Random Walk"))
        self.display_max_steps()

    def start_user_input(self):
        """Method that initializes the user input walk"""
        self.canvas.delete("knight")  # Reset board
        self.handle_user_input(Support.input("Enter starting square for Input Own Walk"))
        self.display_max_steps()

    def handle_random_walk(self, input_text):
        """Method that parses inputs and sends to logic for random walk"""
        start_column, start_row = parse_start_position(input_text)
        self.chessboard.move_knight_random(start_row, start_column, self.update_board)

    def handle_user_input(self, input_text):
        """Method that parses inputs and sends to logic for user input walk"""
        start_column, start_row = parse_start_position(input_text)
        self.chessboard.move_knight_input(start_row, start_column, self.update_board)

    def display_max_steps(self):
        """Method that prints the number of steps the knight takes"""
        max_steps = self.chessboard.max_steps
        Support.print(f"The knight took {max_steps} steps before stopping!")
        save_high_score(max_steps)

    def draw_knight_path(self):
        """Draws the knight's path on the canvas.

        Returns:
            None
        """
        for r in range(2, 10):
            for c in range(2, 10):
                if self.chessboard.board[r][c] != 0:
                    x, y = (c - 2) * 50, (9 - r) * 50 # Drawn board starts at 0 while matrix starts at 2, and tkinter orientation starts upper left.
                    self.canvas.create_text(x + 25, y + 25, text=str(self.chessboard.board[r][c]),
                                            font=("Helvetica", 10, "bold"), tags="knight")

def main():
    """The main function that initializes the chessboard and runs the GUI.

    Returns:
        None
    """
    root = tk.Tk()
    app = ChessboardGUI(root)
    root.mainloop()

    max_number_of_steps = max(max(row) for row in chessboard_gui.chessboard.board)
    Support.print(f"The knight took {max_number_of_steps} steps before stopping!")

    save_high_score(max_number_of_steps)


if __name__ == "__main__":
    main()
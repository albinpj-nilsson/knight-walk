"""From the engine I build a GUI here using Tkinter.
"""

__author__ = "Albin Nilsson"
__copyright__ = "Copyright 2023, Kth"
__license__ = "CC0"

import random
import tkinter as tk
from tkinter import ttk
import time

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
                break # Exit loop when there are no more valid squares to visit

            chosen_move = random.choice(valid_moves) # Randomly chooses a move from permitted moves
            move_number += 1
            self.board[chosen_move[0]][chosen_move[1]] = move_number

            start_row, start_column = chosen_move # The chosen move becomes input for the next loop

            if update_callback:
                update_callback(self.board)  # Call the callback function to update the GUI
                time.sleep(0.3)  # Introduce a 0.3-second delay

    def move_knight_user_input(self, sequence_of_moves, update_callback=None):
        """Moves the knight based on a sequence of moves given by user, given sequence is valid.

        Args:
            sequence_of_moves (list): A list of moves given by user
            update_callback (callable): Callback function to update the GUI after each step.

        Returns:
            None"""
        self.__init__()  # Clean board before proceeding
        move_number = 1
        start_row, start_column = sequence_of_moves[0]
        self.board[start_row][start_column] = move_number  # Map the first move

        for i in range(len(sequence_of_moves[1:])):
            valid_next_moves = self.valid_moves(start_row, start_column)
            if sequence_of_moves[i + 1] in valid_next_moves:
                move_number += 1
                start_row, start_column = sequence_of_moves[i + 1]  # Update to the next move
                self.board[start_row][start_column] = move_number

                if update_callback:
                    update_callback(self.board)  # Call the callback function to update the GUI
                    time.sleep(0.3)  # Introduce a 0.3-second delay
            else:
                print(f"Invalid move: {sequence_of_moves[i + 1]}")
                break



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
        print(f"New high score! {steps} steps is higher than the previous high score of {high_score} steps.")
        with open("high_score.txt", "w") as file:
            file.write(str(steps))

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
        """Starts a random walk of the knight on the chessboard. Based off of main in engine.

        Returns:
            None
        """
        start_position = input("Type your starting square (e.g., E4): ")
        start_column = ord(start_position[0].upper()) - ord('A') + 2
        start_row = int(start_position[1]) + 1
        self.chessboard.move_knight_random(start_row, start_column, self.update_board)

    def start_user_input(self):
        """Starts a knight's tour based on the user's input.

        Returns:
            None
        """
        move_sequence = []
        while True:
            next_move = input("Enter next move (e.g., D2) or type 'DONE' to finish: ")
            if next_move.upper() == "DONE":
                self.chessboard.move_knight_user_input(move_sequence, self.update_board)
                break
            move_sequence.append((int(next_move[1]) + 1, ord(next_move[0].upper()) - ord('A') + 2))

    def draw_knight_path(self):
        """Draws the knight's path on the canvas.

        Returns:
            None
        """
        self.canvas.delete("knight") # Reset board

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

if __name__ == "__main__":
    main()
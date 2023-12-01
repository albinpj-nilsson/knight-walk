"""I create the engine for the game reliant upon tkinter. Google style docstrings,
see e.g. https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
"""

__author__ = "Albin Nilsson"
__copyright__ = "Copyright 2023, Kth"
__license__ = "CC0"

import random
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

    def print_board(self):
        """Prints chessboard to terminal by iterating through board
        """
        print("------------------------------------------")
        print("|    ---------------------------------   |")
        for r in range(9, 1, -1): # Iterate backwards to get chessboard row numbers right
            print(f"|{r-1}   |",end="") # Adds row numbers for each row
            for c in range(2, 10):
                print(f" {' ' if self.board[r][c] == 0 else self.board[r][c]} |", end="") # Prints squares where
                # knight has not been as spaces and all other squares as the number of the matrix position
                if c == 9: # Add rightmost board edge when loop reaches last column
                    print("   |")
            print("|    ---------------------------------   |") # Adds lines between rows
        print("|      A   B   C   D   E   F   G   H     |")
        print("------------------------------------------")


    def valid_moves(self, row, column):
        """Calculates valid moves based on current position and board characteristics.

        Args:
            row (int): Input row
            column (int): Input column

        Returns:
            moves (list): List of valid moves computed from input position
        """
        step = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        pass
    def move_knight(self, start_row, start_column):
        """Moves the knight by checking that the move is valid, and ticks up a move counter.
        Alters board by adding this move counter to corresponding position.

        Args:
            start_row (int): Input row
            start_column (int): Input column

        Returns:
            None
        """
        pass


def save_high_score(steps):
    """Reads high_score.txt and writes the steps to it if steps surpass the current high score.

    Args:
        steps (int): The max number of steps from one knight walk in main program

    Returns:
        None
    """
    pass

if __name__ == "__main__":
    knight = Chessboard()
    knight.print_board()

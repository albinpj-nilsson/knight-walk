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
            board (list): 12x12 matrix filled with empty spaces for "real 8x8 board", while squares outside of this are set to -1

        Returns:
            None
        """
    def print_board(self):
        """Prints chessboard to terminal by iterating through board
        """
        pass

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
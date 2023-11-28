"""I create the engine for the game reliant upon tkinter. Google style docstrings,
see e.g. https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
"""

__author__ = "Albin Nilsson"
__copyright__ = "Copyright 2023, Kth"
__license__ = "CC0"

from tkinter import *

# Classes for the game
class Square:
    """Defines logic for a checkboard square

    Attributes: ...
    """

    def __init__(self):
        """Initializes the instance based on ...

        Args:
            str1 (str): The string to be reversed

        Returns:
            reverse(str1): The string which gets reversed
        """
        pass

    def click_event(self):
        """Updates a square when pressed

        Parameters:
            str1 (str): The string to be reversed

        Returns:
            reverse(str1): The string which gets reversed
        """
        pass


class Chessboard:
    """Builds functions for the chessboard and game logic

    Attributes: ...
    """
    def __init__(self):
        """Initializes the instance based on moves a knight can take ...

        Args:
            str1 (str): The string to be reversed

        Returns:
            reverse(str1): The string which gets reversed
        """
        self.moves = [(-1, -2), (-1, 2), (1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    def create_board(self):
        """Iterates across the window and to create instances for the Square class

        Args:
            str1 (str): The string to be reversed

        Returns:
            reverse(str1): The string which gets reversed
        """
        pass

    def valid_moves(self, position):
        """Calculates valid moves based on current position.

        Args:
            str1 (str): The string to be reversed

        Returns:
            valid_moves: List of valid coordinates
        """
        pass

    def compute_longest_route():
        """Computes the longest route for knight.

        Args:
            str1 (str): The string to be reversed

        Returns:
            longest_route: List of positions in order of the path
        """
        pass
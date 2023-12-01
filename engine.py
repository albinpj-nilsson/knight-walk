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
        print("---------------------------------------------------")
        print("|    -----------------------------------------    |")
        for r in range(9, 1, -1): # Iterate backwards to get chessboard row numbers right
            print(f"|{r-1}   |",end="") # Adds row numbers for each row
            for c in range(2, 10):
                square_value = self.board[r][c]
                if square_value == 0:
                    value_str = " "
                else:
                    value_str = str(square_value)
                spaces_to_add = 4 - len(value_str)
                print(f"{' ' * (spaces_to_add // 2)}{value_str}{' ' * (spaces_to_add - spaces_to_add // 2)}|", end="") # Prints squares where
                # knight has not been as spaces and all other squares as the number of the matrix position
                if c == 9: # Add rightmost board edge when loop reaches last column
                    print("    |")
            print("|    -----------------------------------------    |") # Adds lines between rows
        print("|       A    B    C    D    E    F    G    H      |")
        print("---------------------------------------------------")


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



    def move_knight(self, start_row, start_column):
        """Moves the knight by checking that the move is valid, and ticks up a move counter.
        Alters board by adding this move counter to corresponding position.

        Args:
            start_row (int): Input row
            start_column (int): Input column

        Returns:
            None
        """
        move_number = 1
        self.board[start_row][start_column] = move_number # We represent the squares the knight has visited with its number

        while True:
            moves = self.valid_moves(start_row, start_column)

            if not moves:
                break # Exit loop when there are no more valid squares to visit

            chosen_move = random.choice(moves) # Randomly chooses a move
            move_number += 1
            self.board[chosen_move[0]][chosen_move[1]] = move_number

            start_row, start_column = chosen_move # The chosen move becomes input for the next loop

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
        with open("high_score.txt", "w") as file:
            file.write(str(steps))

if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.print_board() # User gets an overview of the chessboard before making a choice

    while True: # User input must be valid
        start_position = input("Type your starting square (e.g., E4): ")
        start_column = ord(start_position[0].upper()) - ord('A') + 2
        start_row = int(start_position[1]) + 1

        if 2 <= start_row <= 9 and 2 <= start_column <= 9:
            break
        else:
            print("Invalid starting position. Please try again.")

    chessboard.move_knight(start_row, start_column)
    chessboard.print_board() # The user is shown the result of their choice

    max_number_of_steps = max(max(row) for row in chessboard.board)
    print(f"The knight took {max_number_of_steps} steps before it could not walk to any new squares!")

    save_high_score(max_number_of_steps)

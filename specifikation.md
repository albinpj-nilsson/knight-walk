# Inledning

Springarens vandring på
schackbrädet (134) är en medelsvår uppgift som kan ge betyg A-E. Jag siktar på A.

Springaren rör sig enligt schackreglerna, det vill säga antingen två steg horisontellt och ett steg vertikalt eller två steg vertikalt och ett steg horisontellt. Under hela vandringen får springaren inte besöka samma plats mer än en gång. Användaren får ange startpositionen för springaren, och det finns högst åtta möjliga platser för springaren att gå till från varje ruta. Programmet ska implementera en klass vars fält representerar schackbrädet och vars metoder styr springarens förflyttning. Om springaren står på en kantplats finns vissa riktningar den inte kan röra sig i för att undvika att hamna utanför brädet. Slutligen ska programmet välja slumpmässigt vilken ruta springaren ska gå till bland de godkända alternativen.

Det kommer att vara svårt att programmera det grafiska gränssnittet, och att få de olika delarna av programmet att prata med varandra. 

Wikipediasidan: https://en.wikipedia.org/wiki/Knight%27s_tour

# Användarscenarier

Ett tänkt användarscenario är att användaren kan simulera springarens vandring för att lära sig mer om shack, till exempel om man vill se hur man kan komma till en ny position givet var man står just nu. Då kan detta program visa de möjliga platserna man korsar genom att gå till den angivna destinationen. 

Ett annat användarscenario är för att undervisa om schackstrategi och taktik när man använder springaren, för att öva på hur springaren rör sig samt bli bättre på kalkylering av framtida utfall och sekvenser.

# Kodskelett

```python
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
```

# Minnet

[Se LåP](LåP Knight Walk.pdf)

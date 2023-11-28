# Inledning

Springarens vandring på
schackbrädet är en medelsvår uppgift som kan ge betyg A-E. Jag siktar på A.

Springaren rör sig enligt schackreglerna, det vill säga antingen två steg horisontellt och ett steg vertikalt eller två steg vertikalt och ett steg horisontellt. Under hela vandringen får springaren inte besöka samma plats mer än en gång. Användaren får ange startpositionen för springaren, och det finns högst åtta möjliga platser för springaren att gå till från varje ruta. Programmet ska implementera en klass vars fält representerar schackbrädet och vars metoder styr springarens förflyttning. Om springaren står på en kantplats finns vissa riktningar den inte kan röra sig i för att undvika att hamna utanför brädet. Slutligen ska programmet välja slumpmässigt vilken ruta springaren ska gå till bland de godkända alternativen.

Det kommer att vara svårt att programmera det grafiska gränssnittet, och att få de olika delarna av programmet att prata med varandra. 

Wikipediasidan: https://en.wikipedia.org/wiki/Knight%27s_tour

# Användarscenarier



# Kodskelett

```python
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
        """Initializes the instance based on ...

        Args:
            str1 (str): The string to be reversed

        Returns:
            reverse(str1): The string which gets reversed
        """
        pass
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
    
```
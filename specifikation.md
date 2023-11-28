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

    def click_event(self): # Kanske uppdatera
        """Updates a square when pressed

        Parameters:
            str1 (str): The string to be reversed

        Returns:
            reverse(str1): The string which gets reversed
        """
        pass


class Chessboard:
    """Builds functions for the chessboard and game logic

    Attributes: 
    """
    def __init__(self):
        """Initializes the instance based on ...

        Args:
            str1 (str): The string to be reversed

        Returns:
            reverse(str1): The string which gets reversed
        """
        self.moves = [(-1,-2),(-1,2),(1,2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
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
            position: Current position of knight
            
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
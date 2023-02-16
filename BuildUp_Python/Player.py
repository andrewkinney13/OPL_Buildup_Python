
from Tile import Tile
from Deck import Deck

class Player:
    # Constructor
    def __init__(self):
        self.score = 0
        self.roundsWon = 0
        self.isTheirTurn = False

    # Checks if player has playable tiles
    def HasPlayableTiles(self):
        return True

    # Sets functions to run after a turn
    def InitalizeRoundData(self, GUI, changeTurnFunction, returnToHandFunction):
        self.GUI = GUI
        self.changeTurnFunction = changeTurnFunction
        self.returnToHandFunction = returnToHandFunction

    # Runs after turn functons
    def AfterTurnFunctions(self):
        self.changeTurnFunction()
        self.returnToHandFunction()
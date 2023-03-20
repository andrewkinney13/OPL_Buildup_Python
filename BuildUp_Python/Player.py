
from tkinter.font import names
from Tile import Tile
from Deck import Deck

class Player:
    # Constructor
    def __init__(self, name, color):

        # Regular attributes
        self.name = name
        self.color = color
        self.score = 0
        self.roundsWon = 0

        # Turn attributes
        self.isTheirTurn = False
        self.selectingHandTile = False
        self.placingOnStackTile = False
        self.tileToPlace = Tile()
        self.tileToPlaceOn = Tile()
        self.PlayHandFunction = None

    # Sets their turn, and relevent booleans 
    def SetTheirTurn(self, theirTurn):
        if(theirTurn):
            self.isTheirTurn = True
            self.selectingHandTile = True
            self.placingOnStackTile = True

        else:
            self.isTheirTurn = False
            self.selectingHandTile = False
            self.placingOnStackTile = False
       
    # Assign play round function
    def SetPlayHandFunction(self, PlayHand):
        self.PlayHandFunction = PlayHand

    # Function ran when tile is pressed, returns itself to round
    def TileSelected(self, tile):

        # Selecting hand tile
        if (self.selectingHandTile):
            self.tileToPlace = tile
            self.selectingHandTile = False

        # Selecting stack tile
        elif(self.placingOnStackTile):
            self.tileToPlaceOn = tile
            self.placingOnStackTile = False

        # Return to play hand
        self.PlayHandFunction()

    # Function ran when continue button pressed, returns to round
    def ContinueSelected(self):
        if (self.selectingHandTile):
            self.selectingHandTile = False

        # Selecting stack tile
        elif(self.placingOnStackTile):
            self.placingOnStackTile = False

        # Return to play hand
        self.PlayHandFunction()

    # Display the tiles at the end of a turn
    def DisplayBoard(self, Players, Decks, playerNum, opponentNum, HandFunc, topMsg = None, bottomMsg = None):

        # Reset the status of the stack tiles
        Decks[0].ResetStackTileStatus()
        Decks[1].ResetStackTileStatus()

        # Create a screen for human to see the new board, and continue to next turn
        self.PlayerView.CreateTileScreen(Players, Decks, playerNum, opponentNum, HandFunc, topMsg, bottomMsg)

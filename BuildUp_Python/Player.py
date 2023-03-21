
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
            self.selectingHandTile = False
            self.tileToPlace = tile

        # Selecting stack tile
        elif(self.placingOnStackTile):
            self.selectingOnStackTile = False
            self.tileToPlaceOn = tile

        # Return to play hand
        self.PlayHandFunction()



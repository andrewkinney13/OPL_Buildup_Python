
from Tile import Tile
from Deck import Deck

class Player:
    # Constructor
    def __init__(self):
        self.score = 0
        self.roundsWon = 0
        self.isTheirTurn = False

        self.selectingHandTile = False
        self.placingOnStackTile = False
        
        self.TileToPlace = Tile()
        self.TileToPlaceOn = Tile()
        self.CreateTurnMenu = None

    # Checks if player has playable tiles
    def HasPlayableTiles(self):
        return True

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

    # Returns whether or not the player has remaining moves
    def HasRemainingMoves(self):
        if (self.selectingHandTile or self.placingOnStackTile):
            return True
        else:
            return False


    # Place tile onto stack
    def PlaceTileOnStack(self):

        self.placingOnStackTile = False
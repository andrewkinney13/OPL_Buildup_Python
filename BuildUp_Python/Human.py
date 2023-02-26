
from Player import Player

class Human(Player):
    
    # Constructor
    def __init__(self, name):
        self.color = 'B'
        self.name = name

        self.SelectionPrompt = "Select a tile from your hand to place on a stack..."
        self.PlacementPrompt = "Select a tile on a stack to place your hand tile..."

        # Call base class constructor
        super().__init__()


   # Select tile from hand
    def SelectHandTile(self, tile):

        self.TileToPlace = tile

        self.selectingHandTile = False

        self.CreateTurnMenu()
    
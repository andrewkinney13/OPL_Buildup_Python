from Player import Player

class Computer(Player):

    # Constructor
    def __init__(self, name):
        self.color = 'W'
        self.name = name

        self.SelectionPrompt = "Computer to select hand tile..."
        self.PlacementPrompt = "Computer to place hand tile on stack..."

        # Call base class constructor
        super().__init__()

 # Select tile from hand to play
    def SelectHandTile(self, ownHand, ownStack, opponentStack):

        # Logic would go here for what tile from hand to place and where 
        self.TileToPlace = ownHand[0]
        self.TileToPlaceOn = opponentStack[0]

        self.selectingHandTile = False

        self.CreateTurnMenu()

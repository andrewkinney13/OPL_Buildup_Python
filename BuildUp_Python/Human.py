
from Player import Player
from HumanView import HumanView

class Human(Player):
    
    # Constructor
    def __init__(self, name, side, GUI):
        self.color = 'B'
        self.name = name
        self.side = side
        self.GUI = GUI
        self.HumanView = HumanView(GUI)

        # Call base class constructor
        super().__init__()

   # Select tile from hand
    def SelectHandTile(self, Players, Decks, playerNum, opponentNum):
        
        # Determine placability of hand tiles
        Decks[playerNum].DetermineHandPlacability(Decks[playerNum].stack, Decks[opponentNum].stack)

        # Create a screen for human to select what tile is chosen 
        self.HumanView.CreateTileScreen(Players, Decks, playerNum, opponentNum, self.TileSelected)
        
    # Select what stack to place on
    def SelectStackTile(self, Players, Decks, playerNum, opponentNum, tileToPlace):
        
        # Determine placability of stack tiles, given tile to place
        Decks[playerNum].DetermineStackPlacability(tileToPlace)
        Decks[opponentNum].DetermineStackPlacability(tileToPlace)

        # Reset status of hand tiles
        Decks[0].ResetHandTileStatus()
        Decks[1].ResetHandTileStatus()

        # Create a screen for human to select what stack to place on
        self.HumanView.CreateTileScreen(Players, Decks, playerNum, opponentNum, self.TileSelected)

    # Display the tiles at the end of a turn
    def DisplayBoard(self, Players, Decks, playerNum, opponentNum, HandFunc):

        # Reset the status of the stack tiles
        Decks[0].ResetStackTileStatus()
        Decks[1].ResetStackTileStatus()

        # Create a screen for human to see the new board, and continue to next turn
        self.HumanView.CreateTileScreen(Players, Decks, playerNum, opponentNum, HandFunc)

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

    


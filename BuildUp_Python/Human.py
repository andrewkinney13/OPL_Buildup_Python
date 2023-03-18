
from Player import Player
from PlayerView import PlayerView

class Human(Player):
    
    # Constructor
    def __init__(self, name, color, GUI):
     
        self.GUI = GUI
        self.PlayerView = PlayerView(GUI)

        # Call base class constructor
        super().__init__(name, color)

   # Select tile from hand
    def SelectHandTile(self, Players, Decks, playerNum, opponentNum):
        
        # Determine placability of hand tiles
        Decks[playerNum].DetermineHandPlacability(Decks[playerNum].stack, Decks[opponentNum].stack)

        # Create a screen for human to select what tile is chosen 
        self.PlayerView.CreateTileScreen(Players, Decks, playerNum, opponentNum, self.TileSelected)
        
    # Select what stack to place on
    def SelectStackTile(self, Players, Decks, playerNum, opponentNum, tileToPlace):
        
        # Determine placability of stack tiles, given tile to place
        Decks[playerNum].DetermineStackPlacability(tileToPlace)
        Decks[opponentNum].DetermineStackPlacability(tileToPlace)

        # Reset status of hand tiles
        Decks[0].ResetHandTileStatus()
        Decks[1].ResetHandTileStatus()

        # Create a screen for human to select what stack to place on
        self.PlayerView.CreateTileScreen(Players, Decks, playerNum, opponentNum, self.TileSelected)

    # Display the tiles at the end of a turn
    def DisplayBoard(self, Players, Decks, playerNum, opponentNum, HandFunc):

        # Reset the status of the stack tiles
        Decks[0].ResetStackTileStatus()
        Decks[1].ResetStackTileStatus()

        # Create a screen for human to see the new board, and continue to next turn
        self.PlayerView.CreateTileScreen(Players, Decks, playerNum, opponentNum, HandFunc)

    


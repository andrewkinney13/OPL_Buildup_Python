
from Player import Player

class Human(Player):
    
    # Constructor
    def __init__(self, name, color, GUI):
     
        self.GUI = GUI

        self.handTileSelectionPrompt = "Please select a tile from your hand to play..."
        self.stackTileSelectionPrompt = "Please select a stack tile to play on..."

        self.handTileSelectionMsg = ""
        self.stackTileSelectionMsg = ""

        self.givesAdvice = False
        self.askedForHelp = False

        # Call base class constructor
        super().__init__(name, color)

   # Select tile from hand
    def SelectHandTile(self, Players, Decks, playerNum, opponentNum):
        
        # Determine placability of hand tiles
        Decks[playerNum].DetermineHandPlacability(Decks[playerNum].stack, Decks[opponentNum].stack)
        
    # Select what stack to place on
    def SelectStackTile(self, Players, Decks, playerNum, opponentNum, tileToPlace):
        
        # Determine placability of stack tiles, given tile to place
        Decks[playerNum].DetermineStackPlacability(tileToPlace)
        Decks[opponentNum].DetermineStackPlacability(tileToPlace)

        # Reset status of hand tiles
        Decks[0].ResetHandTileStatus()
        Decks[1].ResetHandTileStatus()

        

    


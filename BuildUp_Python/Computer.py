
from Player import Player

class Computer(Player):

    # Constructor
    def __init__(self, name):
        self.color = 'W'
        self.name = name

        # Call base class constructor
        super().__init__()

     # For when in a hand, choosing where to place tile
    def TurnChoice(self, Players, Decks, playerNum):
        
        # Initalize current turn attributes
        self.turnDecks = Decks
        self.turnPlayers = Players
        self.playerNum = playerNum

        # Print player menu
        self.PlayerMenu() 

        # Logic here for placing tiles
        print("AHHH!")

    # Creates frame and label for row of buttons for the player's stack
    def CreateStackFrame(self, deck, mainFrame):
        
        # Create subframe 
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel("Stack", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put tile buttons into subframe
        for tile in range(len(deck.stack)):
            self.GUI.CreateTileLabel(deck.stack[tile], subFrame)

    # Creates frame and label for row of labels for the player's hand
    def CreateHandFrame(self, deck, mainFrame):
        # Create subframe 
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel("Hand", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put tile label into subframe
        for tile in range(len(deck.hand)):
            self.GUI.CreateTileLabel(deck.hand[tile], subFrame)


 
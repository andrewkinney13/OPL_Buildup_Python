
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

        print("AHHH!")

    # Creates frame and label for row of buttons for the player's stack
    def CreateStackFrame(self, player, deck, mainFrame):
        
        # Create subframe 
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s stack", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put tile buttons into subrame
        for tile in range(len(deck.stack)):
            self.GUI.CreateTileLabel(subFrame, deck.stack[tile])

    # Creates frame and label for row of labels for the player's hand
    def CreateHandFrame(self, player, deck, mainFrame):
        # Create subframe 
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s hand", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put tile label into subrame
        for tile in range(len(deck.hand)):
            self.GUI.CreateTileLabel(subFrame, deck.hand[tile])

 
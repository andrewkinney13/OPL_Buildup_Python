
from Player import Player

class Human(Player):
    
    # Constructor
    def __init__(self, name):
        self.color = 'B'
        self.name = name

        # Call base class constructor
        super().__init__()

    # For when in a hand, human gets to choose what to do
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
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s stack", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put tile buttons into subframe
        for tile in range(len(deck.stack)):
            self.GUI.CreateTileButton(deck.stack[tile], self.SelectTile, subFrame)

    # Creates frame and label for row of buttons for the player's hand
    def CreateHandFrame(self, player, deck, mainFrame):
        # Create subframe 
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s hand", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put tile buttons into subframe
        for tile in range(len(deck.hand)):
            self.GUI.CreateTileButton(deck.hand[tile], self.SelectTile, subFrame)


    # Selects the tile to try and place
    def SelectTile(self):
        self.PlaceTile()

    # Attempts to place the tile, if unsuccessful, re-calls TurnChoice
    def PlaceTile(self):
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("Tile placed!")
        self.CreateContinueButton()

    
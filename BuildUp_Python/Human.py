
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

    # Prints menu for Human player for their turn
    def PlayerMenu(self):

        # Clear the GUI and print heading
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("It's " + str(self.name) + "'s turn...")

        # Create mainframes to hold human and computer attributes
        humanMainFrame = self.GUI.CreateTileMainFrame('left')
        computerMainFrame = self.GUI.CreateTileMainFrame('right')

        # Create subframes for each player, with their attributes
        for playerNum in range(len(self.turnPlayers)):

            # Human, pass in human subframe
            if (self.turnPlayers[playerNum].color == 'W'):
                self.CreateStackFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], computerMainFrame)
                self.CreateHandFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], computerMainFrame)
                self.CreateBoneyardFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], computerMainFrame)
                
            # Computer, pass in computer subframe
            else:
                self.CreateStackFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], humanMainFrame)
                self.CreateHandFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], humanMainFrame)
                self.CreateBoneyardFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], humanMainFrame)

    # Creates frames a label and frames of buttons for the player's stack
    def CreateStackFrame(self, player, deck, mainFrame):
        
        # Create subframe 
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s stack", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put tile buttons into subrame
        for tile in range(len(deck.stack)):
            self.GUI.CreateTileButton(subFrame, deck.stack[tile], self.SelectTile)

    def CreateHandFrame(self, player, deck, mainFrame):
        # Create subframe 
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s hand", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put tile buttons into subrame
        for tile in range(len(deck.hand)):
            self.GUI.CreateTileButton(subFrame, deck.hand[tile], self.SelectTile)

    def CreateBoneyardFrame(self, player, deck, mainFrame):
        # Create subframe 
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s boneyard", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateTileSubFrame(mainFrame)

        # Put tile buttons into subrame
        count = 0
        for tile in range(len(deck.boneyard)):
            
            # No more than 6 boneyard tiles on subframe, reset if > 6 tiles on subframe
            if (count == 8):
                subFrame = self.GUI.CreateTileSubFrame(mainFrame)
                count = 0

            count += 1

            self.GUI.CreateTileButton(subFrame, deck.boneyard[tile], self.SelectTile)

    # Selects the tile to try and place
    def SelectTile(self):
        self.PlaceTile()

    # Attempts to place the tile, if unsuccessful, re-calls TurnChoice
    def PlaceTile(self):
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("Tile placed!")
        self.GUI.CreateButton("Continue", self.AfterTurnFunctions)
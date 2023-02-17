
from Player import Player

class Human(Player):
    
    # Constructor
    def __init__(self, name):
        self.color = 'B'
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


    # Selects the tile to try and place
    def SelectTile(self):
        self.PlaceTile()

    # Attempts to place the tile, if unsuccessful, re-calls TurnChoice
    def PlaceTile(self):
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("Tile placed!")
        self.GUI.CreateButton("Continue", self.AfterTurnFunctions)

        
    # Prints menu for Human player for their turn
    def PlayerMenu(self):

        # Clear the GUI and print heading
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("It's " + str(self.name) + "'s turn...")

        # Create mainframes to hold human and computer attributes
        humanMainFrame = self.GUI.CreateTileMainFrame('left')
        computerMainFrame = self.GUI.CreateTileMainFrame('right')

        # TO BE MADE INTO FUNCTION!

        # Runs for each player
        for playerNum in range(len(self.turnPlayers)):

            # Human side
            if (self.turnPlayers[playerNum].color == 'W'):

                # Create subframe 
                subFrame = self.GUI.CreateTileSubFrame(humanMainFrame)

                # Put player's name in label
                self.GUI.CreateLabel(str(self.turnPlayers[playerNum].name) + "'s stack", subFrame)

                # Put tile buttons into subrame
                for tile in range(len(self.turnDecks[playerNum].stack)):
                    self.GUI.CreateTileButton(subFrame, self.turnDecks[playerNum].stack[tile], self.SelectTile)

            # Computer side
            else:
                 # Create subframe 
                subFrame = self.GUI.CreateTileSubFrame(computerMainFrame)

                # Put player's name in label
                self.GUI.CreateLabel(str(self.turnPlayers[playerNum].name) + "'s stack", subFrame)

                # Put tile buttons into subrame
                for tile in range(len(self.turnDecks[playerNum].stack)):
                    self.GUI.CreateTileButton(subFrame, self.turnDecks[playerNum].stack[tile], self.SelectTile)


           

        
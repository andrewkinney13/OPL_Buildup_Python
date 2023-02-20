
from Tile import Tile
from Deck import Deck

class Player:
    # Constructor
    def __init__(self):
        self.score = 0
        self.roundsWon = 0
        self.isTheirTurn = False

    # Checks if player has playable tiles
    def HasPlayableTiles(self):
        return True

    # Sets functions to run after a turn
    def InitalizeRoundData(self, GUI, ChangeTurnFunction, ReturnToHandFunction):
        self.GUI = GUI
        self.ChangeTurnFunction = ChangeTurnFunction
        self.ReturnToHandFunction = ReturnToHandFunction

    # Prints menu for the current turn
    def PlayerMenu(self):

        # Clear the GUI and print heading
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("It's " + str(self.name) + "'s turn...")

        # Create mainframes to hold human and computer attributes
        leftMainFrame = self.GUI.CreateTileMainFrame('left')
        rightMainFrame = self.GUI.CreateTileMainFrame('right')

        # Create subframes for each player, with their attributes
        self.CreateSubFrame(0, leftMainFrame)
        self.CreateSubFrame(1, rightMainFrame)

        # Create continue or save buttons
        self.CreateContinueButton()

    # Creates the data for a player and their attributes 
    def CreateSubFrame(self, playerNum, mainFrame):
        self.CreateStackFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], mainFrame)
        self.CreateHandFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], mainFrame)
        self.CreateBoneyardFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], mainFrame)

    # Creates frame and label for row of labels for the player's hand
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

            self.GUI.CreateTileLabel(subFrame, deck.boneyard[tile])

    # Selects the tile to try and place
    def SelectTile(self):
        self.PlaceTile()

    # Attempts to place the tile, if unsuccessful, re-calls TurnChoice
    def PlaceTile(self):
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("Tile placed!")
        self.CreateContinueButton()

    # Runs after turn functons
    def AfterTurnFunctions(self):
        self.ChangeTurnFunction()
        self.ReturnToHandFunction()

    # Continue button w/ after turn functionality
    def CreateContinueButton(self):
        self.GUI.CreateButton("Continue", self.AfterTurnFunctions)

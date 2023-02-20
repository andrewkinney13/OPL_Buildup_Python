
from Tile import Tile
from Deck import Deck

class Player:
    # Constructor
    def __init__(self):
        self.score = 0
        self.roundsWon = 0
        self.isTheirTurn = False

    # Sets functions to run after a turn
    def InitalizeRoundData(self, GUI, ChangeTurnFunction, ReturnToHandFunction, SaveGameFunc):
        self.GUI = GUI
        self.ChangeTurnFunction = ChangeTurnFunction
        self.ReturnToHandFunction = ReturnToHandFunction
        self.SaveGameFunc = SaveGameFunc
        
    # Runs after turn functons
    def AfterTurnFunctions(self):
        self.ChangeTurnFunction()
        self.ReturnToHandFunction()

    # Prints menu for the current turn
    def PlayerMenu(self):

        # Clear the GUI and print heading
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("It's " + str(self.name) + "'s turn...")

        # Create mainframes to hold human and computer attributes
        leftMainFrame = self.GUI.CreatePlayerMainFrame('left')
        rightMainFrame = self.GUI.CreatePlayerMainFrame('right')

        # Create subframes for each player, with their attributes
        self.CreateSubFrames(0, leftMainFrame)
        self.CreateSubFrames(1, rightMainFrame)

        # Creates a button for continue or save, if it's the player's turn (only one button)
        if (self.isTheirTurn):
            self.CreateSaveButton(rightMainFrame)

            # Only continue option if computer player
            if(self.color == 'W'):
                self.CreateContinueButton(leftMainFrame)
            

    # Creates the data for a player and their attributes 
    def CreateSubFrames(self, playerNum, mainFrame):
        self.CreateStackFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], mainFrame)
        self.CreateHandFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], mainFrame)
        self.CreateBoneyardFrame(self.turnPlayers[playerNum], self.turnDecks[playerNum], mainFrame)
        self.CreateRestAttributesFrame(self.turnPlayers[playerNum], mainFrame)

    # Creates frame and label for row of labels for the player's hand
    def CreateBoneyardFrame(self, player, deck, mainFrame):
        # Create subframe 
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s boneyard", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put tile buttons into subrame
        count = 0
        for tile in range(len(deck.boneyard)):
            
            # No more than 8 boneyard tiles on subframe, reset if > 8 tiles on subframe
            if (count == 8):
                subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)
                count = 0

            count += 1

            self.GUI.CreateTileLabel(deck.boneyard[tile], subFrame)

    # Creates labels for rest of the player's attributes, like score and rounds won
    def CreateRestAttributesFrame(self, player, mainFrame):
        # Create subframe
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's attributes name label
        self.GUI.CreateLabel("Score: " + str(player.score), subFrame)
        self.GUI.CreateLabel("Rounds won: " + str(player.roundsWon), subFrame)

    # Checks if player has playable tiles
    def HasPlayableTiles(self):
        return True

     # Creates a button that exits the program and saves the game to a text file
    def CreateSaveButton(self, mainFrame):
        self.GUI.CreateButton("Save and Exit", self.SaveGameFunc, mainFrame, color = "red")

    # Creates a button to continue to next turn
    def CreateContinueButton(self, mainFrame = None):

        # No frame specified
        if (mainFrame == None):
            self.GUI.CreateButton("Continue", self.AfterTurnFunctions, color = "green")

        # Frame specified
        else:
            self.GUI.CreateButton("Continue", self.AfterTurnFunctions, mainFrame, color = "green")

    

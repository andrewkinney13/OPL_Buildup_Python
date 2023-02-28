
from DeckView import DeckView

class HumanView:
    
    # Constructor
    def __init__(self, GUI):
        self.GUI = GUI

    # Creates a screen asking user what tile from their hand to select
    def CreateTileScreen(self, Players, Decks, playerNum, opponentNum, TileFunction):

        # Clear the window
        self.GUI.ClearWindow()

        # Create label asking for expected input
        if (Players[playerNum].selectingHandTile):
            self.GUI.CreateMenuLabel(str(Players[playerNum].name) + "'s turn...\nPlease select a tile from your hand to play")

        elif(Players[playerNum].placingOnStackTile):
            self.GUI.CreateMenuLabel(str(Players[playerNum].name) + "'s turn...\nPlease select a stack tile to play on")

        else:
            self.GUI.CreateMenuLabel(str(Players[playerNum].name) + "'s turn over...\nBoard after your move")

        # Create frames for each player's attributes
        playerMainFrame = self.GUI.CreateMainFrame(Players[playerNum].side)
        opponentMainFrame = self.GUI.CreateMainFrame(Players[opponentNum].side)

        # Create subframes and labels for player's names
        self.CreateNameFrames(playerMainFrame, Players[playerNum].name)
        self.CreateNameFrames(opponentMainFrame, Players[opponentNum].name)

        # Create deck view object
        myDeckView = DeckView(self.GUI)

        # Have DeckView create frames for all of the attributes for each players deck, pass in function for when a tile is pressed
        myDeckView.CreateDeckSubFrames(playerMainFrame, Decks[playerNum], TileFunction)
        myDeckView.CreateDeckSubFrames(opponentMainFrame, Decks[opponentNum], TileFunction)

        # Create subframes and labels for player's score and rounds won
        self.CreatePlayerAttributeFrames(playerMainFrame, Players[playerNum])
        self.CreatePlayerAttributeFrames(opponentMainFrame, Players[opponentNum])

        # Create a save and exit button on the right side of the screen
        if (Players[playerNum].side == "right"):
            self.GUI.CreateSaveExitButton(playerMainFrame)

        else:
            self.GUI.CreateSaveExitButton(opponentMainFrame)

        # Create a continue button if the moves have been made
        if(not Players[playerNum].selectingHandTile and not Players[playerNum].placingOnStackTile):

            # Create it on the left side of the screen
            if (Players[playerNum].side == "left"):
                self.GUI.CreateFrameMenuButton("Continue", TileFunction, playerMainFrame, fg = "white", bg = "green")

            else:
                self.GUI.CreateFrameMenuButton("Continue", TileFunction, opponentMainFrame, fg = "white", bg = "green")


    # Creates subframes and labels for players names
    def CreateNameFrames(self, mainFrame, name):
        
        # Create subframe
        subFrame = self.GUI.CreateSubFrame(mainFrame)
        
        # Create label for the player's name
        self.GUI.CreateFrameMenuLabel("Name: " + str(name), subFrame)

    # Creates subframes and labels for players attributes (score, rounds won)
    def CreatePlayerAttributeFrames(self, mainFrame, player):
        
        # Create subframe
        subFrame = self.GUI.CreateSubFrame(mainFrame)

        # Put player's attributes in label
        self.GUI.CreateFrameMenuLabel("Score: " + str(player.score), subFrame)
        self.GUI.CreateFrameMenuLabel("Rounds won: " + str(player.roundsWon), subFrame)


import tkinter as tk
from DeckView import DeckView

class GUI():
    # Constructor
    def __init__(self):
        # Default attriutes of widgets
        self.defaultWidth = 40
        self.defaultHeight = 2
        self.defaultFont = ("Comic Sans MS", 14, "bold")

        # Initalize window
        self.root = tk.Tk()
        self.root.title("Andrew Kinney's BuildUp Program for OPL")
        self.root.geometry("900x900")

    # Starts input-driven window
    def StartInputLoop(self):
        self.root.mainloop()

    # Clears the window of all widgets
    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Creates menu button
    def CreateMenuButton(self, text, command, fg = "black", bg = "white"):

        # Create the button
        button = tk.Button(text = text, command = command, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, fg = fg, bg = bg)
        button.pack()

    # Creates menu button attatched to specified frame
    def CreateFrameMenuButton(self, text, command, frame, fg = "white", bg = "black"):
        
       # Create the button
        button = tk.Button(text = text, command = command, master = frame, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, fg = fg, bg = bg)
        button.pack()

    # Creates regular label 
    def CreateMenuLabel(self, text):

       # Create the label
        label = tk.Label(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont)
        label.pack()

    # Creates a label on the bottom of the screen
    def CreateBottomMenuLabel(self, text):

        # Create the label
        label = tk.Label(text = text, width = self.defaultWidth + 30, height = 7, font = self.defaultFont)
        label.pack(side = "bottom", fill = "y")

    # Creates regular menu label
    def CreateFrameMenuLabel(self, text, frame):

        # Create label 
        label = tk.Label(text = text, master = frame, width = self.defaultWidth, height = self.defaultHeight-1, font = self.defaultFont)
        label.pack()

    # Creates a main frame for subframes to attatch to, with specified side
    def CreateMainFrame(self, side):

        # Create frame
        frame = tk.Frame(self.root)
        frame.pack(side = side, fill = "y")

        # Return frame
        return frame

    # Creates subframe within mainframe
    def CreateSubFrame(self, mainFrame):

        # Create subframe in mainFrame
        subFrame = tk.Frame(mainFrame)
        subFrame.pack(side = "top")

        return subFrame

    # Sets the save function from Tournament class
    def SetSaveFunction(self, saveFunc):
        self.SaveFunction = saveFunc

    def GetSaveFunction(self):
        return self.SaveFunction


    """
       # Creates entry box with default attributes
    def CreateEntry(self):
        entry = tk.Entry(width = self.tileWidth, font = self.defaultFont)
        entry.pack()
        return entry
    """

    # Creates a screen asking user what tile from their hand to select
    def CreateTileScreen(self, Players, Decks, playerNum, opponentNum, TileFunction, ContinueFunction, HelpFunction,  topMsg = "", bottomMsg = ""):

        # Clear the window
        self.ClearWindow()

        # Create label asking for expected input
        if (Players[playerNum].selectingHandTile):
            self.CreateMenuLabel(str(Players[playerNum].name) + "'s turn...\n" + topMsg)

        elif(Players[playerNum].placingOnStackTile):
            self.CreateMenuLabel(str(Players[playerNum].name) + "'s turn...\n" + topMsg)

        else:
            self.CreateMenuLabel(str(Players[playerNum].name) + "'s turn over...\n" + topMsg)

         # Create an extra text box if text for a message was specified (make it here first so it doesn't get covered by y fill later on)
        if bottomMsg != None:
            self.CreateBottomMenuLabel(bottomMsg)

        # Create frames for each player's attributes
        playerMainFrame = self.CreateMainFrame("left")
        opponentMainFrame = self.CreateMainFrame("right")

        # Create subframes and labels for player's names
        self.CreateNameFrames(playerMainFrame, Players[playerNum].name, Players[playerNum].color)
        self.CreateNameFrames(opponentMainFrame, Players[opponentNum].name, Players[opponentNum].color)

        # Create deck view object
        myDeckView = DeckView(self)

        # Have DeckView create frames for all of the attributes for each players deck, pass in function for when a tile is pressed
        myDeckView.CreateDeckSubFrames(playerMainFrame, Decks[playerNum], TileFunction)
        myDeckView.CreateDeckSubFrames(opponentMainFrame, Decks[opponentNum], TileFunction)

        # Create subframes and labels for player's score and rounds won
        self.CreatePlayerAttributeFrames(playerMainFrame, Players[playerNum])
        self.CreatePlayerAttributeFrames(opponentMainFrame, Players[opponentNum])

        # Create a save and exit button on the right side of the screen
        SaveFunction = self.GetSaveFunction()
        self.CreateFrameMenuButton("Save and Exit", SaveFunction, opponentMainFrame, fg = "white", bg = "red")

        # Create a continue button if the moves have been made or no tiles selectable
        if(not Players[playerNum].selectingHandTile and not Players[playerNum].placingOnStackTile or self.NoSelectableTiles(playerNum, opponentNum, Decks)):
            self.CreateFrameMenuButton("Continue", ContinueFunction, playerMainFrame, fg = "white", bg = "green")

        # Create a button for helping, if this player can ask for, and the other player can give advicce
        elif(Players[playerNum].givesAdvice == False and Players[opponentNum].givesAdvice and Players[playerNum].selectingHandTile and Players[playerNum].askedForHelp == False):
            self.CreateFrameMenuButton("Ask for Help", HelpFunction, playerMainFrame, fg = "white", bg = "orange")


    # Creates subframes and labels for players names
    def CreateNameFrames(self, mainFrame, name, color):
        
        # Create subframe
        subFrame = self.CreateSubFrame(mainFrame)
        
        # Create label for the player's name
        self.CreateFrameMenuLabel("Name: " + str(name) + " (" + color + ")", subFrame)

    # Creates subframes and labels for players attributes (score, rounds won)
    def CreatePlayerAttributeFrames(self, mainFrame, player):
        
        # Create subframe
        subFrame = self.CreateSubFrame(mainFrame)

        # Put player's attributes in label
        self.CreateFrameMenuLabel("Score: " + str(player.score), subFrame)
        self.CreateFrameMenuLabel("Rounds won: " + str(player.roundsWon), subFrame)

    # Checks to see if a player has any selectable tiles on screen 
    def NoSelectableTiles(self, playerNum, opponentNum, Decks):
        
        # Check for hand placability
        for tileNum in range(len(Decks[playerNum].hand)):
            if Decks[playerNum].hand[tileNum].handPlacable:
                return False

        # Check for stack placability, player stack
        for tileNum in range(len(Decks[playerNum].stack)):
            if Decks[playerNum].stack[tileNum].stackPlacable:
                return False

        # Check for stack placability, opponenet stack
        for tileNum in range(len(Decks[opponentNum].stack)):
            if Decks[opponentNum].stack[tileNum].stackPlacable:
                return False

        # No tiles placeabile, return true
        return True
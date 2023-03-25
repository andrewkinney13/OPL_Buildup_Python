
"""
     ************************************************************
     * Name:  Andrew Kinney                                     *
     * Project:  BuildUp, Python Version                        *
     * Class:  Tournament View                                  *
     * Date:  3.25/2023                                         *
     ************************************************************
"""

class TournamentView:

    # Constructor
    def __init__(self, GUI):
        self.GUI = GUI


    # Inital start menu for initalizing game 
    # Asks user what kinds of players, or to load from file
    def StartMenu(self, DeclareHumanComputerGame, DeclareHumanHumanGame, DeclareComputerComputerGame, LoadSerializationFile):

        # Create title label
        self.GUI.CreateMenuLabel("Welcome to my BuildUp Program for OPL!\nPlease seleect how to initalize your game...")

        # Create buttons attatched to functions for selections
        self.GUI.CreateMenuButton("New Human vs Computer Game", DeclareHumanComputerGame)
        self.GUI.CreateMenuButton("New Human vs Human Game", DeclareHumanHumanGame)
        self.GUI.CreateMenuButton("New Computer vs Computer Game", DeclareComputerComputerGame)
        self.GUI.CreateMenuButton("Load Game from Serialization File", LoadSerializationFile)

         # Start the "mainloop" (event driven program)
        self.GUI.StartInputLoop()


    # Ask user what size domino set to play with
    def AskDominoSetSize(self, DeclareDecks):
       
        self.GUI.ClearWindow()
        self.GUI.CreateMenuLabel("What Size Set of Domino Tiles\nWould you Like to Play With?")
        self.GUI.CreateMenuButton("Double-six", lambda: (DeclareDecks(6)))
        self.GUI.CreateMenuButton("Double-seven", lambda: (DeclareDecks(7)))
        self.GUI.CreateMenuButton("Double-eight", lambda: (DeclareDecks(8)))
        self.GUI.CreateMenuButton("Double-nine", lambda: (DeclareDecks(9)))

    
    # Ask the user to enter the name of the serialization file
    def AskFileName(self, loadGame, invalidFileName = False):

        # Clear the window
        self.GUI.ClearWindow()

        # Create label asking for user to enter file name
        self.GUI.CreateMenuLabel("Seralization file name: ")

        # Create textbox to enter name
        entryBox = self.GUI.CreateEntry()

        # Make a button to enter the text
        self.GUI.CreateMenuButton("Enter", lambda: (self.GetEntryText(entryBox, loadGame)), fg = "white", bg = "green")

        # If this is the second+ time running, tell remind the user to enter a proper file name
        if invalidFileName:
            self.GUI.CreateMenuLabel("Invalid file name! Try again...")

        # Wait for user to continue
        self.GUI.StartInputLoop()

        
    # Obtains text from an entry box
    def GetEntryText(self, entryBox, returnFunction):
         text = entryBox.get()
         returnFunction(text)

    # Exit screen
    def ExitScreen(self, winnerNum):

        # Clear the screen
        self.GUI.ClearWindow()

        # Alert user who won
        if (winnerNum != None):
            self.GUI.CreateMenuLabel(str(winnerNum) + " won the tournament!")

        else:
            self.GUI.CreateMenuLabel("Tournament ended in a draw")

        # Exit button
        self.GUI.CreateMenuButton("Exit", exit)

    # Saved screen
    def SavedScreen(self, fileName):

        # Clear the screen
        self.GUI.ClearWindow()

        # Ask to exit
        self.GUI.CreateMenuLabel("Saving...\nSave file created, named: '" + fileName + "'")
        self.GUI.CreateMenuButton("Exit", exit, fg = "white", bg = "red")
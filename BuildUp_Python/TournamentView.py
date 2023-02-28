
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
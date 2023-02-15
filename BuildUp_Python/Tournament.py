
from GUI import GUI
from Player import Player
from Human import Human
from Computer import Computer
from Deck import Deck
from Round import Round

class Tournament:

    # Constructor
    def __init__(self, GUI):
        # Get the GUI
        self.GUI = GUI

        # Create inital menu screen
        self.GUI.CreateLabel("Welcome to my BuildUp Program for OPL!\nPlease seleect how to initalize your game...")
        self.GUI.CreateButton("New Two Player Game", self.InitTwoPlayers)
        self.GUI.CreateButton("New Four Player Game", self.InitFourPlayers)
        self.GUI.CreateButton("Load Game from Serialization File", self.LoadSerializationFile)

        # Start the "mainloop" (event driven program)
        self.GUI.StartInputLoop()

    # Play Tournament
    def PlayTournament(self):
        
        # Initalize Round object with players
        self.Round = Round(GUI, self.Players, self.Decks)

        # Clear the GUI
        self.GUI.ClearWindow()

        # Play a round of BuildUp
        self.Round.PlayRound()

    # Initalize new game with two players (1 human, 1 computer)
    def InitTwoPlayers(self):

        # Initalize 2 players
        self.Players = []
        self.Players.append(Human())
        self.Players.append(Computer())

        # Ask for size of domino set
        self.AskDominoSetSize()
        
    # Initalize new game with four players (2 human, 2 computer)
    def InitFourPlayers(self):

        # Initalize 4 players
        self.Players = []
        self.Players.append(Human())
        self.Players.append(Human())
        self.Players.append(Computer())
        self.Players.append(Computer())

        # Ask for size of domino set
        self.AskDominoSetSize()

    # Initalize new game from serialization file
    def LoadSerializationFile(self):

        # Load in file, assign attributes

        # Play Tournament
        self.PlayTournament()

    # Ask user what size domino set to play with
    def AskDominoSetSize(self):
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("What Size Set of Domino Tiles\nWould you Like to Play With?")
        self.GUI.CreateButton("Double-six", lambda: (self.SetDecks(6)))
        self.GUI.CreateButton("Double-seven", lambda: (self.SetDecks(7)))
        self.GUI.CreateButton("Double-eight", lambda: (self.SetDecks(8)))
        self.GUI.CreateButton("Double-nine", lambda: (self.SetDecks(9)))

    # Set deck w/ domino set size
    def SetDecks(self, size):
        self.Decks = []

        # Create as many decks as there are players, with domino set size
        for i in range(len(self.Players)):
            self.Decks.append(Deck(size))

        # Decks are last thing to initalize, start the tournament
        self.PlayTournament()




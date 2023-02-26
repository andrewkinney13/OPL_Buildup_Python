
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
        self.GUI.CreateButton("New Human vs Computer Game", self.DeclareHuamnComputerGame)
        self.GUI.CreateButton("New Human vs Human Game", self.DeclareHumanHumanGame)
        self.GUI.CreateButton("New Computer vs Computer Game", self.DeclareComputerComputerGame)
        self.GUI.CreateButton("Load Game from Serialization File", self.LoadSerializationFile)

        # Start the "mainloop" (event driven program)
        self.GUI.StartInputLoop()

    # Play Tournament
    def PlayTournament(self):
        
        # Initalize Round object with players
        self.Round = Round(self.GUI, self.Players, self.Decks, self.SaveGame)

        # Play a round of BuildUp
        self.Round.PlayRound(self.AskNewRound)

    # Declare 1 human, 1 computer
    def DeclareHuamnComputerGame(self):

        # Initalize 2 human players
        self.Players = []
        self.Players.append(Human('Human'))
        self.Players.append(Computer('Computer'))

        # Ask for size of domino set
        self.AskDominoSetSize()

    # Declare 2 humans
    def DeclareHumanHumanGame(self):

        # Initalize 2 human players
        self.Players = []
        self.Players.append(Human('Human 1'))
        self.Players.append(Human('Human 2'))

        # Ask for size of domino set
        self.AskDominoSetSize()

    # Declare 2 computers
    def DeclareComputerComputerGame(self):

        # Initalize 2 human players
        self.Players = []
        self.Players.append(Computer('Computer 1'))
        self.Players.append(Computer('Computer 2'))

        # Ask for size of domino set
        self.AskDominoSetSize()

    # Initalize game state from serialization file
    def LoadSerializationFile(self):

        # Load in file, assign attributes

        # Play Tournament
        self.PlayTournament()

    # Save the game to text file
    def SaveGame(self):
        exit()

    # Ask user what size domino set to play with
    def AskDominoSetSize(self):
        self.GUI.ClearWindow()
        self.GUI.CreateLabel("What Size Set of Domino Tiles\nWould you Like to Play With?")
        self.GUI.CreateButton("Double-six", lambda: (self.DeclareDecks(6)))
        self.GUI.CreateButton("Double-seven", lambda: (self.DeclareDecks(7)))
        self.GUI.CreateButton("Double-eight", lambda: (self.DeclareDecks(8)))
        self.GUI.CreateButton("Double-nine", lambda: (self.DeclareDecks(9)))

    # Set deck w/ domino set size
    def DeclareDecks(self, tileSetSize):
        self.Decks = []

        # Create as many decks as there are players, with domino set size
        for i in range(len(self.Players)):
            self.Decks.append(Deck(tileSetSize))

        # Decks are last thing to initalize, start the tournament
        self.PlayTournament()

    # Asks the user if they want to play another round of buildup
    def AskNewRound(self):
        # Clear the GUI
        self.GUI.ClearWindow()

        # Ask the user
        self.GUI.CreateLabel("Round over, play another round?")
        self.GUI.CreateButton("yes", self.PlayTournament, color = "green")
        self.GUI.CreateButton("no", self.FinalScreen, color = "red")

    # Show final screen with who won and stuff
    def FinalScreen(self):
        # Clear the GUI
        self.GUI.ClearWindow()

        # Print goodbye 
        self.GUI.CreateLabel("Tournament over!")
        self.GUI.CreateButton("exit", exit, color = "red")


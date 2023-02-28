
from GUI import GUI
from TournamentView import TournamentView
from Player import Player
from Human import Human
from Computer import Computer
from Deck import Deck
from Round import Round

class Tournament:

    # Constructor
    def __init__(self, GUI):
        
        # Initalize View object
        self.GUI = GUI
        self.GUI.SetSaveFunction(self.SaveGame)
        self.TournamentView = TournamentView(GUI)

        # Declare data members
        self.Players = []
        self.Decks = []

    # Starts Tournament, just initalizes everything
    def StartTournament(self):
        
        # Create the inital menu asking how to start the game
        self.TournamentView.StartMenu(self.DeclareHuamnComputerGame, self.DeclareHumanHumanGame, self.DeclareComputerComputerGame, self.LoadSerializationFile)

    # Plays rounds of buildup 
    def PlayTournament(self):
        
        # Plays a round of buildup
        myRound = Round(self.Players, self.Decks, self.GUI)
        myRound.PlayRound()
        
       
    def EndTournament(self):
        # Tournament over, determine the winner and exit
        winnerNum = self.DetermineWinner()
        self.TournamentView.ExitScreen(winnerNum)

    # Declare 1 human, 1 computer
    def DeclareHuamnComputerGame(self):

        # Initalize 2 human players
        self.Players.append(Human('Human', "left", self.GUI))
        self.Players.append(Computer('Computer', "right", self.GUI))

        # Ask for size of domino set
        self.TournamentView.AskDominoSetSize(self.DeclareDecks)

    # Declare 2 humans
    def DeclareHumanHumanGame(self):

        # Initalize 2 human players
        self.Players.append(Human('Human 1', "left", self.GUI))
        self.Players.append(Human('Human 2', "right", self.GUI))

        # Ask for size of domino set
        self.TournamentView.AskDominoSetSize(self.DeclareDecks)

    # Declare 2 computers
    def DeclareComputerComputerGame(self):

        # Initalize 2 human players
        self.Players.append(Computer('Computer 1', "left", self.GUI))
        self.Players.append(Computer('Computer 2', "right", self.GUI))

        # Ask for size of domino set
        self.TournamentView.AskDominoSetSize(self.DeclareDecks)

    # Initalize game state from serialization file
    def LoadSerializationFile(self):

        # Load in file, assign attributes

        # Play Tournament
        self.PlayTournament()

    # Save the game to text file
    def SaveGame(self):
        exit()

    # Set deck w/ domino set size
    def DeclareDecks(self, tileSetSize):

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

    # Determine the winner of the tournament
    def DetermineWinner(self):
        
         # Player 0 won
        if self.Players[0].roundsWon > self.Players[1].roundsWon:
            return 0

        # Players 1 won
        elif self.Players[1].roundsWon > self.Players[0].roundsWon:
            return 1

        # Tie
        else:
            return None





"""
     ************************************************************
     * Name:  Andrew Kinney                                     *
     * Project:  BuildUp, Python Version                        *
     * Class:  Tournament                                       *
     * Date:  3.25/2023                                         *
     ************************************************************
"""

from TournamentView import TournamentView
from Human import Human
from Computer import Computer
from Deck import Deck
from Round import Round
from Tile import Tile

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
        self.TournamentView.StartMenu(self.DeclareHuamnComputerGame, self.DeclareHumanHumanGame, self.DeclareComputerComputerGame, self.AskSerializationFileName)

    # Plays rounds of buildup 
    def PlayTournament(self):
        
        # Initalizes round object
        self.myRound = Round(self.Players, self.Decks, self.GUI)

        # Plays a round of buildup
        self.myRound.PlayRound()
       
    def EndTournament(self):
        # Tournament over, determine the winner and exit
        winnerNum = self.DetermineWinner()
        self.TournamentView.ExitScreen(winnerNum)

    # Declare 1 human, 1 computer
    def DeclareHuamnComputerGame(self):

        # Initalize 2 human players
        self.Players.append(Human('Human', "B", self.GUI))
        self.Players.append(Computer('Computer', "W", self.GUI))

        # Ask for size of domino set
        self.TournamentView.AskDominoSetSize(self.DeclareDecks)

    # Declare 2 humans
    def DeclareHumanHumanGame(self):

        # Initalize 2 human players
        self.Players.append(Human('Human_1', "B", self.GUI))
        self.Players.append(Human('Human_2', "W", self.GUI))

        # Ask for size of domino set
        self.TournamentView.AskDominoSetSize(self.DeclareDecks)

    # Declare 2 computers
    def DeclareComputerComputerGame(self):

        # Initalize 2 human players
        self.Players.append(Computer('Computer_1', "B", self.GUI))
        self.Players.append(Computer('Computer_2', "W", self.GUI))

        # Ask for size of domino set
        self.TournamentView.AskDominoSetSize(self.DeclareDecks)

    # Aquire the name of the seriaization file
    def AskSerializationFileName(self, invalidFileName = False):

        # Ask the user to enter the name of the serialization file
        self.TournamentView.AskFileName(self.LoadGame, invalidFileName)

    # Load a game from serialization file
    def LoadGame(self, fileName):
 
        # Try to open the file, if unable, re ask user
        fileFound = False
        while not fileFound:
            try: 
                file = open(fileName, "r")
                contents = file.read()
                file.close()
                fileFound = True

            except FileNotFoundError:
                self.AskSerializationFileName(invalidFileName = True)

        # File opened successfuly, load game state
        else:
            playerCount = 0
            lineList = []

            for line in contents.splitlines():
                lineList.append(line)

            # Go through every line
            lineNum = 0
            while lineNum < len(lineList) - 2:

                # Init computer
                if lineList[lineNum] == "Computer:":
                    self.Players.append(Computer("Computer", "W", self.GUI))

                # Init human
                elif lineList[lineNum] == "Human:":
                    self.Players.append(Human("Human", "B", self.GUI))

                # Init computer 1
                elif lineList[lineNum] == "Computer_1:":
                    self.Players.append(Computer(lineList[lineNum], "B", self.GUI))

                # Init human 1
                elif lineList[lineNum] == "Human_1:":
                    self.Players.append(Computer(lineList[lineNum], "B", self.GUI))

                # Init computer 2
                elif lineList[lineNum] == "Computer_2:":
                    self.Players.append(Computer(lineList[lineNum], "W", self.GUI))

                # Init human 2
                elif lineList[lineNum] == "Human_2:":
                    self.Players.append(Human(lineList[lineNum], "W", self.GUI))

                # Increment line num (account for getting name)
                lineNum += 1

                # Init deck
                self.Decks.append(Deck())

                # Initalize all the data for the player, update linenum
                lineNum = self.SerializePlayer(playerCount, lineList, lineNum)

                # Account for new line in between player data 
                lineNum += 1
                playerCount += 1

            # Last line, find out whose turn it is
            turnVal = ""
            turnLine = lineList[lineNum]
            for word in turnLine.split(" "):

                # skip header
                if word == "Turn:" or word == "":
                    continue

                # access tile values
                turnVal = word
                
            # Assign the turn to the appropriate player
            for playerNum in range(len(self.Players)):
                
                if self.Players[playerNum].name == turnVal:
                    self.Players[playerNum].isTheirTurn = True

            # Everything loaded in, play the tournament!
            self.PlayTournament()
            
        
    # Initalize a players attributes based on serialization file
    def SerializePlayer(self, playerNum, lineList, lineNum):
        
        # Initalize the stack
        stackLine = lineList[lineNum]
        for word in stackLine.split(" "):

            # skip header
            if word == "Stacks:" or word == "":
                continue

            # access tile values
            self.Decks[playerNum].stack.append(Tile(word[0], int(word[1]), int(word[2])))
        lineNum += 1

        # Initalize the boneyard
        boneyardLine = lineList[lineNum]
        for word in boneyardLine.split(" "):

            # skip header
            if word == "Boneyard:" or word == "":
                continue

            # access tile values
            self.Decks[playerNum].boneyard.append(Tile(word[0], int(word[1]), int(word[2])))
        lineNum += 1

        # Initalize the hand
        handLine = lineList[lineNum]
        for word in handLine.split(" "):

            # skip header
            if word == "Hand:" or word == "":
                continue

            # access tile values
            self.Decks[playerNum].hand.append(Tile(word[0], int(word[1]), int(word[2])))
        lineNum += 1
        
        # Initalize the score
        scoreLine = lineList[lineNum]
        for word in scoreLine.split(" "):

            # skip header
            if word == "Score:" or word == "":
                continue

            # access tile values
            self.Players[playerNum].score = int(word)
        lineNum += 1

        # Initalize the rounds won
        roundLine = lineList[lineNum]
        for word in roundLine.split(" "):

            # skip header
            if word == "Rounds" or word == "Won:" or word == "":
                continue

            # access tile values
            self.Players[playerNum].roundsWon = int(word)
        lineNum += 1
        
        return lineNum
        
    # Save the game to text file
    def SaveGame(self):

        # Create a text file
        fileName = "savedBuildup.txt"
        file = open(fileName, "w")

        # Write the data to the file
        for playerNum in range(len(self.Players)):

            # Write their name
            file.write(self.Players[playerNum].name + ":\n")

            # Write their stacks
            file.write("    Stacks: ")
            for tileNum in range(len(self.Decks[playerNum].stack)):
                file.write(self.Decks[playerNum].stack[tileNum].GetStringForm() + " ")
            file.write("\n")

            # Write their boneyards
            file.write("    Boneyard: ")
            for tileNum in range(len(self.Decks[playerNum].boneyard)):
                file.write(self.Decks[playerNum].boneyard[tileNum].GetStringForm() + " ")
            file.write("\n")

            # Write their hands 
            file.write("    Hand: ")
            for tileNum in range(len(self.Decks[playerNum].hand)):
                file.write(self.Decks[playerNum].hand[tileNum].GetStringForm() + " ")
            file.write("\n")

            # Write their score
            file.write("    Score: " + str(self.Players[playerNum].score))
            file.write("\n")

            # Write their rounds won
            file.write("    Rounds Won: " + str(self.Players[playerNum].roundsWon))
            file.write("\n\n")
            
        # Write the turn status
        file.write("Turn: ")

        if (self.Players[0].isTheirTurn):
            file.write(self.Players[0].name)

        else:
            file.write(self.Players[1].name)

        # Close the file
        file.close()

        # Alert the user, ask to exit
        self.TournamentView.SavedScreen(fileName)

        
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
        self.GUI.CreateButton("New Round", self.PlayTournament, color = "green")
        self.GUI.CreateButton("End Tournament", self.FinalScreen, color = "red")





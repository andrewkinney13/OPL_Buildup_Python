
from RoundView import RoundView
from Tile import Tile

class Round:
    # Constructor
    def __init__(self, Players, Decks, GUI):
        
        # Initalize View object
        self.GUI = GUI
        self.RoundView = RoundView(GUI)
        
        # Initalize data members 
        self.Players = Players
        self.Players[0].SetPlayHandFunction(self.PlayHand)
        self.Players[1].SetPlayHandFunction(self.PlayHand)
        self.Decks = Decks
        self.turnNum = 999
        self.opponentNum = 999

    # Plays round
    def PlayRound(self):

        # Initalize decks
        self.InitalizeDecks()

        # Set first turn
        self.SetFirstTurn()

        # If hand successfully created (boneyard tiles remain), play a hand
        if (len(self.Decks[0].hand)):
            self.PlayHand()

        # End the round if not
        else:           
            # Clear everything
            self.ClearHands()
            self.ClearStacks()

            # Determine the winner of the round
            winnerNum, winnerMsg = self.DetermineWinner()

            # Create a screen asking if user wants to play another hand
            self.RoundView.AskNewRound(winnerNum, winnerMsg, self.EndTournament, self.PlayRound) 
        
    # Play hand of buildup until no playable tiles remain
    def PlayHand(self):

        # Check if hand is over
        if (self.PlayableTilesRemain()):

            # If player who has the turn can place tile, let them
            if (self.Decks[self.turnNum].HasPlayableTiles(self.Decks[0].stack, self.Decks[1].stack)):
                
                # Player is selecting from hand to place
                if(self.Players[self.turnNum].selectingHandTile):

                    # Let them choose the hand tile
                    self.Players[self.turnNum].SelectHandTile(self.Players, self.Decks, self.turnNum, self.opponentNum)

                    # Dsplay tile screen
                    self.GUI.CreateTileScreen(self.Players, self.Decks, self.turnNum, self.opponentNum, self.Players[self.turnNum].TileSelected, \
                        self.PlayHand, self.Players[self.turnNum].handTileSelectionPrompt, "")

                   
                # Player selects the tile on stack to place on 
                elif(self.Players[self.turnNum].placingOnStackTile):

                    # Highlight the tile they chose
                    self.Decks[self.turnNum].HighlightHandTile(self.Players[self.turnNum].tileToPlace)

                    # Let them chose the stack tile
                    self.Players[self.turnNum].SelectStackTile(self.Players, self.Decks, self.turnNum, self.opponentNum, self.Players[self.turnNum].tileToPlace) 

                    # Display the tile screen
                    self.GUI.CreateTileScreen(self.Players, self.Decks, self.turnNum, self.opponentNum, self.Players[self.turnNum].TileSelected, \
                        self.PlayHand, self.Players[self.turnNum].stackTileSelectionPrompt, self.Players[self.turnNum].handTileSelectionMsg)
                    
            
                # Tile from hand selected, and stack tile to play on selected, place the tile and end the turn
                else:
                    # Find out the position and stack of the tiles
                    stackNum, stackPosition = self.FindStackLocation(self.Players[self.turnNum].tileToPlaceOn)

                    # Place the tile
                    self.Decks[stackNum].PlaceTileOnStack(self.Players[self.turnNum].tileToPlace, stackPosition)

                    # Remove tile from player's hand
                    self.Decks[self.turnNum].RemoveHandTile(self.Players[self.turnNum].tileToPlace)

                    # Reset the status of the stack tiles
                    self.Decks[0].ResetStackTileStatus()
                    self.Decks[1].ResetStackTileStatus()

                    # Display finished board
                    self.GUI.CreateTileScreen(self.Players, self.Decks, self.turnNum, self.opponentNum, self.Players[self.turnNum].TileSelected, \
                        self.PlayHand, "", self.Players[self.turnNum].stackTileSelectionMsg)

                    # Reset the player's tiles' status
                    self.Decks[self.turnNum].ResetHighlightedTileStatus()
                    self.Decks[self.opponentNum].ResetHighlightedTileStatus()

                    # Change turns 
                    self.ChangeTurns()

            # If they can't skip their turn
            else:

                # Create a screen to tell the user a turn is being skipped
                self.GUI.CreateTileScreen(self.Players, self.Decks, self.turnNum, self.opponentNum, self.Players[self.turnNum].TileSelected, \
                        self.PlayHand, "No moves to make, turn being skipped")

                # Change turns 
                self.ChangeTurns()

        # Hand is over
        else:

            # Add up the scores, get reasoning
            scoresMsg = self.AddUpScores()

            # Print the board and score msg
            self.GUI.CreateTileScreen(self.Players, self.Decks, self.turnNum, self.opponentNum, self.Players[self.turnNum].TileSelected, \
                        self.PlayRound, "Hand over, adding up scores...", scoresMsg)

            # Clear hands
            self.ClearHands()

    # See if playable tiles are left in any player's hand
    def PlayableTilesRemain(self):

        # Go through each player, if at any point someone can play, return true
        for deckNum in range(2):
            if (self.Decks[deckNum].HasPlayableTiles(self.Decks[0].stack, self.Decks[1].stack)):
                return True

        # No one has a playable tile
        return False

    # See if the player with turn is selecting a tile from hand to place
    def IsPlayerSelectingHandTile(self):
        for playerNum in range(2):
            if (self.Players[playerNum].selectingHandTile):
                return True

        return False

    # See if the player with the turn is placing a tile onto a stack tile
    def IsPlayerPlacingOnStack(self):
        for playerNum in range(2):
            if (self.Players[playerNum].placingOnStackTile):
                return True

        return False

    # Gives turn to next player
    def ChangeTurns(self):

        # Player 0 had turn
        if (self.Players[0].isTheirTurn):
            self.Players[0].SetTheirTurn(False)
            self.Players[1].SetTheirTurn(True)
            self.turnNum = 1
            self.opponentNum = 0

        # Player 1 had turn
        else:
            self.Players[0].SetTheirTurn(True)
            self.Players[1].SetTheirTurn(False)
            self.turnNum = 0
            self.opponentNum = 1

    # Assigns first turn based on first hand tile value, if not assigned already by serialization
    def SetFirstTurn(self):

        # Return without assigining if turn already set
        for playerNum in range(2):
            if (self.Players[playerNum].isTheirTurn):
                self.turnNum = playerNum

                if (self.turnNum == 0):
                    self.opponentNum = 1
                else:
                    self.opponentNum = 0

                return

        # Assign first turn based on value of first non-duplicate hand tile
        notFound = True 
        tileNum = 0
        turnName = ""

        # Run a loop until non duplicate is found and turn assigned
        while notFound:

            # Player 0 gets turn
            if self.Decks[0].hand[tileNum].GetValue() > self.Decks[1].hand[tileNum].GetValue():
                self.Players[0].SetTheirTurn(True)
                self.turnNum = 0
                self.opponentNum = 1
                turnName = self.Players[0].name
                notFound = False

            # Player 1 gets turn
            elif self.Decks[1].hand[tileNum].GetValue() > self.Decks[0].hand[tileNum].GetValue():
                self.Players[1].SetTheirTurn(True)
                self.turnNum = 1
                self.opponentNum = 0
                turnName = self.Players[1].name
                notFound = False

            # Check the next tile
            else:
                tileNum += 1

        # print screen showing what happend 
        self.GUI.CreateTileScreen(self.Players, self.Decks, self.turnNum, self.opponentNum, self.Players[self.turnNum].TileSelected, \
                        self.PlayHand, "Determining first turn based on hand tile scores", turnName + " had the highest first hand tile...\nThey go first!")

        # start game
        self.GUI.StartInputLoop()

    # Initalizes decks 
    def InitalizeDecks(self):

        # Check if stack sizes aren't zero (serialization)
        if (len(self.Decks[0].stack) != 0):
    
            # Check if the hands are set, if not, set them
            if (len(self.Decks[0].hand) == 0):
                self.InitalizeHands()
            # Otherwise do nothing

        # Otherwise, initalize everything
        else:
            self.InitalizeBoneyards()
            self.InitalizeStacks()
            self.InitalizeHands()

    # Add up the scores at the end of a hand
    def AddUpScores(self):

        # Declare variables
        scoresMsg = ""

        orgScores = []
        orgScores.append(self.Players[0].score)
        orgScores.append(self.Players[1].score)

        gainedScores = [0] * 2

        lostScores = [0] * 2

        # Go through all the tiles on each player's stack
        for playerNum in range(len(self.Players)):

            # determine opponent's number
            if playerNum == 0:
                opponentNum = 1
            else:
                opponentNum = 0

            # Go through each tile on stack
            for tileNum in range(len(self.Decks[playerNum].stack)):
                
                # Check if it's this players tile (add score to them)
                if (self.Decks[playerNum].stack[tileNum].color == self.Players[playerNum].color):
                    self.Players[playerNum].score += self.Decks[playerNum].stack[tileNum].GetValue()  
                    gainedScores[playerNum] += self.Decks[playerNum].stack[tileNum].GetValue()

                # Other players tile, add to their score
                else:
                    self.Players[opponentNum].score += self.Decks[playerNum].stack[tileNum].GetValue()
                    gainedScores[opponentNum] += self.Decks[playerNum].stack[tileNum].GetValue()


        # Subtract all the tiles remaining in each player's hand
        for playerNum in range(len(self.Players)):

            # Go through each hand tile
            for tileNum in range(len(self.Decks[playerNum].hand)):

                # Subtract it's value from their score
                self.Players[playerNum].score -= self.Decks[playerNum].hand[tileNum].GetValue()
                lostScores[playerNum] += self.Decks[playerNum].hand[tileNum].GetValue()

        # Write a nice score message to explain score change
        for playerNum in range(len(self.Players)):

            scoresMsg += self.Players[playerNum].name + " gained " + str(gainedScores[playerNum]) + " points, lost " + str(lostScores[playerNum]) + " points\n"
            scoresMsg += str(orgScores[playerNum]) + " (original score) + " + str(gainedScores[playerNum]) + " - " + str(lostScores[playerNum]) + \
                " = " + str(self.Players[playerNum].score) + "\n\n"

        # Return the reasoning
        return scoresMsg

    # Clear the remaining tiles in hand
    def ClearHands(self):
        for playerNum in range(2):
            self.Decks[playerNum].hand.clear()

    # Clears the stack
    def ClearStacks(self):
        for playerNum in range(2):
            self.Decks[playerNum].stack.clear()

    # Initalizes all the hands
    def InitalizeHands(self):
        for playerNum in range(2):
            self.Decks[playerNum].CreateHand()

    # Initalizes all the boneyards
    def InitalizeBoneyards(self):
        for playerNum in range(2):
            self.Decks[playerNum].CreateBoneyard(self.Players[playerNum].color)

    # Initalizes all the stacks
    def InitalizeStacks(self):
        for playerNum in range(2):
            self.Decks[playerNum].CreateStack()

    # Determines who won the round, adds a win to their score, returns the player number of who one
    def DetermineWinner(self):

        # Player 0 won
        if self.Players[0].score > self.Players[1].score:
            self.Players[0].roundsWon += 1
            return (0, "haha0")

        # Players 1 won
        elif self.Players[1].score > self.Players[0].score:
            self.Players[1].roundsWon += 1
            return (0, "haha1")

        # Tie
        else:
            return (None, "tie!")
            
    # Returns to the tournament class
    def EndTournament(self):
        self.EndTournament()

    # Sets the return to tournament function
    def SetEndTournamentFunction(self, endFunction):
        self.EndTournamentFunc = endFunction

    # Finds what stack and where a tile is
    def FindStackLocation(self, tile):

        # Check in player stack for tile
        for tileNum in range(len(self.Decks[self.turnNum].stack)):
            if (tile == self.Decks[self.turnNum].stack[tileNum]):
                return (self.turnNum, tileNum)

        # Check in opponent stack for tile
        for tileNum in range(len(self.Decks[self.opponentNum].stack)):
            if (tile == self.Decks[self.opponentNum].stack[tileNum]):
                return (self.opponentNum, tileNum)
        

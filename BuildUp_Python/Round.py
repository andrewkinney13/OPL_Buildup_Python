
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
        self.count1 = 99
        self.count2 = 99

    # Plays round
    def PlayRound(self):

        # Initalize decks
        self.InitalizeDecks()

        # Set first turn
        self.SetFirstTurn()

        # If hand successfully created (boneyard tiles remain), play a hand
        if (len(self.Decks[0].hand)):
            self.count1 -= 1
            self.PlayHand()

        # This is just for testing, but would be the case if a round ends
        # Once scoring properly implemented, change if statement to an else
        if (self.count1 <= 0):
           
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
                    self.Players[self.turnNum].SelectHandTile(self.Players, self.Decks, self.turnNum, self.opponentNum)
                   
                # Player selects the tile on stack to place on 
                elif(self.Players[self.turnNum].placingOnStackTile):
                    self.Decks[self.turnNum].HighlightHandTile(self.Players[self.turnNum].tileToPlace)
                    self.Players[self.turnNum].SelectStackTile(self.Players, self.Decks, self.turnNum, self.opponentNum, self.Players[self.turnNum].tileToPlace)
            
                # Tile from hand selected, and stack tile to play on selected, end the turn
                else:
                    # Find out the position and stack of the tiles
                    stackNum, stackPosition = self.FindStackLocation(self.Players[self.turnNum].tileToPlaceOn)

                    # Place the tile
                    self.Decks[stackNum].PlaceTileOnStack(self.Players[self.turnNum].tileToPlace, stackPosition)

                    # Remove tile from player's hand
                    self.Decks[self.turnNum].RemoveHandTile(self.Players[self.turnNum].tileToPlace)

                    # Display finished board
                    self.Players[self.turnNum].DisplayBoard(self.Players, self.Decks, self.turnNum, self.opponentNum, self.PlayHand)

                    # Reset the player's tiles' status
                    self.Decks[self.turnNum].ResetHighlightedTileStatus()
                    self.Decks[self.opponentNum].ResetHighlightedTileStatus()

                    # Change turns 
                    self.ChangeTurns()

            # If they can't skip their turn
            else:

                # Create a screen to tell the user a turn is being skipped
                self.TournamentView.SkipTurn(self.turnNum)

                # Change turns 
                self.ChangeTurns()

        # Hand is over
        else:

            # Add up the scores, get reasoning
            scoresMsg = self.AddUpScores()

            # Clear the remaining tiles in hand
            self.ClearHands()

            # Create a screen for user to see the new scores and play next hand
            self.RoundView.EndOfHandScreen(scoresMsg, self.PlayHand)


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

        # Assign first turn based on hand value
        self.Players[0].SetTheirTurn(True)
        self.turnNum = 0
        self.opponentNum = 1

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
        return "haha"

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
        

    # ---------------------------------------- GUI STUFF ----------------------------------------

"""
    # Prints menu for the current turn
    def CreateTurnMenu(self):

        # Clear the GUI and print heading
        self.GUI.ClearWindow()

        # Find if there's a selected hand tile
        for playerNum in range(2):
            if (self.Players[playerNum].isTheirTurn and not self.Players[playerNum].selectingHandTile):
                self.TileToPlace = self.Players[playerNum].TileToPlace

        # Gather text for heading label, name
        headingText = ""
        if (self.Players[0].isTheirTurn):
            headingText += "It's " + self.Players[0].name + "'s turn\n"

        else: 
            headingText += "It's " + self.Players[1].name + "'s turn\n"

        # Gather text for heading label, expected action
        if (self.PlayerSelectingHandTile()):
           headingText += self.Players[self.turnNum].SelectionPrompt

        elif (self.PlayerPlacingOnStack()):
            headingText += self.Players[self.turnNum].PlacementPrompt

        # Create heading label
        self.GUI.CreateLabel(headingText)

        # Create mainframes to hold human and computer attributes
        leftMainFrame = self.GUI.CreatePlayerMainFrame('left')
        rightMainFrame = self.GUI.CreatePlayerMainFrame('right')

        # Create subframes for each player, with their attributes
        self.CreateSubFrames(0, leftMainFrame)
        self.CreateSubFrames(1, rightMainFrame)

        # Creates a button for saving the game
        self.CreateSaveButton(rightMainFrame)

        # Creates a button for continuing, if no moves left for player who has the turn or computer player's turn
        for playerNum in range(2):

            if (self.Players[playerNum].isTheirTurn and not self.Players[playerNum].HasRemainingMoves()):
                self.CreateContinueButton(leftMainFrame)

            elif (self.Players[playerNum].color == 'W' and self.Players[playerNum].isTheirTurn):
                self.CreateNextComputerMoveButton(leftMainFrame)
            
    # Creates the data for a player and their attributes 
    def CreateSubFrames(self, playerNum, mainFrame):
        self.CreateNameFrame(self.Players[playerNum], mainFrame)
        self.CreateStackFrame(self.Decks[playerNum], self.Players[playerNum], mainFrame)
        self.CreateHandFrame(self.Decks[playerNum], self.Players[playerNum], mainFrame)
        self.CreateBoneyardFrame(self.Decks[playerNum], mainFrame)
        self.CreateRestAttributesFrame(self.Players[playerNum], mainFrame)

    # Creates a title frame for the player's attributes
    def CreateNameFrame(self, player, mainFrame):
        # Create subframe
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel(str(player.name) + "'s Data", subFrame)

    # Creates frame and label for row of buttons for the player's stack
    def CreateStackFrame(self, deck, player, mainFrame):
        
        # Create subframe 
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel("Stack", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put tile buttons into subframe
        for tile in range(len(deck.stack)):
            self.GUI.CreateTileLabel(deck.stack[tile], subFrame)

    # Creates frame and label for row of buttons for the player's hand
    def CreateHandFrame(self, deck, player, mainFrame):
        # Create subframe 
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel("Hand", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put tiles into subframe

        # Selectable tiles of player who's selecting hand tiles
        if (player.selectingHandTile):
            for tile in range(len(deck.hand)):
                self.GUI.CreateTileButton(deck.hand[tile], player.SelectHandTile, subFrame)

        # Unselectable tiles, player is not selecting tiles or already made selection
        else:
            for tile in range(len(deck.hand)):

                # If making label for selected tile, highlight it
                if (deck.hand[tile] == self.TileToPlace):
                    self.GUI.CreateTileLabel(deck.hand[tile], subFrame, highlighted = True)

                # Otherwise, make it a regular tile
                else:
                    self.GUI.CreateTileLabel(deck.hand[tile], subFrame)

    # Creates frame and label for row of labels for the player's hand
    def CreateBoneyardFrame(self, deck, mainFrame):
        # Create subframe 
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's name in label
        self.GUI.CreateLabel("Boneyard", subFrame)

        # Reinit subframe so buttons are centered (i dont know why we have to do this)
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put tiles into subrame
        count = 0
        for tile in range(len(deck.boneyard)):
            
            # Keep track of how many tiles placed, make it so only 2 rows are made of boneyard tiles
            if (count > len(deck.boneyard) / 5):
                subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)
                count = 0

            count += 1

            # Create the tile
            self.GUI.CreateTileLabel(deck.boneyard[tile], subFrame)

    # Creates labels for rest of the player's attributes, like score and rounds won
    def CreateRestAttributesFrame(self, player, mainFrame):
        # Create subframe
        subFrame = self.GUI.CreateAttributeSubFrame(mainFrame)

        # Put player's attributes name label
        self.GUI.CreateLabel("Score: " + str(player.score), subFrame)
        self.GUI.CreateLabel("Rounds won: " + str(player.roundsWon), subFrame)


     # Creates a button that exits the program and saves the game to a text file
    def CreateSaveButton(self, mainFrame):
        self.GUI.CreateButton("Save and Exit", self.SaveGameFunc, mainFrame, color = "red")

    # Creates a button to continue to next turn
    def CreateContinueButton(self, mainFrame = None):

        # No frame specified
        if (mainFrame == None):
            self.GUI.CreateButton("Continue", self.ContineuButtonFunctions, color = "green")

        # Frame specified
        else:
            self.GUI.CreateButton("Continue", self.ContineuButtonFunctions, mainFrame, color = "green")

    # Functions ran after pressing a button
    def ContineuButtonFunctions(self):
        self.ChangeTurnFunction()
        self.ReturnToHandFunction()

    # Creates a button to continue to next move (for when watching computer)
    def CreateNextComputerMoveButton(self, mainFrame):
        self.GUI.CreateButton("Next Move", self.NextComputerMoveFunctions, mainFrame, color = "green")

    # Runs next function for computer 
    def NextComputerMoveFunctions(self):

        # If the computer is selecting a hand tile
        if (self.Players[self.turnNum].selectingHandTile):
            self.Players[self.turnNum].SelectHandTile(self.Decks[self.turnNum].hand, self.Decks[self.turnNum].stack, self.Decks[self.opponentNum].stack)

        # If the computer is placing onto stack tile
        elif(self.Players[self.turnNum].placingOnStackTile):
            self.Players[self.turnNum].PlaceOnStackTile()

"""
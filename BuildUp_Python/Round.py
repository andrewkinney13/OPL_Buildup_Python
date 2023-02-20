
from pickle import FALSE
from GUI import GUI

class Round:
    # Constructor
    def __init__(self, GUI, Players, Decks):
        # Initalize data members 
        self.GUI = GUI
        self.Players = Players
        self.Decks = Decks
        self.count1 = 5
        self.count2 = 8

        # Initalize player's data
        for playerNum in range(2):
            self.Players[playerNum].InitalizeRoundData(self.GUI, self.ChangeTurns, self.PlayHand)

    # Plays round
    def PlayRound(self, retFunc):
        
        # Set return function
        self.retFunc = retFunc

        # Initalize decks
        self.InitalizeDecks()

        # Set first turn
        self.SetFirstTurn()

        # If hand successfully created, play a round
        if (len(self.Decks[0].hand) != 0 or self.count2 >= 0):
            self.count1 -= 1
            self.count2 = 8
            self.PlayHand()

        # This is just for testing
        if (self.count1 <= 0):
           
           # let em' know and return to tournament 
           self.GUI.ClearWindow()
           self.GUI.CreateLabel("Round Over!")
           self.GUI.ClearStacks()
           self.GUI.CreateButton("Continue", retFunc)

        """
        # If hand not created, round is over
           else: 
            self.GUI.ClearWindow()
            self.GUI.CreateLabel("Round Over!")
            self.GUI.ClearStacks()
            self.GUI.CreateButton("Continue", retFunc)
        """
        

    # Play hand of buildup until no playable tiles remain
    def PlayHand(self):

        # Check if hand is over
        if (self.PlayableTilesRemain() and self.count2 != 0):

            # Cycle through players
            for playerNum in range(len(self.Players)):

                # If their turn, let them play
                if (self.Players[playerNum].isTheirTurn and self.Players[playerNum].HasPlayableTiles()):
                    self.Players[playerNum].TurnChoice(self.Players, self.Decks, playerNum)
                    break
            
            self.count2 -= 1

        # Hand is over
        else:

            # Add up the scores
            self.AddUpScores()

            # Clear the remaining tiles in hand
            self.ClearHands()

            # Alert the user
            self.GUI.ClearWindow()
            self.GUI.CreateLabel("Hand Over!")
            self.GUI.CreateButton("Continue", lambda: (self.PlayRound(self.retFunc)))

    # See if playable tiles are left in any player's hand
    def PlayableTilesRemain(self):

        # Go through each player, if at any point someone can play, return true
        for playerNum in range(2):
            if (self.Players[playerNum].HasPlayableTiles()):
                return True

        # No one has a playable tile
        return False

    # Gives turn to next player
    def ChangeTurns(self):

        # Player 0 had turn
        if (self.Players[0].isTheirTurn):
            self.Players[0].isTheirTurn = False
            self.Players[1].isTheirTurn = True

        # Player 1 had turn
        else:
            self.Players[1].isTheirTurn = False
            self.Players[0].isTheirTurn = True

    # Assigns first turn based on first hand tile value, if not assigned already by serialization
    def SetFirstTurn(self):

        # Return without assigining if turn already set
        for playerNum in range(2):
            if (self.Players[playerNum].isTheirTurn == True):
                return

        # Assign first turn based on hand value
        self.Players[0].isTheirTurn = True

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
        pass

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
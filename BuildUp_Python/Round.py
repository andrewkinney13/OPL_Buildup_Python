
from GUI import GUI

class Round:
    # Constructor
    def __init__(self, GUI, Players, Decks):
        # Initalize data members 
        self.GUI = GUI
        self.Players = Players
        self.Decks = Decks
        self.count = 8;

        # Initalize player's data
        for playerNum in range(len(self.Players)):
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
        if (len(self.Decks[0].hand) != 0 or self.count >= 0):
            self.PlayHand()

        # This is just for testing
        if (self.count <= 0):
           # add up scores func
           # let em' know and return to tournament 
           self.GUI.ClearWindow()
           self.GUI.CreateLabel("Round Over!")
           self.GUI.CreateButton("Continue", retFunc)

        """
        # If hand not created, round is over
           else: 
            self.GUI.ClearWindow()
            self.GUI.CreateLabel("Round Over!")
            self.GUI.CreateButton("Continue", retFunc)
        """
        

    # Play hand of buildup until no playable tiles remain
    def PlayHand(self):

        # Clear GUI
        self.GUI.ClearWindow()

        # Check if hand is over
        if (self.PlayableTilesRemain() and self.count != 0):
            print(self.count)
            self.Players[0].score += 15

            # Cycle through players
            for playerNum in range(len(self.Players)):

                # If their turn, let them play
                if (self.Players[playerNum].isTheirTurn and self.Players[playerNum].HasPlayableTiles()):
                    self.Players[playerNum].TurnChoice(self.Decks, playerNum)
                    break
            
            self.count -= 1

        else:
            self.GUI.CreateLabel("Hand Over!")
            self.GUI.CreateButton("Continue", lambda: (self.PlayRound(self.retFunc)))

    # See if playable tiles are left in any player's hand
    def PlayableTilesRemain(self):

        # Go through each player, if at any point someone can play, return true
        for playerNum in range(len(self.Players)):
            if (self.Players[playerNum].HasPlayableTiles()):
                return True

            # No one has a playable tile
            return False

    # Gives turn to next player
    def ChangeTurns(self):

        # Go through each player
        for playerNum in range(len(self.Players)):

            # Find who has current turn
            if (self.Players[playerNum].isTheirTurn):

                # Unassign the turn
                self.Players[playerNum].isTheirTurn = False

                # They're the last player in list, assign turn to player zero
                if(playerNum == len(self.Players) - 1):
                    self.Players[0].isTheirTurn = True
                    return

                # Otherwise, assign turn to next player in list
                else:
                    self.Players[playerNum + 1].isTheirTurn = True
                    return           
                

    # Assigns first turn based on first hand tile value, if not assigned already by serialization
    def SetFirstTurn(self):

        # Return without assigining if turn already set
        for playerNum in range(len(self.Players)):
            if (self.Players[playerNum].isTheirTurn == True):
                return

        # Assign first turn based on hand value
        self.Players[0].isTheirTurn = True

    # Initalizes decks 
    def InitalizeDecks(self):

        # Check if stack sizes aren't zero (serialization)
            # Check if the hands are set, if not, set them
            # Otherwise do nothing

        # Otherwise, initalize everything
        pass

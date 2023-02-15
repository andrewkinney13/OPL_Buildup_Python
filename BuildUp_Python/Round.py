
from GUI import GUI

class Round:
    # Constructor
    def __init__(self, GUI, Players, Decks):
        # Initalize data members 
        self.GUI = GUI
        self.Players = Players
        self.Decks = Decks
        self.count = 3;

    # Plays round
    def PlayRound(self, retFunc):
        self.retFunc = retFunc

        # Initalize decks if not done so already
        if(len(self.Decks[0].stack) == 0):
            pass

        # Initalize hand if not done so already and boneyard tiles remain
        if(len(self.Decks[0].hand) == 0 and len(self.Decks[0].boneyard) != 0):
            pass

        # Set first turn
        self.SetFirstTurn()

        # If hand successfully created, play a round
        if(len(self.Decks[0].hand) != 0 or self.count >= 0):
            self.PlayHand()

        # This is just for testing
        if(self.count <= 0):
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
        if(self.PlayableTilesRemain() and self.count != 0):
            print(self.count)

            # Cycle through players
            for i in range(len(self.Players)):

                # If their turn, let them play
                if(self.Players[i].isTheirTurn and self.Players[i].HasPlayableTiles()):
                    self.Players[i].TurnChoice(self.GUI, self.PlayHand)
            
            self.count -= 1
            self.ChangeTurns()

            

        else:
            self.GUI.CreateLabel("Hand Over!")
            self.GUI.CreateButton("Continue", lambda: (self.PlayRound(self.retFunc)))



    # See if playable tiles are left in any player's hand
    def PlayableTilesRemain(self):
        return True

    # Gives turn to next player
    def ChangeTurns(self):
        pass

    # Assigns first turn based on first hand tile value, if not assigned already by serialization
    def SetFirstTurn(self):

        # Return without assigining if turn already set
        for i in range(len(self.Players)):
            if(self.Players[i].isTheirTurn == True):
                return

        # Assign first turn based on hand value
        self.Players[0].isTheirTurn = True

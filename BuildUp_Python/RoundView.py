
class RoundView:
    
    # Constructor
    def __init__(self, GUI):
        self.GUI = GUI

    # End of round screen
    def AskNewRound(self, winnerNum, winnerMsg, EndTournament, PlayRound):
        
        # Clear the window
        self.GUI.ClearWindow()

        # Alert player who won
        self.GUI.CreateMenuLabel("Round Over...")
        self.GUI.CreateMenuLabel(str(winnerNum) + " won the round!\n" + winnerMsg)

        # Give options how to continue
        self.GUI.CreateMenuButton("Play New Round", PlayRound, fg = "white", bg = "green")
        self.GUI.CreateMenuButton("Exit", EndTournament, fg = "white", bg = "red")
        
    # End of hand screen 
    def EndOfHandScreen(self, scoreMsg, PlayHand):
        
        # Clear the window
        self.GUI.ClearWindow()

        # Alert player score changes 
        self.GUI.CreateMenuLabel(scoreMsg)

        # Create continue button 
        self.GUI.CreateMenuButton("Continue", PlayHand, fg = "white", bg = "green")


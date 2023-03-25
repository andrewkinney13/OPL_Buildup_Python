
"""
     ************************************************************
     * Name:  Andrew Kinney                                     *
     * Project:  BuildUp, Python Version                        *
     * Class:  Round View                                       *
     * Date:  3.25/2023                                         *
     ************************************************************
"""

class RoundView:
    
    # Constructor
    def __init__(self, GUI):
        self.GUI = GUI

    # End of round screen
    def AskNewRound(self, winnerMsg, EndTournamentFunction, PlayRoundFunction):
        
        # Clear the window
        self.GUI.ClearWindow()

        # Alert player who won
        self.GUI.CreateMenuLabel("Round Over...")
        self.GUI.CreateBigMenuLabel(winnerMsg + "\n")

        # Give options how to continue
        self.GUI.CreateMenuButton("Play New Round", PlayRoundFunction, fg = "white", bg = "green")
        self.GUI.CreateMenuButton("End Tournament", EndTournamentFunction, fg = "white", bg = "red")

    def EndTournament(self, winnerMsg):

        # Clear the window
        self.GUI.ClearWindow()

        # Alert player who won
        self.GUI.CreateMenuLabel("Tournament Over...")
        self.GUI.CreateBigMenuLabel(winnerMsg + "\n")

        # Give options how to continue
        self.GUI.CreateMenuButton("Exit", exit, fg = "white", bg = "red")

 
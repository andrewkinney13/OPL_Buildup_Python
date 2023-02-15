

class Round:
    # Constructor
    def __init__(self, GUI, Players, Decks):
        # Initalize data members 
        self.GUI = GUI
        self.Players = Players
        self.Decks = Decks

    # Plays round
    def PlayRound(self):

        for i in range(len(self.Players)):
            print("PLAYER HERE!")
            print("DECK HERE, WITH SIZE: " + str(self.Decks[i].size))
        
        pass
    



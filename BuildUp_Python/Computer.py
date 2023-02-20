
from Player import Player

class Computer(Player):

    # Constructor
    def __init__(self, name):
        self.color = 'W'
        self.name = name

        # Call base class constructor
        super().__init__()

     # For when in a hand, choosing where to place tile
    def TurnChoice(self, Players, Decks, playerNum):
        
        # Initalize current turn attributes
        self.turnDecks = Decks
        self.turnPlayers = Players
        self.playerNum = playerNum

        # Print player menu
        self.PlayerMenu() 

        print("AHHH!")

 

from Player import Player

class Computer(Player):

    # Constructor
    def __init__(self, name):
        self.color = 'W'
        self.name = name

        # Call base class constructor
        super().__init__()

     # For when in a hand, choosing where to place tile
    def TurnChoice(self, Decks, playerNum):
        self.GUI.CreateLabel("It's " + str(self.name) + "'s turn...")
        self.GUI.CreateButton("Continue", self.AfterTurnFunctions)

 
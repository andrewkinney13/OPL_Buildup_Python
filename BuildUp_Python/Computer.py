
from Player import Player

class Computer(Player):

    # Constructor
    def __init__(self, name):
        self.color = 'W'
        self.name = name

        # Call base class constructor
        super().__init__()

     # For when in a hand, choosing where to place tile
    def TurnChoice(self, GUI, retFunc):
        GUI.CreateLabel("Computer does what it wants!")
        GUI.CreateButton("Continue", retFunc)




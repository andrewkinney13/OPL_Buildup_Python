
from Player import Player

class Human(Player):
    
    # Constructor
    def __init__(self, name):
        self.color = 'B'
        self.name = name

        # Call base class constructor
        super().__init__()


    # For when in a hand, choosing where to place tile
    def TurnChoice(self, GUI, retFunc):
        GUI.CreateLabel("It's your turn, human, what do")
        GUI.CreateButton("Continue", retFunc)


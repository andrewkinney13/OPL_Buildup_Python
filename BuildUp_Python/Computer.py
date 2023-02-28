
from Player import Player

class Computer(Player):

    # Constructor
    def __init__(self, name, side, GUI):
        self.color = 'W'
        self.name = name
        self.side = side
        self.GUI = GUI

        # Call base class constructor
        super().__init__()



    

from Player import Player
from ComputerView import ComputerView

class Computer(Player):

   # Constructor
    def __init__(self, name, color, GUI):
     
        self.GUI = GUI
        self.ComputerView = ComputerView(GUI)

        # Call base class constructor
        super().__init__(name, color)



    
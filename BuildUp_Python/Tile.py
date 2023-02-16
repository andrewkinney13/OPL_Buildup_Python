
class Tile:

    # Constructor 
    def __init__(self, color, sideOnePips, sideTwoPips):
        self.color = color
        self.sideOnePips = sideOnePips
        self.sideTwoPips = sideTwoPips
        
    # Returns if tile is a doulbe
    def IsDouble(self):
        if (self.sideOnePips == self.sideTwoPips):
            return True
        else:
            return False

    # Returns total pip value of the tile
    def GetValue(self):
        return self.sideOnePips + self.sideTwoPips

    # Returns string form of the tile
    def GetStringForm(self):
        return str(self.color) + str(self.sideOnePips) + str(self.sideTwoPips)

    # Overloaded operators
    def __gt__(self, other):

        # This tile is non-double
        if (not self.IsDouble()):

            # Compare values
            if (self.GetValue() > other.GetValue()):
                return True

            else:
                return False

        # This tile is a double
        else:

            # The other tile is a non-double
            if (not other.IsDouble()):
                return True

            # They're both doubles
            else:
                return self.sideOnePips > other.sideOnePips





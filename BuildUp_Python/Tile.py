
class Tile:

    # Constructor
    def __init__(self, color = 'E', sideOnePips = 999, sideTwoPips = 999, playerNum = 999):
        self.color = color
        self.sideOnePips = sideOnePips
        self.sideTwoPips = sideTwoPips

        # Tile's current placability status, in context of a current turn
        self.handPlacable = False
        self.stackPlacable = False

        # Tile highlighted if selected by a player
        self.highlighted = False
        
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
            if (self.GetValue() >= other.GetValue()):
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

    def __eq__(self, other):

        # everything is the same
        if (self.color == other.color and self.sideOnePips == other.sideOnePips and self.sideTwoPips == other.sideTwoPips):
            return True

        # they're not equal
        return False




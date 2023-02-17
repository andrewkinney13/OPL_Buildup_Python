
from Tile import Tile
import random

class Deck:

    # Constructor
    def __init__(self, tileSetSize):
        self.boneyard = []
        self.stack = []
        self.hand = []
        self.maxTilePips = tileSetSize

    
    # Create shuffled boneyard
    def CreateBoneyard(self, color):

        # Create boneyard
            # 0 to domino set size
        for pipSideOneVal in range(self.maxTilePips):

            # sideOneVal to domino set size (so no duplicates)
            for pipSideTwoVal in range(pipSideOneVal, self.maxTilePips):
                self.boneyard.append(Tile(color, pipSideOneVal, pipSideTwoVal))

        # Shuffle the list
        random.shuffle(self.boneyard)

    # Creates hand from boneyard tiles
    def CreateHand(self):
        # If enough tiles exist for default hand size
        if(len(self.boneyard) >= 6):
            for tile in range(6):
                self.hand.append(self.TakeTileFromBoneyard)

        # Make hand with whatever tiles remain
        else:
            for tile in range(len(self.boneyard)):
                self.hand.append(self.TakeTileFromBoneyard)

    # Creates stack from boneyard tiles
    def CreateStack(self):
        # Takes 6 tiles from boneyard to make stack
        for tile in range(6):
            self.stack.append(self.TakeTileFromBoneyard())

    # Take and placement functions
    def TakeTileFromBoneyard(self):
        tile = self.boneyard.pop(0)
        return tile

    # Takes tile from hand at position
    def TakeTileFromHand(self, position):
        tile = self.hand.pop(position)
        return tile



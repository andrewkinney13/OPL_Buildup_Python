
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
    def CreateBoneyard(self, color, playerNum):

        # Create boneyard
            # 0 to domino set size
        for pipSideOneVal in range(self.maxTilePips + 1):

            # sideOneVal to domino set size (so no duplicates)
            for pipSideTwoVal in range(pipSideOneVal, self.maxTilePips + 1):
                self.boneyard.append(Tile(color, pipSideOneVal, pipSideTwoVal, playerNum))

        # Shuffle the list
        random.shuffle(self.boneyard)

    # Creates hand from boneyard tiles
    def CreateHand(self):
        # If enough tiles exist for default hand size
        if(len(self.boneyard) >= 6):
            for tile in range(6):
                self.hand.append(self.TakeTileFromBoneyard())

        # Make hand with whatever tiles remain
        else:
            for tile in range(len(self.boneyard)):
                self.hand.append(self.TakeTileFromBoneyard())

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

    # Places tile onto stack
    def PlaceTileOnStack(self, tile, position):
        self.stack[position] = tile

    # Determines what tiles from hand are placeable on specified stacks
    def DetermineHandPlacability(self, playerStack, opponentStack):
        
        # Go through each tile in the hand
        for handTile in range(len(self.hand)):
           
            # Check for placeability on players stack
            for stackTile in range(len(playerStack)):
                if (self.hand[handTile] > playerStack[stackTile]):
                    self.hand[handTile].handPlacable = True
                    break

            # Check for placability on opponent stack
            for stackTile in range(len(opponentStack)):
                if (self.hand[handTile] > opponentStack[stackTile]):
                    self.hand[handTile].handPlacable = True
                    break

    # Determines what tiles in the stack can be placed on with specified tile
    def DetermineStackPlacability(self, tileToPlace):

        # Go through every stack tile
        for stackTile in range(len(self.stack)):
            
            # Check if the tile can be places
            if (tileToPlace > self.stack[stackTile]):
                self.stack[stackTile].stackPlacable = True

    # Reset hand tile status
    def ResetHandTileStatus(self):
        for tile in range(len(self.hand)):
            self.hand[tile].handPlacable = False

    # Reset stack tile status
    def ResetStackTileStatus(self):
        for tile in range(len(self.stack)):
            self.stack[tile].stackPlaceable = False

    # Reset status of all tiles
    def ResetTileStatus(self):

        # Reset placability statuc
        self.ResetHandTileStatus()
        self.ResetStackTileStatus()

        # Reset the highlighted stack tile
        for tile in range(len(self.stack)):
            self.stack[tile].highlighted = False

    # Removes tile from hand
    def RemoveHandTile(self, tileToRemove):
         
        # Find the tile in hand, remove it
        self.hand.remove(tileToRemove)

    # Highlight selected tile from hand 
    def HighlightHandTile(self,tile):

        # Go through hand, find tile and highlight it
        for tileNum in range(len(self.hand)):
            if (tile == self.hand[tileNum]):
                self.hand[tileNum].highlighted = True
                return


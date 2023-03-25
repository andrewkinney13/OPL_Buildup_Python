
"""
     ************************************************************
     * Name:  Andrew Kinney                                     *
     * Project:  BuildUp, Python Version                        *
     * Class:  Deck                                             *
     * Date:  3.25/2023                                         *
     ************************************************************
"""

from Tile import Tile
import random

class Deck:

    def __init__(self, tileSetSize = 6):
        self.boneyard = []
        self.stack = []
        self.hand = []
        self.maxTilePips = tileSetSize

    # Create shuffled boneyard
    def CreateBoneyard(self, color):

        # Create boneyard
            # 0 to domino set size
        for pipSideOneVal in range(self.maxTilePips + 1):

            # sideOneVal to domino set size (so no duplicates)
            for pipSideTwoVal in range(pipSideOneVal, self.maxTilePips + 1):
                self.boneyard.append(Tile(color, pipSideOneVal, pipSideTwoVal))

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
            self.stack[tile].stackPlacable = False

    # Reset status of all tiles
    def ResetHighlightedTileStatus(self):

        # Reset the highlighted hand tile
        for tile in range(len(self.hand)):
            self.hand[tile].highlighted = False

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

    # Checks if any tiles in the hand are playable 
    def HasPlayableTiles(self, stackOne, stackTwo):
        
        # Go through every hand tile
        for handTile in range(len(self.hand)):

            # Check in first stack
            for stackTile in range(len(stackOne)):
                if self.hand[handTile] > stackOne[stackTile]:
                    return True

            # Check in second stack
            for stackTile in range(len(stackTwo)):
                if self.hand[handTile] > stackTwo[stackTile]:
                    return True

        # There is no placeable tile
        return False

    # Finds tile's index in list, returns -1 if not found
    def FindTile(self, tile, tileList):
        for tileNum in range(len(tileList)):
            if tileList[tileNum] == tile:
                return tileNum

        return -1
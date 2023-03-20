from Player import Player
from PlayerView import PlayerView

class Computer(Player):

    # Constructor
    def __init__(self, name, color, GUI):
        self.GUI = GUI
        self.PlayerView = PlayerView(GUI)

        self.handTileSelectionMsg = ""
        self.stackTileSelectionMsg = ""

        # Call base class constructor
        super().__init__(name, color)

    # Select tile from hand to play
    def SelectHandTile(self, Players, Decks, playerNum, opponentNum):

        # Pick the tile to select
        self.TileSelectionLogic(Decks, playerNum, opponentNum)

        # Create the menu
        self.PlayerView.CreateTileScreen(Players, Decks, playerNum, opponentNum, self.ContinueSelected, "Computer to select tile from hand to play...", self.handTileSelectionMsg)

    # Select what stack to place on
    def SelectStackTile(self, Players, Decks, playerNum, opponentNum, tileToPlace):

        # Print screen with selected stack tile
        self.PlayerView.CreateTileScreen(Players, Decks, playerNum, opponentNum, self.ContinueSelected, "Computer to select stack tile to play on...", self.stackTileSelectionMsg)

    # Selects what tile from hand to play, and on what stack
    def TileSelectionLogic(self, Decks, playerNum, opponentNum, helping = False):

        # Determine placablility of hand tiles
        Decks[playerNum].DetermineHandPlacability(Decks[playerNum].stack, Decks[opponentNum].stack)

        # Create a new hand list with only placeable tiles
        tempHand = []
        for tile in range(len(Decks[playerNum].hand)):
            
            # if tile is placeable, place it in appropriate location
            if (Decks[playerNum].hand[tile].handPlacable):
                    tempHand.append(Decks[playerNum].hand[tile])

        # Reset the tile status (none clickable)
        Decks[0].ResetHandTileStatus()
        Decks[1].ResetHandTileStatus()

        # Sort the new hand list by placement, ascending (doubles last)
        for i in range(len(tempHand) - 1):
            for j in range (0, len(tempHand) - i - 1):
                if tempHand[j] > tempHand[j + 1]:

                    # Check for non-double placement on double, which in this case is invalid
                    if (not tempHand[j].IsDouble() and tempHand[j + 1].IsDouble()):
                        continue
                    else:
                        swapTile = tempHand[j]
                        tempHand[j] = tempHand[j + 1]
                        tempHand[j + 1] = swapTile

        # Create a new stack list, combined and sorted based on the two stacks
        tempStack = []
        tempStack = Decks[playerNum].stack + Decks[opponentNum].stack
        
        # Sort it in descending order, by value
        for i in range(len(tempStack) - 1):
            for j in range (0, len(tempStack) - i - 1):
                if tempStack[j + 1].GetValue() > tempStack[j].GetValue():
                    swapTile = tempStack[j]
                    tempStack[j] = tempStack[j + 1]
                    tempStack[j + 1] = swapTile

        # Go through every tile in hand list, try and place at lowest position that is opponent tile
        tileFound = False
        for handTile in range(len(tempHand)):
            for stackTile in range(len(tempStack)):

                # the hand tile is placeable, and it is the opposite color
                if (tempHand[handTile] > tempStack[stackTile] and tempStack[stackTile].color != Decks[playerNum].hand[0].color):
                    
                    # assign the tile attributes
                    self.tileToPlace = tempHand[handTile]
                    self.tileToPlaceOn = tempStack[stackTile]
                    tileFound = True

                    # assign the message attributes
                    if helping:
                        self.handTileSelectionMsg = "Reccomends " + self.tileToPlace.GetStringForm()  + " because it is the\n lowest placeable tile your hand\n that can be played on opponent"
                        self.stackTileSelectionMsg = "Reccomends " + self.tileToPlaceOn.GetStringForm() + " because it is the\n highest stack tile " + self.tileToPlace.GetStingForm() + " can play on"

                    else:
                        self.handTileSelectionMsg = "Chose " + self.tileToPlace.GetStringForm()  + " because it is the\n lowest placeable tile in hand\n that can be played on opponent"
                        self.stackTileSelectionMsg = "Chose " + self.tileToPlaceOn.GetStringForm() + " because it is the\n highest stack tile " + self.tileToPlace.GetStringForm() + " can play on"

                    break

            if tileFound:
                break

        # None placeable on opponent, place at lowest point on own stack tile
        if not tileFound:
            tempStack.reverse()
            for handTile in range(len(tempHand)):
                for stackTile in range(len(tempStack)):

                    # the hand tile is placeable, anywhere
                    if (tempHand[handTile] > tempStack[stackTile]):

                        # assign the tile attributes
                        self.tileToPlace = tempHand[handTile]
                        self.tileToPlaceOn = tempStack[stackTile]
                        tileFound = True

                        # assign the message attributes
                        if helping:
                            self.handTileSelectionMsg = "Reccomends " + self.TileToPlace.GetStringForm()  + " because it is the\n lowest placeable tile your hand\n that can be played on a stack"
                            self.stackTileSelectionMsg = "Reccomends " + self.tileToPlaceOn.GetStringForm() + " because it is the\n lowest stack tile " + self.tileToPlace.GetStingForm() + " can play on (to save points)"

                        else:
                            self.handTileSelectionMsg = "Chose " + self.TileToPlace.GetStringForm()  + " because it is the\n lowest placeable tile in hand\n that can be played on a stack"
                            self.stackTileSelectionMsg = "Chose " + self.tileToPlaceOn.GetStringForm() + " because it is the\n lowest stack tile " + self.tileToPlace.GetStingForm() + " can play on (to save points)"

                            break

                if tileFound:
                    break


             
        

        



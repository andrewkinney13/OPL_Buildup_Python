
"""
     ************************************************************
     * Name:  Andrew Kinney                                     *
     * Project:  BuildUp, Python Version                        *
     * Class:  Deck View                                        *
     * Date:  3.25/2023                                         *
     ************************************************************
"""

from TileView import TileView

class DeckView:
    
    # Constructor
    def __init__(self, GUI):
        self.GUI = GUI
        self.TileView = TileView(GUI)

    # Create attribute subframes for a player's deck
    def CreateDeckSubFrames(self, mainFrame, deck, TileFunction):
    
        # Create stack subframe
        self.CreateStackSubFrame(deck, mainFrame, TileFunction)

        # Create hand subframe
        self.CreateHandSubFrame(deck, mainFrame, TileFunction)

        # Create boneyard subframe
        self.CreateBoneyardSubFrame(deck, mainFrame)


    # Create stack subframe
    def CreateStackSubFrame(self, deck, mainFrame, TileFunction):
         # Create subframe 
        subFrame = self.GUI.CreateSubFrame(mainFrame)

        # Give a title to the subframe
        self.GUI.CreateFrameMenuLabel("Stack", subFrame)

        # Reinit subframe so buttons are centered 
        subFrame = self.GUI.CreateSubFrame(mainFrame)

        # Put tiles into subrame
        for tile in range(len(deck.stack)):
                
            # If function is specified, attatch it to applicable buttons
            if(deck.stack[tile].stackPlacable and TileFunction != None):
                self.TileView.CreateTileButton(deck.stack[tile], TileFunction, subFrame)

            # Otherwise, make it a label
            else:
                self.TileView.CreateTileLabel(deck.stack[tile], subFrame)

    # Create hand subframe
    def CreateHandSubFrame(self, deck, mainFrame, TileFunction):
        # Create subframe 
        subFrame = self.GUI.CreateSubFrame(mainFrame)

        # Give a title to the subframe
        self.GUI.CreateFrameMenuLabel("Hand", subFrame)

        # Reinit subframe so buttons are centered 
        subFrame = self.GUI.CreateSubFrame(mainFrame)

        # Put tiles into subrame
        for tile in range(len(deck.hand)):
                
            # If function is specified, attatch it to applicable buttons
            if(deck.hand[tile].handPlacable and TileFunction != None):
                self.TileView.CreateTileButton(deck.hand[tile], TileFunction, subFrame)

            # Otherwise, make it a label
            else:
                self.TileView.CreateTileLabel(deck.hand[tile], subFrame)

        # If no tiles exist in hand, pack an empty tile for spacing reasons
        if (range(len(deck.hand) == 0)):
            self.TileView.CreateBlankTileLabel(subFrame)


    # Create boneuard subframe
    def CreateBoneyardSubFrame(self, deck, mainFrame):
         
        # Create subframe 
        subFrame = self.GUI.CreateSubFrame(mainFrame)

        # Give a title to the subframe
        self.GUI.CreateFrameMenuLabel("Boneyard", subFrame)

        # Reinit subframe so labels are centered 
        subFrame = self.GUI.CreateSubFrame(mainFrame)

        # Put tiles into subrame
        count = 0
        for tile in range(len(deck.boneyard)):
            
            # Keep track of how many tiles placed, make it so only 6 rows max are made of boneyard tiles
            if (count > len(deck.boneyard) / 6):
                subFrame = self.GUI.CreateSubFrame(mainFrame)
                count = 0

            count += 1

            # Create the tile
            self.TileView.CreateTileLabel(deck.boneyard[tile], subFrame)

        # If no tiles in boneyard, just print a blank tile 
        if len(deck.boneyard) == 0:
            self.TileView.CreateBlankTileLabel(subFrame)


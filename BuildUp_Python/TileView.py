
import tkinter as tk

class TileView:

    # Constructor
    def __init__(self, GUI):
        self.GUI = GUI

        # Default attributes of tiles
        self.tileWidth = 4
        self.tileHeight = 1
        self.tileFont = ("Comic Sans MS", 14)

    # Creates Tile button (pickable / placeable tile)
    def CreateTileButton(self, tile, function, frame):

        # White
        if (tile.color == 'W'):
            button = tk.Button(master = frame, text = tile.GetStringForm(),  font = self.tileFont, \
                                width = self.tileWidth, height = self.tileHeight, command = lambda: (function(tile)), bg = 'white', fg = 'green')

        # Black
        else:
            button = tk.Button(master = frame, text = tile.GetStringForm(), font = self.tileFont, \
                                width = self.tileWidth, height = self.tileHeight, command = lambda: (function(tile)), bg = 'black', fg = 'green')

        button.pack(side = 'left')

    # Creates Tile label (non-pickable / non-placeable tile)
    def CreateTileLabel(self, tile, frame):

        # Highlighted
        if (tile.highlighted):
            label = tk.Button(master = frame, text = tile.GetStringForm(), font = self.tileFont, \
                               width = self.tileWidth, height = self.tileHeight, bg = 'yellow')

        # Regular color
        else:

            # White
            if (tile.color == 'W'):
                label = tk.Button(master = frame, text = tile.GetStringForm(),  font = self.tileFont, \
                                   width = self.tileWidth, height = self.tileHeight)

            # Black
            else:
                label = tk.Button(master = frame, text = tile.GetStringForm(), font = self.tileFont, \
                                   width = self.tileWidth, height = self.tileHeight, bg = 'black', fg = 'white')

        label.pack(side = 'left')

    # Creates a blank tile if no tiles were placed in a subframe
    def CreateBlankTileLabel(self, frame):
        label = tk.Label(master = frame, width = self.tileWidth, height = self.tileHeight + 1, bg = 'white', fg = 'white')
        label.pack(side = 'left')

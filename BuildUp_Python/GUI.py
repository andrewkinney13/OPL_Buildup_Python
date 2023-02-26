
import tkinter as tk

class GUI():
    # Constructor
    def __init__(self):
        # Default attriutes of widgets
        self.defaultWidth = 40
        self.defaultHeight = 3
        self.defaultFont = ("Comic Sans MS", 14, "bold")

        # Default attributes of tiles
        self.tileWidth = 4
        self.tileHeight = 1
        self.tileFont = ("Comic Sans MS", 14)

        # Initalize window
        self.root = tk.Tk()
        self.root.title("Andrew Kinney's BuildUp Program for OPL")
        self.root.geometry("1000x900")

    # Creates button with default attributes, but custom text and command
    def CreateButton(self, text, command, frame = None, color = None):
        
        # No color specified
        if (color == None):

            # No frame specified
            if (frame == None):
                button = tk.Button(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, command = command)

            # Frame specified
            else:
                button = tk.Button(text = text, master = frame, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, command = command)

        # Color specified
        else: 
            # No frame specified
            if (frame == None):
                button = tk.Button(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, command = command, 
                                   bg = color, fg = "white")

            # Frame specified
            else:
                button = tk.Button(text = text, master = frame, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, command = command, 
                                   bg = color, fg = "white")

        # Pack the button
        button.pack()

    # Creates label with default attributes, custom text
    def CreateLabel(self, text, frame = None):

        # Create label on window (main menu)
        if (frame == None):
            label = tk.Label(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont)
            label.pack()

        # Create label on frame (attribute label)
        else:
            label = tk.Label(text = text, master = frame, width = self.defaultWidth, height = self.defaultHeight - 1, font = self.defaultFont)
            label.pack(side = 'top', fill= 'x')

    # Creates entry box with default attributes
    def CreateEntry(self):
        entry = tk.Entry(width = self.tileWidth, font = self.defaultFont)
        entry.pack()
        return entry

    # Clears the window of all widgets
    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Starts input-driven window
    def StartInputLoop(self):
        self.root.mainloop()


    # Creates Tile button (pickable / placeable tile)
    def CreateTileButton(self, tile, function, frame):

        # White
        if (tile.color == 'W'):
            button = tk.Button(master = frame, text = tile.GetStringForm(),  font = self.tileFont, \
                                width = self.tileWidth, height = self.tileHeight, command = lambda: (function(tile)))

        # Black
        else:
            button = tk.Button(master = frame, text = tile.GetStringForm(), font = self.tileFont, \
                                width = self.tileWidth, height = self.tileHeight, command = lambda: (function(tile)), bg = 'black', fg = 'white')

        button.pack(side = 'left')

    # Creates Tile label (non-pickable / placeable tile)
    def CreateTileLabel(self, tile, frame, highlighted = False):
        # Highlighted
        if (highlighted):
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

    # Creates Tile main frame, holds rows of frames of buttons and labels
    def CreatePlayerMainFrame(self, side):

        # Create frame
        frame = tk.Frame(self.root)
        frame.pack(side = side, fill = 'y')

        return frame

    # Creates subframe within mainframe
    def CreateAttributeSubFrame(self, mainFrame):

        # Create subframe in mainFrame
        subFrame = tk.Frame(mainFrame)
        subFrame.pack(side = "top")

        return subFrame





import tkinter as tk

class GUI():
    # Constructor
    def __init__(self):
        # Default attriutes of widgets
        self.defaultWidth = 40
        self.defaultHeight = 3
        self.defaultFont = ("Comic Sans MS", 14, "bold")

        # Default attributes of tiles
        self.tileWidth = 6
        self.tileHeight = 2
        self.tileFont = ("Comic Sans MS", 14)

        # Initalize window
        self.root = tk.Tk()
        self.root.geometry("1100x600")
        self.root.title("Andrew Kinney's BuildUp Program for OPL")

    # Creates button with default attributes, but custom text and command
    def CreateButton(self, text, command):
        button = tk.Button(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, command = command)
        button.pack()

    # Creates label with default attributes, custom text
    def CreateLabel(self, text, frame = None):

        # Create label on window
        if (frame == None):
            label = tk.Label(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont)
            label.pack()

        # Create label on frame
        else:
            label = tk.Label(text = text, master = frame, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont)
            label.pack(side = 'top', fill= 'x')
        

    # Creates entry box with default attributes
    def CreateEntry(self):
        entry = tk.Entry(width = self.defaultWidth, font = self.defaultFont)
        entry.pack()
        return entry

    # Clears the window of all widgets
    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Starts input-driven window
    def StartInputLoop(self):
        self.root.mainloop()


    # Creates Tile button (placeable tile)
    def CreateTileButton(self, frame, tile, function, highlighted = False):
        # Highlighted
        if (highlighted):
            button = tk.Button(master = frame, text = tile.GetStringForm(), font = self.tileFont, \
                               width = self.tileWidth, height = self.tileHeight, command = function, bg = 'yellow')

        # Regular color
        else:

            # White
            if (tile.color == 'W'):
                button = tk.Button(master = frame, text = tile.GetStringForm(),  font = self.tileFont, \
                                   width = self.tileWidth, height = self.tileHeight, command = function)

            # Black
            else:
                button = tk.Button(master = frame, text = tile.GetStringForm(), font = self.tileFont, \
                                   width = self.tileWidth, height = self.tileHeight, command = function, bg = 'black', fg = 'white')

        # Put button in the frame
        button.pack(side = 'left', fill = 'x')

    # Creates Tile main frame, holds rows of frames of buttons and labels
    def CreateTileMainFrame(self, side):

        # Create frame
        frame = tk.Frame(self.root)
        frame.pack(side = side, fill = 'y')

        return frame

    # Creates subframe within mainframe
    def CreateTileSubFrame(self, mainFrame):

        # Create subframe in mainFrame
        subFrame = tk.Frame(mainFrame)
        subFrame.pack(side = "top")

        return subFrame




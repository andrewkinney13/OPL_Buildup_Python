
import tkinter as tk

class GUI():
    # Constructor
    def __init__(self):
        # Default attriutes of widgets
        self.defaultWidth = 40
        self.defaultHeight = 2
        self.defaultFont = ("Comic Sans MS", 14, "bold")

        # Initalize window
        self.root = tk.Tk()
        self.root.title("Andrew Kinney's BuildUp Program for OPL")
        self.root.geometry("900x900")

    # Starts input-driven window
    def StartInputLoop(self):
        self.root.mainloop()

    # Clears the window of all widgets
    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Creates menu button
    def CreateMenuButton(self, text, command, fg = "black", bg = "white"):

        # Create the button
        button = tk.Button(text = text, command = command, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, fg = fg, bg = bg)
        button.pack()

    # Creates menu button attatched to specified frame
    def CreateFrameMenuButton(self, text, command, frame, fg = "white", bg = "black"):
        
       # Create the button
        button = tk.Button(text = text, command = command, master = frame, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, fg = fg, bg = bg)
        button.pack()

    # Creates regular label 
    def CreateMenuLabel(self, text):

       # Create the label
        label = tk.Label(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont)
        label.pack()

    # Creates a label on the bottom of the screen
    def CreateBottomMenuLabel(self, text):

        # Create the label
        label = tk.Label(text = text, width = self.defaultWidth, height = 7, font = self.defaultFont)
        label.pack(side = "bottom", fill = "y")

    # Creates regular menu label
    def CreateFrameMenuLabel(self, text, frame):

        # Create label 
        label = tk.Label(text = text, master = frame, width = self.defaultWidth, height = self.defaultHeight-1, font = self.defaultFont)
        label.pack()

    # Creates a main frame for subframes to attatch to, with specified side
    def CreateMainFrame(self, side):

        # Create frame
        frame = tk.Frame(self.root)
        frame.pack(side = side, fill = "y")

        # Return frame
        return frame

    # Creates subframe within mainframe
    def CreateSubFrame(self, mainFrame):

        # Create subframe in mainFrame
        subFrame = tk.Frame(mainFrame)
        subFrame.pack(side = "top")

        return subFrame

    # Sets the save function from Tournament class
    def SetSaveFunction(self, saveFunc):
        self.SaveFunction = saveFunc

    def GetSaveFunction(self):
        return self.SaveFunction


    """
       # Creates entry box with default attributes
    def CreateEntry(self):
        entry = tk.Entry(width = self.tileWidth, font = self.defaultFont)
        entry.pack()
        return entry
    """
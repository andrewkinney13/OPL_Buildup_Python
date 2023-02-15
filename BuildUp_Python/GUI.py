
import tkinter as tk
from Tournament import Tournament

class GUI():
    # Constructor
    def __init__(self):
        # Default attriutes of widgets
        self.defaultWidth = 40
        self.defaultHeight = 3
        self.defaultFont = ("Comic Sans MS", 14, "bold")

        # Initalize window
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Andrew Kinney's BuildUp Program for OPL")

        # Initalize tournament object
        self.Tournament = Tournament()

        # Get the menu input on game initalization before starting the game
        self.GetInitialInput()

        


        # Start the event-driven loop
        self.root.mainloop()

    # Get first menu input to start the game
    def GetInitialInput(self):
        self.CreateLabel(text = "Welcome to my Buildup Program!\nPlease make a selection...")
        self.CreateButton(text = "Create new 2 Player Tournament", command = self.InitTwoPlayers)
        self.CreateButton(text = "Create new 4 Player Tournament", command =  self.InitFourPlayers)
        self.CreateButton(text = "Create Tournament from Serialization File", command = self.LoadSerializationFile)
       
    # Use tournament class function
    def InitTwoPlayers(self):
        self.Tournament.InitTwoPlayers()

    # Use tournament class function
    def InitFourPlayers(self):
        self.Tournament.InitFourPlayers()

    # Obtain filename
    def LoadSerializationFile(self):
        self.ClearWindow()
        self.CreateLabel(text = "Enter the name of the serialization file:")
        self.CreateEntry()

    # Creates button with default attributes, but custom text and functions
    def CreateButton(self, text, command):
        button = tk.Button(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont, command = command)
        button.pack()

    # Creates label with default attributes, custom text
    def CreateLabel(self, text):
        label = tk.Label(text = text, width = self.defaultWidth, height = self.defaultHeight, font = self.defaultFont)
        label.pack()

    # Creates entry box with default attributes
    def CreateEntry(self):
        entry = tk.Entry(width = self.defaultWidth, font = self.defaultFont)
        entry.pack()

    # Clears the window of all widgets
    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    




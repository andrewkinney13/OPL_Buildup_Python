
"""
     ************************************************************
     * Name:  Andrew Kinney                                     *
     * Project:  BuildUp, Python Version                        *
     * Class:  Client (main)                                    *
     * Date:  3.25/2023                                         *
     ************************************************************
"""

from GUI import GUI
from Tournament import Tournament

# Initalize GUI
myGUI = GUI()

# Initalize tournament object
myTournament = Tournament(myGUI)

# Start tournament
myTournament.StartTournament()
""" Make a class and instance of that class; Put the team’s player roster into the text file and retrieve that text. Make sure the file is readable."""

class Player:
   """Put the team's player roster into the text file and retrieve that text
    Attributes:
        roster (str) : the team's player roster
    """
    def __init__(self, file):
        """Initialize attribute for creating file and read the file
        Args:
            roster (list) : the team's player roster
        """
        self.roster = list()
        
        with open(file, "w", encoding="utf-8")
    
    
    def findRoster(self, players):
        """Retrieve the text file of the team's player roster
        Args:
            players (text) : a text file of the teams' player roster
        """
        with open(players, "r", encoding="utf-8")
            
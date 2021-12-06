import random
teams = ["Arizona Cardinals", "Atlanta Falcons", "Carolina Panthers", "Dallas Cowboys",
         "Chicago Bears", "Detroit Lions", "Green Bay Packers", "New York Giants",
         "Los Angeles Rams", "Minnesota Vikings", "New Orleans Saints", "Philadelphia Eagles",
         "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Washington Football Team"]
contestants = ["Baltimore Ravens", "Buffalo Bills", "Cincinatti Bengals", "Cleveland Browns",
               "Denver Broncos", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars",
               "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers", "Miami Dolphins",
               "New England Patriots", "New York Jets", "Pittsburgh Steelers", "Tennessee Titans"]

class Game:
    def __init__(self, name):
        self.name = name

class Contestant(Game):
    def retrieve_team(self):
        random.shuffle(self.name)
        return {'AFC:':self.name[0], 'NFC:':self.name[1]}

my_team = Contestant(contestants).retrieve_team()
for team, name in my_team.items():
    print(team, name)
   
""" Make a class and instance of that class; Put the team’s player roster into the text file and retrieve that text. Make sure the file is readable."""

class Roster:
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
            

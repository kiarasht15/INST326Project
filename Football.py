import random

"""reference for roster_team: 
https://www.azcardinals.com/team/players-roster/, https://www.atlantafalcons.com/team/players-roster/, 
https://www.panthers.com/team/players-roster/, https://www.dallascowboys.com/team/players-roster/, 
https://www.chicagobears.com/team/players-roster/, https://www.detroitlions.com/team/players-roster/,
https://www.packers.com/team/players-roster/, https://www.giants.com/team/players-roster/,
https://www.therams.com/team/players-roster/, https://www.vikings.com/team/players-roster/,
https://www.neworleanssaints.com/team/players-roster/, https://www.philadelphiaeagles.com/team/players-roster/,
https://www.49ers.com/team/players-roster/, https://www.seahawks.com/team/players-roster/,
https://www.buccaneers.com/team/players-roster/, https://www.washingtonfootball.com/team/players-roster/"""

"""reference for roster_contestants:
https://www.baltimoreravens.com/team/players-roster/, https://www.buffalobills.com/team/players-roster/,
https://www.bengals.com/team/players-roster/, https://www.clevelandbrowns.com/team/players-roster/,
https://www.denverbroncos.com/team/players-roster/, https://www.houstontexans.com/team/players-roster/,
https://www.colts.com/team/players-roster/, https://www.jaguars.com/team/players-roster/,
https://www.chiefs.com/team/players-roster/, https://www.raiders.com/team/players-roster/,
https://www.chargers.com/team/players-roster/, https://www.miamidolphins.com/team/players-roster/,
https://www.patriots.com/team/players-roster/, https://www.newyorkjets.com/team/players-roster/,
https://www.steelers.com/team/players-roster/, https://www.tennesseetitans.com/team/players-roster/ 
""" 




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

retrieved_teams = Contestant(contestants).retrieve_team()
for team, name in retrieved_teams.items():
    print(team, name)
   


class Roster:
    """open the team's player roster as text file and find one of team roster thorugh the text file
    then return list of the roster
    Attributes:
        roster (dictionary) : a dictionary for the team's player roster
        file (txt) : text file for the team's player roster
    """
    
    def __init__(self, file):
        """Initialize attribute for creating file and read the file
        Args:
            file (txt) : text file for the team's player roster
        """
        self.roster = dict()      
        self.file = file
    
    def roster_file(self, teams):
        """read text file and return list of team roster 
        Args:
            teams (txt) : a text file of the teams' player roster
        Returns:
            (dictionary) : a dictionary of tema roster with each team name
        """
        with open(teams.file, "r", encoding="utf-8") as f: 
            self.roster 
            for line in f:
                lines = line.strip().split(': ')
                self.roster[lines[0]] = lines[1].split(', ')
                result = self.roster
            return result
    
    def find_roster(self, teamname):
        """find roster which match with the teamname
        Args:
            teamname (str) : a team name 
        Returns:
            (str) :  show a string with team name and its roster from 
            list of the roster"""
        roster_dict = self.roster
        for names in roster_dict:
            if teamname in names:
                return names[teamname]
            

import random
teams = ["Arizona Cardinals", "Atlanta Falcons", "Carolina Panthers", "Dallas Cowboys",
         "Chicago Bears", "Detroit Lions", "Green Bay Packers", "New York Giants",
         "Los Angeles Rams", "Minnesota Vikings", "New Orleans Saints", "Philadelphia Eagles",
         "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Washington Football Team"]
contestants = ["Baltimore Ravens", "Buffalo Bills", "Cincinnati Bengals", "Cleveland Browns",
               "Denver Broncos", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars",
               "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers", "Miami Dolphins",
               "New England Patriots", "New York Jets", "Pittsburgh Steelers", "Tennessee Titans"]

   
class Contestant:
    """This class pulls two random teams from each of the lists (teams and contestants). 
    
    Attributes: 
      name (str) : variable used for updating the name to output the retrieved teams from above. 
        
    Returns: 
        (str) : a team from the list of teams. 
    """

    def __init__(self, name):
         self.name = name

    def retrieve_team(self):
        random_team = random.choice(self.name)
        return random_team
        
  


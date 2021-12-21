import random
teams = ["Arizona Cardinals", "Atlanta Falcons", "Carolina Panthers", "Dallas Cowboys",
         "Chicago Bears", "Detroit Lions", "Green Bay Packers", "New York Giants",
         "Los Angeles Rams", "Minnesota Vikings", "New Orleans Saints", "Philadelphia Eagles",
         "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Washington Football Team"]
contestants = ["Baltimore Ravens", "Buffalo Bills", "Cincinnati Bengals", "Cleveland Browns",
               "Denver Broncos", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars",
               "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers", "Miami Dolphins",
               "New England Patriots", "New York Jets", "Pittsburgh Steelers", "Tennessee Titans"]

class Game:
    """ This class is used to initiate the name object that is later used in the code.

    Attributes: 
      name : This attribute was used to create the name variable. 

    Returns: 
      Makes a new instance of the name variable.  
    
    """
   
class Contestant(Game):
    """This class pulls two random teams from each of the lists (teams and contestants). 
    
    Attributes: 
      random.shuffle : Used this global function to randomly shuffle between the two lists. 
      retrieved_teams (str ): Set this variable to output the team names that were retrieved. 
      team (str) : variable used for updating the team to output the league that the teams were from (NFC and AFC). 
      name (str) : variable used for updating the name to output the retrieved teams from above. 
        
    Returns: 
        This code returns a team from the AFC list and the NFC list. 
    """

    def __init__(self, name):
         self.name = name

    def retrieve_team(self):
        random.shuffle(self.name)
        return {'AFC:':self.name[0], 'NFC:':self.name[1]}
        
    print(f"Which team would you like to choose?")
retrieved_teams = Contestant(contestants).retrieve_team()
for team, name in retrieved_teams.items():
    print(team, name)
value = input("Please choose a team from the two options above\n")
if value == name:
    print(f"You entered {name}")
else:
    print("Sorry that is not an option")

import Team
import Roster
import sys
import random
import csv
import re
import argparse

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
    def __init__(self, name):
        self.name = name

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

txt1 = "roster_afc_team.txt"
txt2 = "roster_nfc_team.txt"


def increase_skill(team_name):
    number = input("Enter 1 to increase running skill or enter 2 to increase throwing skill")
    
    if number == 1:
        team_name.increase_running_skill()
    elif number == 2:
        team_name.increase_throwing_skill()

def main(player1, player2):
    """Play football game
    Args:
        player1 (str) : player1 team name
        player2 (str) : player2 team name
    Side Effects:
        (str) : Indicate which team is winner with its score
    """
    roster1 = roster_file(txt1)
    roster2 = roster_file(txt2)
    
    p1 = find_roster(player1, roster1)
    p2 = find_roster(player2, roster2)
 



    
def parse_args(arglist):
    """ Parse command-line arguments.
    Args:
        arglist (list of str): command-line arguments.
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file containing roster")
    args = parser.parse_args(arglist)
    return args

       
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)  
    
    

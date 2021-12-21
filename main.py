from skills import *
from roster import *
from footballteams import *
import sys
import random
import csv
import re
import argparse

skills.__init__()

txt1 = "roster_afc_team.txt"
txt2 = "roster_nfc_team.txt"

teams = ["Arizona Cardinals", "Atlanta Falcons", "Carolina Panthers", "Dallas Cowboys",
         "Chicago Bears", "Detroit Lions", "Green Bay Packers", "New York Giants",
         "Los Angeles Rams", "Minnesota Vikings", "New Orleans Saints", "Philadelphia Eagles",
         "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Washington Football Team"]
contestants = ["Baltimore Ravens", "Buffalo Bills", "Cincinnati Bengals", "Cleveland Browns",
               "Denver Broncos", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars",
               "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers", "Miami Dolphins",
               "New England Patriots", "New York Jets", "Pittsburgh Steelers", "Tennessee Titans"]

user_choice = ""


def increase_skill(team_name):
    number = input("Enter 1 to increase running skill or enter 2 to increase throwing skill")
    
    if number == 1:
        return Team.increase_running_skill(team_name)
    elif number == 2:
        return Team.increase_throwing_skill(team_name)

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
 
    
    
    
 
    user_choice = input("Would you want to start season for your football game or 'no'?: ")
    if user_choice == "no"
         print("End")
    p1 = random.choice(teams)
    prinnt(p1)
    p2 = random.choice(contestants)
    print(p2)
    r1 = find_roster(choose_team1, roster1)
    r2 = find_roster(choose_team2, roster2)
    team1 = Team(choose_team1, 0, 0, random.randint(1, 5), r1)
    team2 = Team(chhose_team2, 0, 0, random.randint(1, 5), r2)
    
    question = input("Which team do you want to play? Enter 1 for team 1 and 2 for team 2: ")
    if question == 1:
            print(r1)
            print("Running Skill = " + team1.combined_running_skill)
            print("Throwing Skill = " + team1.combined_throwing_skill)
            print("Skill Tokens = " + team1.skill_token)
                  
            increase_skill(team1)
    if question == 2:
            print(r2)
            print("Running Skill = " + team2.combined_running_skill)
            print("Throwing Skill = " + team2.combined_throwing_skill)
            print("Skill Tokens = " + team2.skill_token)
                  
            increase_skill(team2)
    
    
        



    
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
    
    
def find_score(graph, start, end, path=[]):
    score = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_score(graph, node, end, path)
            if newpath:
                return newpath
            
print(find_score(graph, 'd', 'c'))

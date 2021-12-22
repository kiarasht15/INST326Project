from skills import *
from roster import *
from footballteams import *
from score import *
import sys
import random
import csv
import re
import argparse

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



def main():
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
         
    p1 = Contestant(teams).retrieve_team()
    print(p1)
    p2 = Contestant(contestants).retrieve_team()
    print(p2)
    r1 = find_roster(p1, roster1)
    r2 = find_roster(p2, roster2)
    team1 = Team(p1, 0, 0, random.randint(1, 5), r1)
    team2 = Team(p2, 0, 0, random.randint(1, 5), r2)
    
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
    for i in range(18):
        team1_odd = odd()
        team1_even = even()
        team2_odd = odd()
        team2_even = even()
        score1 = cal_score(team1_even, team1_odd)
        score2 = cal_score(team2_even, team2_odd)
    if score1 > score2:
        print(f"team1 is winner with score {score1}!")
    elif score1 == score2:
        print(f"there is no winner at this time -- tie -------")
    elif score1 < score2:
        print(f"team2 is winner with score {score2}!")
         
        
    
        



    

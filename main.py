from Team, Roster, Game, Contestant import *
import Contestant
import sys
import random
import csv
import re
import argparse


txt1 = "roster_afc_team.txt"
txt2 = "roster_nfc_team.txt"
user_choice = ""


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
    
    while (user_choice != "no"):
        user_choice = input("Would you want to start season for your football game or 'no'?: ")
 



    
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
    
    

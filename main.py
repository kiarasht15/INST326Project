import Team
import Roster
import sys
import random
import csv



txt1 = "roster_afc_team.txt"
txt2 = "roster_nfc_team.txt"


def increase_skill(team_name):
    number = input("Enter 1 to increase running skill or enter 2 to increase throwing skill")
    
    if number == 1:
        team_name.increase_running_skill()
    elif number == 2:
        team_name.increase_throwing_skill()

def main(player1,player2):
    x = Roster(txt1)
    y = Roster(txt2)
    
    player1 = x.roster_file()
    player2 = y.roster_file()
    
    
    

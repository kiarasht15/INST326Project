import Team
import sys
import random
From Roster import roster_file, find_roster

def increase_skill(team_name):
    number = input("Enter 1 to increase running skill or enter 2 to increase throwing skill")
    
    if number == 1:
        team_name.increase_running_skill()
    elif number == 2:
        team_name.increase_throwing_skill()


    
        

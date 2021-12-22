import sys
import random

class Team:

    def __init__(self, team_name, combined_running_skill, combined_throwing_skill, skill_token, roster):
        """Creates an instance of a team object
        Attributes:
        team_name (String) : Name of the team
        combined_running_skill (int) : How good the team is at running the ball
        combined_throwing_skill (int) : How good the team is at throwing the ball
        skill_token (int) : How many tokens the team has to increase their skill 
        roster (Roster) : The players in the team

        """
        self.team_name = team_name
        
        running_skill = random.randint(1,100)
        throwing_skill = random.randint(1,100)

        self.combined_running_skill = running_skill
        self.combined_throwing_skill = throwing_skill
        self.roster = roster
    
    def increase_throwing_skill(self):
      """Uses a skill token to increase the throwing skill for the team.
      
      """
      if self.skil_token > 0 and self.combined_throwing_skill < 100:
        if self.combined_throwing_skill + 10 > 100:
          increase = 100 - self.combined_throwing_skill
          combined_throwing_skill = self.combined_throwing_skill + increase
        else:
          combined_throwing_skill = self.combined_throwing_skill + 5        
    
    def increase_running_skill(self):
      """Uses a skill token to increase the running skill for the team.
      
      """
      if self.skil_token > 0 and self.combined_running_skill < 100:
        if self.combined_running_skill + 10 > 100:
          increase = 100 - self.combined_running_skill
          combined_running_skill = self.combined_running_skill + increase
        else:
          combined_running_skill = self.combined_running_skill + 5
     
    def get_running_skill(self):
        return self.combined_running_skill
    
    def get_throwing_skill(self):
        return self.combined_throwing_skill

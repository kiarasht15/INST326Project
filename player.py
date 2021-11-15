team_database = dict()

class Player:
    def __init__(self, name, position, skill_stat, team):
        self.name = name
        self.position = position
        self.skill_stat = skill_stat
        self.team = team
    
    def get_info(player):
        print("Name: " + player.name + " Position: " + player.position
              + "Skill: " + player.skill_stat + "Team: " + player.team)
    
    def trade_player(player, team):
        player.team = team
        

def add_team(team_name, list_player):
    team_database[team_name] = list_player

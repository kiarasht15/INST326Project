import random
teams = ["Arizona Cardinals", "Atlanta Falcons", "Carolina Panthers", "Dallas Cowboys",
         "Chicago Bears", "Detroit Lions", "Green Bay Packers", "New York Giants",
         "Los Angeles Rams", "Minnesota Vikings", "New Orleans Saints", "Philadelphia Eagles",
         "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Washington Football Team"]
contestants = ["Baltimore Ravens", "Buffalo Bills", "Cincinatti Bengals", "Cleveland Browns",
               "Denver Broncos", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars",
               "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers", "Miami Dolphins",
               "New England Patriots", "New York Jets", "Pittsburgh Steelers", "Tennessee Titans"]

class Game:
    def __init__(self, name):
        self.name = name

class Contestant(Game):
    def retrieve_team(self):
        random.shuffle(self.name)
        return {'AFC':self.name[0], 'NFC':self.name[1]}

my_team = Contestant(contestants).retrieve_team()
for team, name in my_team.items():
    print(team, name)

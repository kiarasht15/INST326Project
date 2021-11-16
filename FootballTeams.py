import random
import sys

class footballGame: 
    nfc_team = ""
    afc_team = ""

    def nfcTeamRandom():
        nfc_team = ["Arizona Cardinals", "Atlanta Falcons", "Carolina Panthers", "Dallas Cowboys", "Chicago Bears", "Detroit Lions", 
        "Green Bay Packers", "New York Giants", "Los Angeles Rams", "Minnesota Vikings", "New Orleans Saints",
         "Philadelphia Eagles", "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Washington Football Team"]

        for name in random.sample(nfc_team, 1):
            nfc_team = name
            nfc_team = nfc_team.upper()

        footballGame.nfc_team = nfc_team

    def afcTeamRandom():
        afc_team = ["Baltimore Ravens", "Buffalo Bills", "Cincinatti Bengals", "Cleveland Browns", "Denver Broncos", "Houston Texans", 
        "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers",
        "Miami Dolphins", "New England Patriots", "New York Jets", "Pittsburgh Steelers", "Tennessee Titans"]

        for name in random.sample(afc_team, 1):
            afc_team = name
            afc_team = afc_team.upper()

        footballGame.afc_team = afc_team
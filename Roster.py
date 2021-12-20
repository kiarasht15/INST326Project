
""" Make a class and instance of that class; open the team's player roster as 
text file and find one of team roster thorugh the text file then return list of the roster"""

"""reference for roster_team: 
https://www.azcardinals.com/team/players-roster/, https://www.atlantafalcons.com/team/players-roster/, 
https://www.panthers.com/team/players-roster/, https://www.dallascowboys.com/team/players-roster/, 
https://www.chicagobears.com/team/players-roster/, https://www.detroitlions.com/team/players-roster/,
https://www.packers.com/team/players-roster/, https://www.giants.com/team/players-roster/,
https://www.therams.com/team/players-roster/, https://www.vikings.com/team/players-roster/,
https://www.neworleanssaints.com/team/players-roster/, https://www.philadelphiaeagles.com/team/players-roster/,
https://www.49ers.com/team/players-roster/, https://www.seahawks.com/team/players-roster/,
https://www.buccaneers.com/team/players-roster/, https://www.washingtonfootball.com/team/players-roster/"""

"""reference for roster_contestants:
https://www.baltimoreravens.com/team/players-roster/, https://www.buffalobills.com/team/players-roster/,
https://www.bengals.com/team/players-roster/, https://www.clevelandbrowns.com/team/players-roster/,
https://www.denverbroncos.com/team/players-roster/, https://www.houstontexans.com/team/players-roster/,
https://www.colts.com/team/players-roster/, https://www.jaguars.com/team/players-roster/,
https://www.chiefs.com/team/players-roster/, https://www.raiders.com/team/players-roster/,
https://www.chargers.com/team/players-roster/, https://www.miamidolphins.com/team/players-roster/,
https://www.patriots.com/team/players-roster/, https://www.newyorkjets.com/team/players-roster/,
https://www.steelers.com/team/players-roster/, https://www.tennesseetitans.com/team/players-roster/ 
""" 

class Regex:
    """open the team's player roster as text file and find one of team roster thorugh the text file
    then return list of the roster
    Attributes:
        team (str) : team name
    """
    
    def __init__(self, team):
        """Initialize attribute for creating file and read the file
        Args:
            team (str) : team name
        """     
        self.team = team

    def match_regex(self):
        """match regex with team name
        Raises:
            ValueError : if regular expression fails, 
            indicate that the team name string could not be parsed
        """
        pattern = r"""(?xs)
                    ^
                    (?P<cg_fline>[A-Za-z]{3,15})
                    (\s)?(?P<ct_sline>[A-Za-z]{3,9})
                    (\s)?(?P<cg_tline>(\w{3,13})?)
                    $"""
        
        
        match = re.search(pattern, self.team)
        
        if match:
            self.team = match.group()
            return (self.team)
        else:
            raise ValueError("The team name string could not be parsed!")
            

    def __repr__(self):
        """present the team name"""
        
        return (f"{self.team!r}")




def roster_file(file):
    """read text file and return list of team roster 
        
    Returns:
        (dictionary) : a dictionary of tema roster with each team name
    """
    with open(file, "r", encoding="utf-8") as f: 
        roster = dict() 
        for line in f:
            lines = line.strip().split(': ')
            roster[Regex(lines[0])] = lines[1].split(', ')
            result = roster        
        print(result) 




def find_roster(chosen_name, team_roster):
        """find roster which match the regular expression with the teamname
        Args:
            chosen_name (str) : chosen team name 
            team_roster (dict) : dictionary of teams' roster
        Returns:
            (str) :  show a string with team name and its roster from 
            list of the roster
        Raises:
            ValueError : if chosen team name is not in the team roster
        """
        for team_names in team_roster:
            if chosen_name in team_names:
                print(f"Team Name : {chosen_name} & members: {team_roster[chosen_name]}")
            else:
                raise ValueError(" ")

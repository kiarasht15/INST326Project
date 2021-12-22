import sklearn

class File:

  """Class file have two methods, one for reading the file and printing it,
  other for closing the file"""

  def __init__(self, fileName):
    information = open(fileName, "r")
    print(information.read()) 

  def closeFile(self, fileName):
    information.close()


class Players:

  """Class players has two methods, one for reading the file and other for
  adding players to the file"""

  def __init__(self,fileName):
    print("-----------------------------")
    readPlayers = File(fileName)

  def newPlayer(self, fileName):
    print("-----------------------------")
    addPlayer = open(fileName, "a")
    pName = input("Please add the new player name and the points (separated by a comma): ")
    addPlayer.write("\n")
    addPlayer.write(pName)


class Plays:

  """read and print the file"""

  def __init__(self, fileName):
    print("-----------------------------")
    print("Name      |       Points \n")
    readPlays = open(fileName, "r")
    splitFile = readPlays.split(",")
    print(splitFile)



if __name__ == "__main__":

"""creates objects of the classes that inherit all the methods"""

  name1 = 'Players.txt'
  name2 = 'Players2.txt'
  plays = 'Plays.txt'

  team1 = Players(name1)
  team1.newPlayer(name1)
  team1 = Players(name1)

  team2 = Players(name2)
  playsDisplay = Plays(plays)

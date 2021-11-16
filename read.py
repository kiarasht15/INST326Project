"""Read.ipynb


Original file is located at
    https://colab.research.google.com/drive/1k_2RkOkROk1dlMv0oNYGI36cDDIhd5O0
"""

import sklearn

class File:
  '''Class to set up a file object'''
  def __init__(self, fileName):
    information = open(fileName, "r")
    print(information.read()) 

  def closeFile(self, fileName):
    '''Class to close the file'''
    information.close() 

#Running Main code and creating an object
name = 'Plays.txt'
information = File(name)
information.closeFile

#Docstrings
print(File.__doc__)
print(information.closeFile.__doc__)
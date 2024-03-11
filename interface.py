#The purpose of this file is to display previous guesses and clues to the user in a board
from graphics import *
import random
import math
import time

def drawClues(len,win,spacer,y):
  '''this function draws all the circles that involved in a clue. the number of clues and their formation can vary. at the end the set of 3 to 6 dots is returned as clue which is a list of len circle objects'''
  
  clue = []
  circleRadius = 4
  if len == 5:
    distancer = 9
  elif len == 6:
    distancer = 10
  else:
    distancer = 7
  centerX = (len+0.75)*spacer 
  if len == 3:
    topLeft = Circle(Point(centerX,y-distancer),circleRadius)
    clue.append(topLeft)
    
  else:
    topLeft = Circle(Point(centerX-distancer,y-distancer),circleRadius)
    clue.append(topLeft)
    c = Circle(Point(centerX+distancer,y-distancer),circleRadius)
    clue.append(c)
    c.draw(win)
  d = Circle(Point(centerX-distancer,y+distancer),circleRadius)
  e = Circle(Point(centerX+distancer,y+distancer),circleRadius)
  topLeft.draw(win)
  d.draw(win)
  e.draw(win)  
  clue.append(d)
  clue.append(e)

  if len == 5:
    center = Circle(Point(centerX,y),circleRadius)
    center.draw(win)
    clue.append(center)
  if len == 6:
    leftCenter = Circle(Point(centerX-distancer,y),circleRadius)
    rightCenter = Circle(Point(centerX+distancer,y),circleRadius)
    leftCenter.draw(win)
    rightCenter.draw(win)
    clue.append(leftCenter)
    clue.append(rightCenter)
  return clue
    
def drawDots(rowLength,win,spacer):
  '''draws all the circle objects for all the guess as a two dimentional list called guesses. it also makes all the clue circles into a two dimensional list. it returns both two dimentional lists'''
  clues = []
  guesses = []
  for j in range(14):
    y = j*(spacer*1.3)+((spacer*1.5)//2)
    guess = []
    for i in range(rowLength):
      x = i*spacer+(spacer//2)
      c = Circle(Point(x,y),7)
      guess.append(c)
      c.draw(win)
    guesses.append(guess)
    clues.append(drawClues(rowLength,win,spacer,y))
  return guesses,clues

def createDisplay(answer):
  '''creates a window called win which will display the board. it returns all the clue objects, all the guess objects and the window'''
  spacer = 30
  frameWidth = len(answer)*spacer + spacer*1.5
  frameHeight=600
  win = GraphWin("Your Board",frameWidth , frameHeight)
  win.setBackground("darkgray")
  rect1 = Rectangle(Point(0,0),Point(len(answer)*spacer,frameHeight))
  rect1.draw(win)
  rect1.setFill("gray")
  rect2 = Rectangle(Point(0,550),Point(len(answer)*spacer + spacer*1.5+10,frameHeight))
  rect2.draw(win)
  rect2.setFill("darkslategray")
  
  prevTry, clues = drawDots(len(answer),win,spacer)
  message = Text(Point(frameWidth//2,frameHeight-25), "Mastermind")
  message.draw(win)
  message.setFill("Orange")
  return clues,prevTry,win
  
def end(win):
  '''closes the window'''
  win.close()

def display(prev, clues, prevTry):
  '''takes in the prev(previous guesses and clues) list, the clues(clue circle objects) list and the prevTry(guess circle objects) list and updates the clues and prevTry list to match the prev list; '''

  for i in range(0,len(prev)-2,3):

    for c in range(len(prev[i+1])):
      prevTry[i//3][c].setFill(guessList(prev[i+1])[c])

    for c in range(len(prev[i+1])):
      clues[i//3][c].setFill(clueList(prev[i+2])[c])
    
def guessList(numberGuess):
  '''takes in a guess in the form of a list of integers and returns a list of colors to be used to fill in circles'''

  colToNum = {1:"red",2:"orange",3:"yellow",4:"lime",5:"green",6:"blue",7:"purple",8:"pink",9:"brown",10:"turquoise",11:"violet"}
  output = []
  for i in numberGuess:

    output.append(colToNum[i])
  return output

def clueList(temp):
  '''takes a clue in the form of a tuple and turns it into a list of black, white, and dark gray as strings '''
  clue=[0,0]
  clue[0] = temp[0]
  clue[1] = temp[1]
  lst = []
  for i in range(15):
    if clue[0] != 0:
      clue[0] -=1
      lst.append("black")
    elif clue[1] != 0:
      clue[1] -= 1
      lst.append("white")
    else:
      lst.append("dark gray")
  return lst





#The purpose of this file is to give the user a way to make a guess in the game


from graphics import *

class WindowInformation:

  '''this class exists only to make passing information about the inputter window easier. I thought of this quite late but it allows only one parameter to be passed into a function and the relevant variables to be extracted via get methods'''
  def __init__(self, inputter, frameWidth, frameHeight, length,maxim,boxHeight, radius, boxLength,dots):
    '''the set of variables above are stored in as self variables so that they can be easily accessed from other functions'''
    self.inputter = inputter
    self.frameWidth = frameWidth
    self.frameHeight = frameHeight
    self.length = length
    self.maxim = maxim
    self.boxHeight = boxHeight
    self.dotRadius = radius
    self.boxLength = boxLength
    frameCenter = frameWidth // 2
    dotSpacing = radius * 3
    rowLength = dotSpacing * (length - 1)
    self.dotsLeft = frameCenter - (rowLength / 2) - radius
    self.dotsRight = frameWidth - self.dotsLeft
    self.dots = dots
 
  def getFrameWidth(self):
    '''returns the frameWidth'''
    return self.frameWidth

  def getFrameHeight(self):
    '''returns the frameHeight'''
    return self.frameHeight

  def getBoxHeight(self):
    '''returns the height of the buttons'''
    return self.boxHeight

  def getDotRadius(self):
    '''returns the radius of the circles'''
    return self.dotRadius

  def getDotCount(self):
    '''returns the amount of circles'''
    return self.length

  def getBoxLength(self):
    '''returns the returns the length of a button'''
    return self.boxLength

  def getDotsRight(self):
    '''returns the x value that lies just outside the rightmost dot'''
    return self.dotsRight

  def getDotsLeft(self):
    '''returns the x value that likes just outside the leftmost dot'''
    return self.dotsLeft

  def getInputter(self):
    '''returns the window called inputter'''
    return self.inputter
  
  def getDots(self):
    '''returns the the list of dot objects'''
    return self.dots
  
  def getMaxim(self):
    '''returns the amount of colors(amount of buttons)'''
    return self.maxim

def makeColorRectangles(boxCount, length, frameWidth, frameHeight, inputter,boxHeight):
  '''this function makes the boxes that will function as buttons for the different colors. it returns a list of rectangle objects called boxes, a height for future dots to be placed at and the length of the buttons'''
  boxLength = frameWidth / boxCount
  boxes = []

  x1 = 0
  x2 = boxLength
  y1 = frameHeight - boxHeight
  y2 = frameHeight
  dotHeight = y1 // 2
  for i in range(boxCount):

      c = Rectangle(Point(x1, y1), Point(x2, y2))
      c.draw(inputter)
      x1 = x2
      x2 += boxLength
      boxes.append(c)

  return boxes, dotHeight, boxLength

def boxFiller(boxes):
  '''this function takes the list of boxes and colors them by taking the place of each box in the list and determining the color assosiated with that key in a dictionary.'''
  numColors = {
      1: "red",
      2: "orange",
      3: "yellow",
      4: "lime",
      5: "green",
      6: "blue",
      7: "purple",
      8: "pink",
      9: "brown",
      10: "turquoise",
      11: "violet"
  }
  for i in range(len(boxes)):
      color = numColors[i + 1]
      boxes[i].setFill(color)

def makeDots(y, frameWidth, length, inputter):
  '''creates the list called dots which contains one circle object for each place in the combination'''
  #placement is determined
  dots = []
  frameCenter = frameWidth / 2

  radius = 14
  dotSpacing = radius * 3
  rowLength = dotSpacing * (length - 1)
  x = frameCenter - (rowLength // 2)

  for i in range(length):

      c = Circle(Point(x, y), radius)
      c.draw(inputter)
      dots.append(c)
      x += dotSpacing

  return dots, radius

def dotFiller(dots, guess):
  '''takes in the list of dots and fills them in to show the user the current state of their guess. it fills in the objects in dots so they match guess'''
  numColors = {
      0: "dark gray",
      1: "red",
      2: "orange",
      3: "yellow",
      4: "lime",
      5: "green",
      6: "blue",
      7: "purple",
      8: "pink",
      9: "brown",
      10: "turquoise",
      11: "violet"
  }
  for i in range(len(dots)):
      dots[i].setFill(numColors[guess[i]])

def createInputWindow(length, maxim):
  '''this function creates a window called inputter and adds elements to it. it uses the length of the answer and how many colors are allowed and returns the window, a list of dots, and inputterInfo(info about the window)'''
  #starts the guess out blank
  blank = [0, 0, 0, 0, 0, 0]
  frameWidth = length * 60
  frameHeight = 120
  boxHeight = 40
  titleHeight = 50
  inputter = GraphWin("Input", frameWidth, frameHeight + titleHeight)
  inputter.setBackground("dark gray")
  # buttons are made
  boxes, dotHeight, boxLength = makeColorRectangles(maxim, length, frameWidth, frameHeight, inputter, boxHeight)
  boxFiller(boxes)
  # dots are Mastermind
  dots, radius = makeDots(dotHeight, frameWidth, length, inputter)
  # dots are filled with a blank guess
  dotFiller(dots, blank)
  # inputterInfo is created with all the parameters from above
  inputterInfo = WindowInformation(inputter, frameWidth, frameHeight, length, maxim, boxHeight, radius, boxLength, dots)

  #Adds the box with the name at the bottom
  point1 = Point(0, frameHeight)
  point2 = Point(frameWidth, frameHeight + titleHeight)
  titleBox = Rectangle(point1, point2)
  titleBox.draw(inputter)
  titleBox.setFill("darkslategray")
  message = Text(Point(frameWidth // 2, frameHeight + (titleHeight // 2)), "Mastermind")
  message.draw(inputter)
  message.setFill("Orange")

  return inputter, dots, inputterInfo

def boxOrDot(x, y, inputterInfo):
  '''this function uses the x and y returned from a mouse click to determine whether a button or a dot was clicked or neither. it then returns that information'''
  frameWidth = inputterInfo.getFrameWidth()
  frameHeight = inputterInfo.getFrameHeight()
  boxHeight = inputterInfo.getBoxHeight()
  radius = inputterInfo.getDotRadius()
  dotCount = inputterInfo.getDotCount()
  colorTop = frameHeight - boxHeight
  yCenter = colorTop // 2
  dotsLeft = inputterInfo.getDotsLeft()
  dotsRight = inputterInfo.getDotsRight()

  if y >= colorTop and y <= frameHeight:
      return "colorButtons"
  elif y <= yCenter + radius and y >= yCenter - radius and x <= dotsRight and x >= dotsLeft:
      return "dots"
  else:
      return "background"

def whichButton(x, inputterInfo):
    '''after a button press is confirmed this function uses the x value to determine which button was pressed and returns the number of that button'''
    boxLength = inputterInfo.getBoxLength()
    frameWidth = inputterInfo.getFrameWidth()
    buttonAmount = inputterInfo.getMaxim()
    button = int((x // boxLength) + 1)
    if button > buttonAmount:
      button -= 1
    return button

def whichDot(x, inputterInfo):
  '''after a dot is pressed this function uses the x value from the mouse click to determine which dot was clicked. it then returns this value'''
  leftLim = inputterInfo.getDotsLeft()
  rightLim = inputterInfo.getDotsRight()
  dotRange = rightLim - leftLim
  dotCount = inputterInfo.getDotCount()
  dotLength = dotRange / dotCount
  xToDots = x - leftLim
  dot = int(xToDots // dotLength)
  return dot

def dotOutliner(dots, dot):
  '''thickens the outline of a certain dot at the index dot in dots'''
  for i in dots:
    i.setWidth(1)
  dots[dot].setWidth(3)

def getInput(length, maxim, dots, inputter, inputterInfo):
  '''takes in a guess from the user and returns a list of numbers corresponding to that guess'''
  #starts the guess out as a list of zeros-- a blank guess
  blank = [0, 0, 0, 0, 0, 0]
  #the outline of the first dot is darkened to indicate that is the dot that can be currently changed
  dotOutliner(dots, 0)
  dotFiller(dots, blank)  
  frameHeight = inputterInfo.getFrameHeight()
  # a list of the same length as the solution is created and filled wiht 0s
  out = []
  for i in range(length):
    out.append(0)
  guessing = True
  dot = 0
  button = 1
  while guessing:
    #if all of the dots are filled that means that with the use of the enter key or a press of the mastermind button will confirm and guess the guess
    if 0 not in out:
      if b == 'Return':
          guessing = False
      b = inputter.checkKey()
    #if the mouse has been used then the point will be mousePoint
    mousePoint = inputter.checkMouse()
    
    if mousePoint != None:
      #the x and y of the mouse click are separated and it is determined which button or which dot was pressed.
      mouseX, mouseY = mousePoint.getX(), mousePoint.getY()
      whichButtons = boxOrDot(mouseX, mouseY, inputterInfo)
      #this situation means that the user has pressed the mastermind button and if they have a complete guess this sends it off to the game to be analized and added to the board
      if mouseY > frameHeight:
        b = 'Return'
      #the following to elif statements are used in combination to make changes to the guess. a user selects a dot that they want to change and then select a button of the color they want to change it to. if the user has not yet filled all the dots then it will automatically move to the next empty dot after selecting a color with a button. this allows the user to mark all the dots they are certain of with the color they are sure of and then just click on any color to fill in the rest.
      elif whichButtons == "dots":
        dot = whichDot(mouseX, inputterInfo)
        b = ''
      elif whichButtons == "colorButtons":
        b = ''
        button = whichButton(mouseX, inputterInfo)
        out[dot] = button
        while out[dot] != 0 and 0 in out[dot:] and dot < len(out) - 1:
          dot += 1
          if 0 in out[:dot]:
            dot = 0
      # here the dot fillings are updated to match the out list
      dotFiller(dots, out)
      # here the dot that is currently being examined is given a thicker outline
      dotOutliner(dots, dot)
  #once the guess has been completed by filling all the dots and either hitting return or pressing the mastermind button the list 'out' is returned as the guess
  return out

def showAnswer(inputterInfo,answer):
  '''this function displays the correct answer on the input window in the event that a user either wins or loses'''
  dots = inputterInfo.getDots()
  dotFiller(dots,answer)


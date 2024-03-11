# The purpose of this file is to run a game of master mind which can be played either by an AI or by a human.
from solver import solve
from interface import *
from input1 import *
import random


def compare(hand,answer):
  '''this function takes in the players guess and the correct solution and returns what the proper clue should be.'''
  #here two new lists are made to store copies of the hand and answer which can be changed freely without having to deal with mutability
  tempHand = []
  tempAnswer = []
  for place in range(len(hand)):
    tempHand.append(hand[place])
    tempAnswer.append(answer[place])
  #here the clue is determined by first checking how many colors were in the right place and then how many of the remaining colors are found in a different spot on the list
  perfect = 0
  imperfect = 0

  for i in range(len(tempHand)):
    if tempHand[i] == tempAnswer[i]:
      tempHand[i] = "done"
      tempAnswer[i] = "locked"
      perfect += 1

  for i in range(len(tempHand)):
    for b in range(len(tempAnswer)):
      if tempHand[i] == tempAnswer[b]:
        tempHand[i] = "done"
        tempAnswer[b] = "locked"
        imperfect += 1

  return perfect, imperfect

def setUpAnswer():
  '''this function is used to set up a solution. in it the user inputs the length of the combination and the amount of possible colors and then a random combination is generated. it returns the correct answer and how many colors will be avaliable'''
  done = False
  while done == False:
    done = True
    lengthOfAnswer = int(input("How long should the combination be? (between 3 and 6)  "))
    if lengthOfAnswer < 3 or lengthOfAnswer > 6:
      done = False
      print("Invalid input, please try again")

  done = False
  while done == False:
    done = True
    optionQuantity = int(input("How many colors should be possible?  (up to 11 with short combinations)  "))
    if optionQuantity < 1 or optionQuantity > 11:
      done = False
      print("Invalid input, please try again")
  
  answer = []
  for i in range(lengthOfAnswer):
    answer.append(random.randint(1,optionQuantity))
  
  return answer, optionQuantity

def depict(prev,clues,prevTry):
  '''this function uses the list of all previous guesses and clues and makes a depiction of them in the console. It also calls upon the later added display function which displays the board in a window'''
  for i in range(0,len(prev)-2,3):
    #ensures that there won't be wierd spacing after 10 turns
    if prev[i] >= 10:
      spacing = "   "
    else:
      spacing = "    "
    #prints board to console
    print("Turn #",prev[i],spacing,prev[i+1],"   ",prev[i+2])
  #updates the board
  display(prev, clues, prevTry)

def createHand(prev,turn,player,dots,inputter,inputterInfo,maxim,length):
  '''this is where a guess is made. if the computer is playing then it uses the solve function. if the player is playing then it takes their input from the getInput function. it then returns a guess which is a list of integers that represent colors'''

  if player == "computer":
    guess = solve(length,maxim,prev,turn)
  else:
    guess = getInput(length,maxim,dots,inputter,inputterInfo)
  return guess

def doTurn(answer,prev,turn,maxim,player,dots,inputter,inputterInfo):
  '''this function calls upon the createHand function to collect a guess. then it adds the turn were on and the guess to a list called prev. it also adds the clue for that guess using the compare function and finally it returns a 1 or a 0. 1 means win, 0 means continue. '''
  #print(answer)
  length = len(answer)
  hand = createHand(prev,turn,player,dots,inputter,inputterInfo,maxim,length)
  prev.append(turn)
  prev.append(hand)
  prev.append(compare(hand,answer))
  if compare(hand,answer) == (len(hand), 0):
    return 1
  else:
    return 0

def whosPlaying():
  '''this function takes in an input from the user which determines whether the player is playing or if the computer should solve the game. it then retuns the result'''
  
  done = False
  while done == False:
    player = int(input("To play, input 1. to watch AI play, input 2."))
    if player == 1:
      return "player"
      done = True
    elif player == 2: 
      return "computer"
      done = True
    else:
      print("invalid option")
      done = False
         
def main():
  '''this is where everything happens. too much happens here for a doc string so I will add separate comments'''
  b = 0
  #each game is one run through this while loop. everything is reset when it starts again
  while True:
    b += 1
    #an answer and number of colors is chosen
    answer,maxim = setUpAnswer()
    #windows from previous games are closed before new ones are made
    if b != 1:
      end(win)
      if player != "computer":
        end(inputter)
    #a window for the board is created and elements added
    #clues contains all the circles designated for clues
    #prevTry contains all the circles designated to display previous trys
    #win is the board window
    clues, prevTry,win = createDisplay(answer)
    #the player chooses whether they want to play or watch the ai
    player = whosPlaying()
    # if the player is playing then a input window is created that allows them to guess
    if player == "player":
      #inputter is the input window
      #dots is the line of circles in that window
      #inputter info is a collection of information about inputter. it is a class with methods to get that info.
      inputter,dots,inputterInfo = createInputWindow(len(answer),maxim)
    else:
      #this only exist so that when the computer is playing there is something for functions that otherwise would require theses parameters
      inputter,dots,inputterInfo = 0,0,0

    done = 0
    turn = 0
    prev = []
    #this is where games actually take place. 
    #this loop runs until the player has won or run out of guesses(14)

    while done == 0:
      turn+= 1
      print()
      depict(prev, clues, prevTry)
      #does a turn
      done = doTurn(answer,prev,turn,maxim,player,dots,inputter,inputterInfo)
      #checks if the player has lost and if they have then it returns indicates that by setting done to 2.
      if turn == 14 and done == 0:
        done = 2
    depict(prev, clues, prevTry)
    #gives a win or lose message and displays correct answer in the input window(inputter) when the player is playing. 
    if done == 1:
      print("you won on Turn #",turn,"!")
      if player == "player":
        showAnswer(inputterInfo,answer)
    if done == 2:
      print("you lost.")
      if player == "player":
        showAnswer(inputterInfo,answer)


if __name__ == "__main__":
  main()
    

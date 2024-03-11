#The purpose of this file is to solve the master mind game by process of elimination. it takes in only the length of the answer, the permitted number of colors, the previous turns and the turn number it is on to figure out the best next guess for the AI.
from random import shuffle


def copyLst(lst):
  '''this creates a copy of a list and returns that copy so changes can be made to the copy without changing the original'''
  lst2 = []
  for i in lst:
    lst2.append(i)
  return lst2

def createMegaList(length,maxim):
  '''this function takes in the length of the combination and the amount of colors and creates an exhaustive list of all the possible combinations that is called the megaList''' 
  #megaList is set up
  megaList = []
  n = length-1
  m = maxim
  c = 0
  lst = []
  #creates the first version of list which is the right length and only contains 1s
  for i in range(n+1):
    lst.append(1)
  #the megaList is constructed by going through the small list and allways increasing the last place by one and then adding a copy of it to the megaList. if the last number is the maximum number then it increases the number preceeding it by one and setting all the numbers after that back down to 1 and then starts the process again. It repeats that process again for each following digit until it has reached a point at which all the digits have reached the maximum permitted value at which point it knows that the megaList is complete.
  done = False
  while done == False:
    if lst[n-c]!=m:
      megaList.append(copyLst(lst))
      lst[n-c] += 1
    else:
      megaList.append(copyLst(lst))
      while lst[n-c] == maxim and done == False:
        if c < n:
          c+= 1
        else:
          done = True
          break
      if done == False:
        lst[n-c] += 1
      while c!= 0 and done == False:
        c-= 1
        lst [n-c] = 1
  return megaList

def check(lst,guess):
  '''this function has the same purpose as the compare function in main.py. it takes two lists: the currently investigated guess and the previous guess and checks what the clue would be if the current investigated guess was the answer. it returns the clue as perfects and inperfects'''
  
  tempLst = []
  tempGuess = []
  for place in range(len(guess)):
    tempGuess.append(guess[place])
    tempLst.append(lst[place])
 
  perfect = 0
  imperfect = 0
  for i in range(len(tempGuess)):
    if tempGuess[i] == tempLst[i]:
      tempGuess[i] = "done"
      tempLst[i] = "locked"
      perfect += 1
      
  for i in range(len(tempGuess)):
    for b in range(len(tempLst)):
      if tempGuess[i] == tempLst[b]:
        tempGuess[i] = "done"
        tempLst[b] = "locked"
        imperfect += 1
        
  return perfect, imperfect

def viable(lst,prev):
  '''this function checks whether a certain combination is viable as compared to the previous guess. if the combination was the answer, would the previous guess receive the same clue. basically checks whether a combination could be a possible answer. returns boolian accordingly'''
  prevGuess = prev[len(prev)-2]
  clue = check(lst,prevGuess)
  if clue == prev[len(prev)-1]:
    return True
  else:
    return False

def removeWrongs(megaList,prev):
  '''this goes through the megaList and removes all the combinations that are no longer viable  considering the results of the last guess and returns a new megaList with less elements'''
  for i in copyLst(megaList):
    if not viable(i,prev):
      megaList.remove(i)
  return megaList

def solve(length,maxim,prev,turn):
  '''this function always returns the first combination in the megaList as a guess back to the main function. if it is the first turn it creates the megaList containing all possible combinations. on subsequent turns it removes all the impossible combinations from the megaList and then guesses the first remaining entry in that list'''

  if turn == 1:
    global megaList
    megaList = createMegaList(length, maxim)
    shuffle(megaList)
  else:
    removeWrongs(megaList, prev)
  guess = megaList[0]
  return guess



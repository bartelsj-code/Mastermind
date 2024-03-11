Name: Mastermind

By: Jonas Bartels

This project is a game

How to play:
This is a standard game of mastermind.
Your goal is to determine in a limited number of guesses (14) what the correct combination is.
There will be a row of dots and the user will be given a number of colors to apply to those dots. 
COLORS CAN APPEAR MORE THAN ONCE in a combination so just because you know there is one red dot you cannot be certain there won't be more.
In this version of the game you will be able to decide on the length of the combination and on how many colors will be avaliable to the player. These will be prompted as soon as you start up the main.py file. Now you will see a window pop up. this will be your board on which you will be able to keep track of previous guesses. After inputting those two values the console will ask you whether you want to play for yourself or whether you want to watch the AI play for you using a close to ideal method of guessing. To play for yourself, press one and then return. To watch the AI play press two and then return.

      It is to be noted that the AI can get very slow when it is considering long combinations with many color options. though it is able to successfully win a game in which there are 6 dots that could each be one of 11 colors this configuration might take it a few hours to solve. A good suggested game to watch the AI play is a game with a combination length of five dots which could each have one of six colors or one with 6 and 4 accordingly.

If you pressed 1 you will now have a new window called "input" open. You will use this window to make guesses. you will see a row of colored buttons and above them, a row of dots at the top of the window. One of these dots will have a thicker outline than the rest. You can give that dot the color you want to give it by pressing the button of the according color. If you wish to change the color of a certain dot you can select that dot to change it with the any of the colored buttons. this can be useful if you want to mark some spots you are certain of before the rest of your guessing. Once you have filled in all of the dots you will be able to submit your guess. To do this you can either press the button with the word Mastermind that is located under the colored buttons or use the return key on your keyboard. As soon as you do this you will see your guess appear on the board (the other window that opened earlier). next to it you will see a set of circles. THESE are the computer's evaluation of your guess. These circles can be black, white, or empty. 

      If you see a black circle, that indicates to you that you had a dot with the right color at the right position.

      If you see a white circle, that indicates to you that you had a dot with a color that existed in the solution but was guessed in a the wrong position.

      as an example:
 
          let's say the correct solution was
                 
                  red,red,yellow,green

          and let's say you guessed

                  red,yellow,red,blue

          because your solution had one red dot that was in the right position, the computer would show you a black circle. Next, the computer would check your yellow dot. Because your yellow dot exists in the solution but is found in a different position you would be shown a white circle. The same is true for your second red dot because it is found in the solution but once again is in the wrong location. Finally the computer would inspect your blue dot. Because there is no blue dot in the solution you would get neither a black nor a white circle from the computer. At the end of this process the computer will have given you a black circle and two white circles indicating that one of your dots was in the right place and two were in the wrong places.

          Your goal is to determine the correct combination and you will know you have done this once all of the circles are black.

You will be able to use these white and black circles to determine how good your answer was and make an informed follow up guess. To make this next guess you will once again use the input window (the one with the colored buttons). You will be able to make your guess in exactly the same manner as you did before using the dots and colored buttons.
If you manage to determine the solution before you've used up your 14 turns you will have won the game (next time, try to need less guesses to get to the solution).
If you lose the game because you ran out of guesses you will be able to see what the correct answer was in your input window.
to start a new game you need only return to the console that opened up when you opened the main.py file. It will already be asking you for new parameters for the combination and will automatically close your board and input windows as soon as you have entered them.

To run this game you should have the main.py, the graphics.py, and the interface.py files. to play as a human you will also need the input1.py file and to play with the AI you will need the solver.py file. This cannot be run without one and/or the other of these last two.

It may be possible for the user to select an invalid color by pressing on the very right of the colored buttons.



      








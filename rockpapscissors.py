#we have to build a one player game of rock papers and scisorrs in this code.
u = input("PLAYER NAME: ") 
import time as ti     #for importing time from time  moddule

from functools import reduce as rdc

add = lambda x: x + x

import win32com.client as wc
speaker = wc.Dispatch("SAPI.spvoice")

import random         #for importing random and choice functions in code
comp = ["rock","papers","scissors"]          #list form which random options will be choosen by the program itself

for i in range(1,6):              #applying for loop for 5 inputs or func to work 5 times
  s = random.choice(comp)         #applying random and choice function
  points = []                     # creating a variable points to display scores
  i = input("Choose between rock, papers and scissors and quit to quit the game: ")

  if i == "rock" and s == "papers":
   print("computer won")
   speaker.speak("computer won")
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   print("\n\n\n")
  elif i == "rock" and s == "scissors":
   print(f"{u} won")
   speaker.speak(f"{u} won")
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   points.append(2)
   print("\n\n\n")
  elif i == "rock" and s == "rock":
   print("draw")
   speaker.speak("draw")
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   print("\n\n\n")
   
  if i == "papers" and s == "scissors":
   print("computer won")
   speaker.speak("computer won")
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   print("\n\n\n")
  elif i == "papers" and s == "rock":
   print(f"{u} won")
   speaker.speak(f"{u} won")
   points.append(2)
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   print("\n\n\n")
  elif i == "papers" and s == "papers":
   print("draw")
   speaker.speak("draw")
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   print("\n\n\n")

  if i == "scissors" and s == "rock":
   print("computer won")
   speaker.speak("computer won")
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   print("\n\n\n")
  elif i == "scissors" and s == "papers":
   print(f"{u} won")
   speaker.speak(f"{u} won")
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   points.append(2)
   print("\n\n\n")
  elif i == "scissors" and s == "scissors":
   print("draw")
   speaker.speak("draw")
   print(f"computer choose {s}")
   speaker.speak(f"computer choose {s}")
   print("\n\n\n")


print(f"Your total score is: {2}")            #displaying total points won by user
speaker.speak(f"Your total score is: {2}")            #displaying total points won by user


#ti.sleep(6)

#completed my exercise 5 rock papers and scissors game finally:}
'''
Another Cheat
So far we've used break in the while True loop. break leaves the loop completely and runs the next unindented line of code. 
However, you may want to stop the code and start the loop from the top again. (This is ideal for building games!)
In the code below, the game runs and the user is asked if they want to go left or right. If the user chooses left, they fall to their death, and break will kick the user out of the loop. 
That's the game.
'''
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
    
    '''
    Well that's a bit lame and not any different than what we learned in day 16...now for the cheat.
    
    The Continue Command
The continue command stops executing code in the loop and starts at the top of the loop again. Essentially, we want to kick the user back to the original question.
'''
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    
   '''
   The else statement refers to any input besides left or right (up or esc). Since the user is a winner, 
   we do not want to use break or it would say they have failed.

Proceed to the Nearest Exit
The previous code continues to loop even after the user has won. Let's fix that with the exit() command
The exit() command completely stops the program and it will not run any more lines of code.
'''
  
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
So how do we make it stop?

'''
DAY 17 CHALLENGE
'''
from getpass import getpass as input


print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
#hint: create these variables outside loop and then add += with correct player to keep score throughout
player1_score = 0
player2_score = 0
#hint: that the while loop needs to go around all code and then highlight the rest of the code and hit tab once. 
while True: 
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()
  
  if(player1Move=="R"):
    if(player2Move=="R"):
      print("You both picked Rock, draw!")
    elif(player2Move=="S"):
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1_score += 1
    elif(player2Move=="P"):
      print("Player1's Rock is smothered by Player2's Paper!")
      player2_score += 1
  elif(player1Move=="P"):
    if(player2Move=="R"):
      print("Player2's Rock is smothered by Player1's Paper!")
      player1_score += 1
    elif(player2Move=="S"):
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2_score += 1
    elif(player2Move=="P"):
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
  elif(player1Move=="S"):
    if(player2Move=="R"):
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      player2_score += 1
    elif(player2Move=="S"):
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif(player2Move=="P"):
      print("Player1's Scissors make confetti out of Player2's paper!")
      player1_score += 1
  
# hint: make sure you add player scores at the end of all the options but still inside the while loop.
  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:
    continue

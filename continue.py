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

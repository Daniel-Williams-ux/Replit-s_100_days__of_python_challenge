'''
Start with this code below to ensure that whenever you use input, each player cannot see what the other player typed in 😉:

from getpass import getpass as input
'''

from getpass import getpass as input

move1 = "R"
move2 = "P"
move3 = "S"

player1 = input("select your move player1: ")
if player1 == move1 or player1 == "r":
  print("correct")
else:
  print("incorrect")

player2 = input("select your move player2: ")
if player2 == move3 or player2 == "s":
  print("correct")
else:
  print("incorrect")

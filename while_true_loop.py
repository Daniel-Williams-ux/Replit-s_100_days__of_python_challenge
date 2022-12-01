'''
while True Loop
On Day 15, you learned how to create a while loop. However, there are a lot of moving parts that can turn the while loop into an accidental infinite loop...and a nightmare.

Introducing the while True loop...

What do you think the below code does?

Remember you can use the big Stop button on the top if your program does not end.
'''
while True:
  print("This program is running")
print("Aww, I was having a good time 😭")

'''
This type of loop only has two conditions: True and False. Make note of the capital "T" and "F".

A Boolean Loop has two values: True or False. Impress your friends and tell them you know how to use a Boolean Loop.
In this loop, I am saying to the computer:

"while True is True...do this over and over again."

Yes, we made an infinite loop, but hold on...

Make it stop
There is a way to stop the loop with the word break. This exits the loop and stops all code at that point. Even if there is more code written after break that is inside the loop.

After break, the computer jumps out of the loop to the next unindented line of code.
'''

while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")

'''
Common Errors

1. Name Error
👉 What is the error here?
'''
counter = 0
while true:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

'''
Answer

while true needs to be while True.

Notice when you change the lowercase "t" to a capital "T", the color of the word changes as Replit is now recognizing this as a Boolean loop.

2. Syntax Error
'''
counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
addAnother = input("Add another? ")
if addAnother == "no":
  break
print("Bye!")

'''
Answer
Notice the error message is saying the syntax error "break outside loop". 
Do you notice how the last three lines before the bottom print statement are not a part of the loop as they are not properly indented (look at the vertical lines)?

Highlight these three lines of code and press tab key one time to indent this code so it is inside the loop.
'''

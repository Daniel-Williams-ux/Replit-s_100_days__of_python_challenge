counter = 0
while counter < 10:
  print(counter)
  counter += 1
  
  
  
  exit = ""
while exit = "yes":
  print("🥳")
exit = input("Exit?: ")

'''
Day 15 Challenge
Write a program that loops. Inside the loop, ask the user what animal sound they want to hear.
'''
animalType = input("What animal do you want? ")

while animalType == "cow":  
  animalType = 0
  while animalType < 10:
    print("moo")
    animalType += 1

while animalType == "dog":  
  animalType = 0
  while animalType < 10:
    print("woo woo")
    animalType += 1

while animalType == "lion":  
  animalType = 0
  while animalType < 10:
    print("roar")
    animalType += 1    
  
exit = input("do you want to exit? ")
if exit == "yes":
  print("Game over")
else:
  print("Start a new game")

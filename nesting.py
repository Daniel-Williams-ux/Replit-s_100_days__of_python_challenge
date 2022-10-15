favMovie = input('Are you familiar with the movie? ')
if favMovie == 'Titanic':
  print('Oh, you think you know?')
  myChar1 = input('Who is my favorite male character? ')
  if myChar1 == 'Jack':
    print('Wow!')
  myChar2 = input('Who is my favorite female character? ')
  if myChar2 == 'Rose':
     print('That is also true')
  elif myChar2 == "John":
    print('You are fake')
else:
  print('You are real')

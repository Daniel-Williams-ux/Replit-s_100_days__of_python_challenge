name = input('Hey what is your name?: ')
if name == 'Daniel' or name == 'daniel':
  print('Welcome Daniel')
  print()

day = input('What is today?: ')
if day == 'Monday' or day == 'monday':
  print('It is a lovely Monday')
  print('Today you are to study python')
  
elif day == 'Tuesday' or day == 'tuesday':
  print('It is a beautiful Tuesday!')
  print('It is your day of JavaScript coding')

elif day == 'Wednesday' or day == 'wednesday':
  print('It is a colorful Wednesday!')
  print('You have a docker project to complete')

elif day == 'Thursday' or day == 'thursday':
  print('It is a grea day of the week!')
  print('Complete your React development project')

elif day == 'Firday' or day == 'friday':
  print('TGIF!')
  print('However, It is your day for serverless project')

elif day == 'Saturday' or day == 'saturday':
  print('It is weekend!')
  print('It is your day of rest')

elif day == 'Sunday' or day == 'sunday':
  print('You are attending church service by 7 am!')
  print('Remember to attend your cloud development session by 5pm')

else:
  print('Please enter a day of the week')

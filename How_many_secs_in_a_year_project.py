numSecInMin = int(input("How many seconds are in a minute?: "))
if numSecInMin == 60:
  numSecPerHr = numSecInMin * 60
  print("There are", numSecPerHr, "seconds in one hour")
  print()
  
PerDay = int(input("How many seconds are in an hour?: "))
if numSecPerHr == 3600:
  numSecPerDay = 24 * numSecPerHr
  print("There are", numSecPerDay, "in a day")
  print()

perWeek = int(input("How many seconds are in a day?: "))
if numSecPerDay == 86400:
  numSecPerWeek = 7 * numSecPerDay
  print("There are", numSecPerWeek, "in a week")
  print()

perMonth = int(input("How many seconds are in a week?: "))
if numSecPerWeek == 604800:
  numSecPerMonth = 4 * numSecPerWeek
  print("There are", numSecPerMonth, "in a month")
  print()

perYear = int(input("How many seconds are in a year?: "))
if numSecPerMonth == 2419200 or numSecPerMonth == 2764800:
  numSecPerYear = 12 * numSecPerMonth 
  print("There are", numSecPerYear, "in a year")
else:
  print("Please enter the correct integer")
  
  '''
  console
  How many seconds are in a minute?: 60
There are 3600 seconds in one hour

How many seconds are in an hour?: 3600
There are 86400 in a day

How many seconds are in a day?: 86400
There are 604800 in a week

How many seconds are in a week?: 604800
There are 2419200 in a month

How many seconds are in a year?: 2419200
There are 29030400 in a year
'''

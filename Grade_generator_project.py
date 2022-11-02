'''
This project is going to take some time (and some hard thinking) but will be brilliant once you have it working!

You are going to ask the user to type in the name of a test, maximum score they could receive, and how many points they received. 
For example, your test could be called "Python Skills" and the maximum score is 50 points and the user receives 30 points out of 50 possible points.

Here is a grading scale to help you decide the letter grade the user received (feel free to use a different grading scale if you like.)

Letter Grade	Percentage
A+	90-100
A	80-89
B	70-79
C	60-69
D	50-59
U	under 50
'''

name = input("Enter test name: ")
if name == "python" or name == "Python" or name == "PYTHON":
  print("Ok")
else:
  print("Please enter the correct skill")


score = int(input("What is your score? "))

if score <= 100 and score >= 90:
  print("Your grade is A+")
elif score <= 89 and score >= 80:
  print("Your grade is A")
elif score <= 79 and score >= 70:
  print("Your grade is B")
elif score <= 69 and score >= 60:
  print("Your grade is C")
elif score <= 59 and score >= 50:
  print("Your grade is D")
else:
  print("Your score is under 50")

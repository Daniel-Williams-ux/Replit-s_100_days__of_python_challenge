'''
What can range really do?
Give range one number, and it will count up to that number. However, you can actually give the range function a few options...

starting value: what number do you want to start with?
ending value: the number after the number you want to end with (example: if you type 10 as the ending value, the computer will count until 9)
increment: How much should it increase by every time it loops? (example: Do you want to count by 1s, 5s, 10s?)


The ending value has an unsaid 'less than'. Meaning the computer will stop one number before the ending number that is written in the range.

Let's try some examples.

range(starting value, ending value, increment)

he first number in this range, 100, is the starting value. The second number in this range, 110, is the ending value 
(Remember to always put the ending number as one more than where you want to end up).

👉 What number will the code run first? What number will be last? Run the code and find out.
'''

for i in range(100, 110):
  print(i)
  
'''
JavaScript equivalent
'''
for (let i = 100; i < 110; i++) {
console.log(i);
}
  

for i in range(1, 7):
  print("Day", i) 
  
'''
JS
'''
for (let i = 1; i < 8; i++) {
  console.log("Day", i)
}

'''
Did you notice that the counter stopped at 'Day 6'? Change the ending value to be one more than the last number you want shown---in this case, 
8 because we want to display 7 days of the week.
'''
for i in range(1, 8):
  print("Day", i)
  
'''
👉 What happens when you run this code?
'''
print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)

  '''
  JS
  '''
console.log("Thirteen Times Table");
for (let i = 1; i < 13; i++) {
console.log(i + " x 13 = " + i * 13);
'''
template literals
console.log(${i} x 13 = ${i * 13});
'''
}

'''
Increments
We know that this range will start at 0 and continue to 999,999 (which is the number right before the ending value written). 
The number will increase in increments of 25 each time.

👉 What numbers do you expect to see? Hit run and find out.
'''
for i in range (0, 1000000, 25):
  print(i)
  
'''
Counting Backward
In this example, we are starting at 10 and counting backward to 0 (because 0 is what comes right before the ending value listed), 
and counting backward 1 each time.

👉 What do you expect to see when you hit run?
'''
for i in range(10, -1, -1):
  print(i)

  
'''
  Day 20 Challenge
List Generator
Ask the user to list a starting number, ending number, and increment to use. Display an answer based on the users' answers (use the input command.)
Example:
Start at: 200
End before: 300
Increment between values: 20

200
220
240
260
280
''

print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

x = int(input("What number do you want to start with? "))
y = int(input("What number do you want to end with? "))
z = int(input("How many should I add each time? "))

for i in range(x, y, z):
  print(i)

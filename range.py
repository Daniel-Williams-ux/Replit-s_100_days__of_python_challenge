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

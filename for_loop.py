'''
For Loop
A while loop is perfect to use when we don't know how many times we want the loop to repeat.

If we have an idea of how many times we want the loop to repeat, we can use a for loop to loop code in exactly the same way the while loop did.

However, we can set up the variable, control condition, and increment all in ONE line of code.

Let's compare
Here is how we created a counter with a while loop:
'''
counter = 0
while counter < 10:
  print(counter)
  counter += 1
  
'''
And here is the same counter using a for loop:
'''
for counter in range(10):
  print(counter)

'''
Range
The range function creates a list of numbers in the range you create. If you only give it one number, 
it will start at 0 and move to a state where the final number is one less than the number in the brackets. In this case, the final number would be 9.

range(10)
Note: The variable is only there during the loop, not after it is completed.

Fun fact
Commonly computer programmers use the variable names i, j, and k when using for loops for counter. 
There is no real reason. It's just how everyone has always done it. However, feel free to use a variable that has a bit more meaning if you like.

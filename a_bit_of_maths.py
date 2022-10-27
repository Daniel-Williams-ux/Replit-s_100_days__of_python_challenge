adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)

'''
console
7
-1
128
10.0
25
3
7
'''


myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
print("You all owe", answer)

'''
console
What was the bill?: 34.8767788
How many people?: 3
You all owe 11.625592933333332
'''

'''
You can take your answer and use round. Round has two components: "What am I rounding?" and "How many decimal places am I rounding to?"
Add this portion of code after answer and before print. This shows you are rounding answer to 2 decimal points.
'''
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)

'''
console
What was the bill?: 34.876770
How many people?: 3
You all owe 11.63
'''

myBill = float(input("What is the total bill?: "))
tipBill = float(input("What is % of tip wil be added to the total bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)

'''
console
What is the total bill?: 23.098888
What is % of tip wil be added to the total bill?: 5
How many people?: 3
You all owe 7.7
'''

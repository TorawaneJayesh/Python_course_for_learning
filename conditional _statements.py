"""
    conditional statements - there are some statements like if elif and else.
    conditional statements in python allow a program to make decision based on certain conditions.
    if - executes a block of code if the condition is true
    nested if statements - an if statement inside another if statement.
    
"""

# create simple if 
a = 1
if a == 1:
    print("condition is true")

# create simple elif and else
marks = 90
if marks <90:
    print("marks is less than 90")
elif marks == 90:
    print("marks is equal to 90")
else:
    print("marks is greater than 90")
    
# nested if
num = 10 
if num > 0:
    print("positive number")
    if num % 2 == 0 :
        print("even number")
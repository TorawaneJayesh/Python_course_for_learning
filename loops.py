""" 
    loops in python allow you to execute a block of code multiple times.
    1)for - use to iterate over a sequnce (list , tuple , string, range)
    2)while - executes as long as condition is true.
       ~ nested loops - loops inside another loop
       ~ loop controll statement
        1)break - exits a loop completly
        2)continue - skips the current iteration and moves on next
        3)pass - placeholder for an empty loop
"""

# for loop using range function
for i in range(5):
    print(i)

# iterating over a list
fruits = ["mango","banana","grapes"]
for fruit in fruits:
    print(fruit)

# while loop
x = 1
while x <= 5:
    print(x)
    x += 1

# nested loop
for i in range(3):
    for j in range(2):
        print(f"i={i},j={j}")
        
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)


# this pass statement is used when we dont need to write anything in code 
for i in range(5):
    pass



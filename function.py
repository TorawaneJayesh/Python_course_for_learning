""" 
    function - a funtion is a block of reusable code that performs a specific task.
    types of function -  user defined function and built in function.
    
"""

# defining a function 
def greet():
    print("hello world")


# calling a function 
greet()

# function with parameter 
def add(a,b):
    return a+b
result = add(5,3)
print(result)


# default parameters 
def greet(name="user"):
    print("hello",name)
greet()
greet("john")


# return statement
def sqr(num):
    return num * num
print(sqr(4))



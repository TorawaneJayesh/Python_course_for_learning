""" 
    recursion - recursion is a process where a function calls itself.
"""

# factorial using recursion 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# fibonacci series 
def fibonacci(n):
    if n <= 0:
        return "invalid input"
    elif n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))
    

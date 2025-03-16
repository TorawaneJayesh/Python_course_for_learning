""" variable -  a variable is a named storage location in a memory 
    used to store data that can changed during program execution.
    variables are create as follows:
    1)a 
    2)variable
    3)variable_name
    4)VariableName """

# create a variable name
name = "python"

# create a variable marks
marks = 90

# print the length of string (int type does not any length)
print(len(name))    
    
""" constants- a constant is a type of variable whoose value cannot be
    changed during the execution of program."""

# create a constant 
PI = 3.14
gravity = 9.8

# we can also import constant from another file using name of files
import variables
print(variables.PI, variables.gravity)
    
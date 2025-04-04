"""
    when an error occurs or exception as we call it python will normally stop and generate 
    an error message.
    there are three types of errors:
        1) compile time errors 
        2) run time errors 
        3) logical errors 
    1.erros occurs at runtime are known as exception.
    
    try:
        print(x)
    except:
        print("an exception occured.")
    means jab try block me error aayegi to exception block execute hoga.
    finally -  ka matlab agar try block execute ho ya phir except block bus execute karo. 
"""



# in this if user enter string then our program not run for solving this we use try and except.
try:
    a = int(input("enter a num:"))
    print(f"you entered {a}")
except:
    print("please enter num not string")
finally:
    print("it is always execute..")
    
    
# this program throws the value error if user enter age less than 18
age =  int(input("enter the age:"))
if age < 18 :
    raise ValueError("age is small")






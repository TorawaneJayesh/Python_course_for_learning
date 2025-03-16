""" 
    modules - module (like a code library) is file written by another programmer that generally has a function 
    we can use.
    some popullar modules - 
    in built modules - random, os, math, sys.
    third party modules - numpy, pandas, matplotlib etc. which are installed using pip install (pip install packeges)
    user defined modules - this are python files created by the user to orgnise their code.
    
"""
# here are some function of random modules.
import random
a  = random.randint(1,10)
print(a)

# it generates random num between 0.0 and 1.0
a = random.random()
print(a)

a = random.randrange(50)
print(a)

a = random.uniform(1,10)
print(a)

list1 = ["a","b","c","d","g","e"]
print("original list is:",list1)
a = random.choice(list1)
print("generated random list item is:",a)

a = random.shuffle(list1)
print("after shuffling item list is:",list)

from math import*
print(sqrt(4))











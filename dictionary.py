""" 
    dictionary  - are used to store data value in key:value pairs they are unordered mutable & dont allow 
    duplicate key.
"""

# there is simple exaple of dictionary
dict = {"name":"python","type":"oop","author":"guido van rossom"}

print(type(dict))
print(dict)

# dictionary methods
print(dict.keys()) # it returns all the keys

print(dict.values()) # it returns all the values

print(dict.items()) # returns pair as tuples

print(dict.get("name")) # value according to key

dict1 ={"marks":99}
print("dictionary before updation:",dict1)
dict.update("dict1") # insert another dictionary  item to dictionary 
print("dictionary after update",dict)






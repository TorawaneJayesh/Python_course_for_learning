"""  data types - a data types defines the type of value.
in python we don't need to declare data type.
in python following are the types of data types
1)int (1,2,3,4)
2)string ("hello", 'hi')
3)float (1.1, 1.2, 2.2, 3.14)
4)None (None) defines a null object
5)boolean (True = 1, False = 0)
6)list (a = [1,2,3,4,5], b = ["a","b","c","d"])
7)tuple (a = (2,3,"a","c"))
8)dictionary (dic = {1:"one", "marks":90})
9)set (set = {1,2,3,4,5}) """

# create a integer data typee
a = 10
print(a)

# print the type of data type
b = type(a)
print("type of variable a is:",b)

# create a none data type
c = None
print(type(c))

# create an empty string
str = ''
print(type(str))

# convert one data type to another
val = 1.2
print(int(val))

# example of boolean data type (first letter of True and False always capital)
key = True
if key == True:
    print("we have key")
else:
    print("we dont have key")


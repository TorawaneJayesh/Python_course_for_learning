"""
     lists are mutable (changeble)  
     a list is a built in data type that stores set of values it can store element of 
     different data type.
     
"""

# here we create a simple list
fruits = ["mango","orange","banana","apple"]
print(type(fruits))

# acceses all the elements of list
print(fruits)

# acceses particullar elment of list
print("second element of list is:",fruits[1])

# accesses list elements using loop
for fruit in fruits:
    print(fruit)

# use of enumerate function in list
s1 = ["a","c","b","v","g"]
s2 = enumerate(s1,start=2)
print(list(s2))

# list slicing
print(fruits[0:3])

# lists function and methods
list1 = [4,2,3,1]
print("the original list is:",list1)

list1.append(5)
print("add one element at end:",list1)

list1.sort()
print("sort the list using list sort method",list1)

list1.sort(reverse=True)
print("reverse sort the list using list sort method",list1)

list1.reverse()
print("reverse the original list",list1)

list1.insert(6,6) # insert element 6 at 6 index
print(list1)

list1.remove(4) # remove elment 4 from a list
print(list1)

list1.pop(2) # remove elment from 2nd index
print(list1)
""" strings - in python string is a data type. string is a collection of group
    of character. strings are enclosed in single or double quote.
    
    strings are immutable (unchangeble) in python and it cannot be modified.
    
    -backward indexing - python allows us to backward indexing from -1"""
    
# create a string
str1 = 'hello'
str2 = "hi"
print(str1,"\n", str2)

# where use single and double quoted strings 
str3 = "hi that's good"
str4 = 'hi "jonny"'
print(str3,"\n",str4)

# string concatination
print(str1+" "+str2+" "+"python")

# string replication
print(str1*5)

# some string functions
str5 = "hollywood"
print(str5.endswith("ood")) # returns true if condition true.
print(str5.capitalize())
print(str5.replace("holl","boll"))
print(str5.find("y"))
print(str5.count("l"))
print(str5.center(30,"*"))

# basic operations on strings
str6 = "python"
print("original string is:",str6)
print("first element:",str6[0])
print("last element:",str6[-1])
print("element index one to three:",str6[1:3])
print("elements from third index:",str6[3:])
print("elements from zero to third index:",str6[:3])
print("from zero to five as step two:",str6[0:5:2])

str7 = "WELCOME"
print("string is capital or not",str7.isupper())
print("string is lower or not",str7.islower())

s1 = 'python programming'
s1 = s1.encode()
print(s1)
s1 = s1.decode()
print(s1)

# backward indexing
name = "Newyork"
length = len(name)
i = 0
for n in range(-1,(-length-1),-1):
    print(name[i],"\t",name[n])
    i += 1

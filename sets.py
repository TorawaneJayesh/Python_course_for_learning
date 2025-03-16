"""
    sets - set is a collection of unordered items each element in the set must be unique & immutable.
"""

# create an set 
set1 = {1,2,3}
print(type(set1))
print(set1)

# create an empty set 
set2 = set()

# set methods
print(set2)

set2.add(1) # add elements in set 
set2.add(2)
set2.add(3)
print(set2)

set2.remove(3) # remove element from set
print(set2)

set2.pop()  # remove random element from set
print(set2)

set2.clear() # clears the set
print(set2)

set3 = {1,2,3,4}
set4 = {4,5,6,7}

print("set3 is:",set3)
print("set4 is:",set4)

print(set4.union(set3)) # combine both set and return new
print(set4.intersection(set3)) # combine common values






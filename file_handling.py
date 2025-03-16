""" 
    file handling allows reading and writing dara to files.
    after opening a file dont forger to close the file.
    using with function we dont need to close the file.
    there arr two types of files.
    text files - text files are simple text in human readable format a text file is structured as sequnce of lines of
    text.
    binary files - binary files have binary data (0s and 1s) which is understood by the computer.
    
    "r" = mode (default file must exits)
    "w" = write mode (overwrites existing content or creates a new file.)
    "a" = append mode (adds content at the end.)
    "x" = create mode (creates a new file gives error if file exits.)
    "b" = binary mode (e.g."rb",  "wb", for images , video.)
    "r+" = read and write mode.
    
"""

# opening a file using open() and then create a file using write mode.
file = open("sample.txt","w")
file.write("hello this is new sample file.")
file.close()

# reading a file using a r reading mode
f = open("sample.txt","r")
result = f.read()
print(result)

f.seek(0) # this seek fuction use to move pointer position.
print(f.readline()) # read one line at a time.

f.seek(0) 
print(f.readlines()) # read all lines.

f.seek(0) 
print(f.read(5)) # read first 5 characters.
f.close()


# x mode to create a file but when file is already exits then throws error.
"""f = open("demo.txt","x+")
f.seek(0)
print(f.read())"""

# now we can use append mode. also we use with method which does not need to close the file.
with open("sample.txt","a+") as f:
    f.write("this is append content using with syntax.")
    f.write("\nthis is next line only.")
    f.seek(0)
    print(f.read())


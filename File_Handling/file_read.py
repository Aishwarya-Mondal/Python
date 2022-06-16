import os

file = open("text1.txt",'r')

print(file.read()) #reads the file

file.seek(0) # moves to the begining of the file
print(file.read(5)) #reads first 5 characters

file.seek(0)
print(file.readline()) #reads the first line

file.seek(0)
print(file.readline(3)) #reads first 3 characters

file.seek(0)
print(file.readlines()) #reads all the lines and returns a list

file.seek(0)
for line in file:
    print(file.readline())

file.seek(0)
while file:
    line = file.readline()
    print(line)
    if line == "":
        break
file.close()
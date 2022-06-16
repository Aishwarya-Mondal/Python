import os

file = open("test3.txt",'x') #x mode for creation of file, throws error if file already exists

file.write("This is a new file\n")
file.write("Enjoy!\n")

file.close()
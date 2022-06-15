import re
line = "pet:_cat I love cats"
#match = re.match(pattern, string,flag=0(optional))
match = re.match(r"pet:\w\w\w",line) #\w can be letter digit and '_' and matches single character
print(match.group(0))

match = re.search(r"pet:\w\w\w",line)
print(match.group(0))

line2 = "I love my country:India"
m = re.match(r"country:\w\w\w\w\w",line2)
#print(m.group(0)) 
#  -->throws error because the search pattern is present at the end of the line.
#  match function can search for pattern which is presnt at the begining of the line.

s = re.search(r"country:\w\w\w\w\w",line2)
print(s.group(0)) 
# search function gives the output though the pattern is present at the end of the line.
#  This is the differnece between match and search function.

line3= "pet:cat I love cats pet:cow I love cow"
s1 = re.search(r"pet:\w\w\w",line3)
print(s1.group(0))
# although there are two occurances of this pattern in the given line but search function will return the first occurance of the pattern

# to get all the occurances--> findall function is used
f = re.findall(r"pet:\w\w\w",line3)
print(f) # returns a list
import re
line = "I love cats pet:cat I love cows pet:cow Thank you"
s = re.split(r"pet:\w\w\w",line)
print(s) # splits the line by the pattern

line2 ="aish@abc.com and john@cde.com"
replace = re.sub(r"@\w+","@xyz",line2) 
print(replace)
# sub is to substitute.
#  @\w+ -> means starts with @ then \w matches (a-z),(0-9)and '_'. + means there can be one or more occurance of that charcater 
#  replace that pattern with xyz
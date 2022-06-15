# find a word in a string

import re

str = "we need to inform him with latest information"
s = re.search(r"inform",str)
if s:
    print(s.group(0))
else:
    print("not found")

f = re.findall(r"inform",str)
if f:
    print(f) # gives a list as output
else:
    print("not found")
#match series of range of characters

import re

str = "Sat, hat, mat, pat"

allstr = re.findall(r"[h-m]at",str)
allstr1 = re.findall(r"[H-Z | h-z]at",str) # uppercase or lowercase
allstr2 = re.findall(r"[^h-m]at",str) # here ^ means anything other than this range
if allstr:
    print(allstr)
else:
    print("No match")
print(allstr1)
print(allstr2)
# match words with a particular pattern

import re

str = "Sat, mat, bat, hat"

allst = re.findall(r"[Ssbhm]at",str)

if allst:
    print(allst)
else:
    print("No match")
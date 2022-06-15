# \s -> [\f\n\t\r\v]
# \S -> anything other than that

import re

name = "Aishwarya Mondal"

if re.search(r"\w{2,20}\s\w{2,20}",name):
    print("Name is valid")
else:
    print("Not valid")
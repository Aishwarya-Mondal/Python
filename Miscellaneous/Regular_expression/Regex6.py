# Replace a string
# re.compile() method is used to compile a regular expression pattern provided as a string into a regex pattern object (re.Pattern).
#  Later we can use this pattern object to search for a match inside different target strings using regex methods such as a re.match()
#  or re.search().
import re

food = "hat rat mat pat"

food = re.sub(r"[r]at","food",food)
print(food)

regex = re.compile(r"[m]at")
rep = regex.sub("hello",food)
print(rep)
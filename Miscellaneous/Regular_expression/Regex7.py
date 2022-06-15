import re

randstr = '''
Hello everyone
I am Aishwarya
Bye.
'''

print(randstr)

regex = re.compile("\n")
newstr = regex.sub(" ",randstr)

print(newstr)

# \b: backspace
# \f: formfeed
# \r: carraige return
# \t: Tab
# \v: vertical tab
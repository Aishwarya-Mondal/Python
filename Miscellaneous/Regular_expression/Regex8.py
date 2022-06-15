import re
randstr = '12345'

#\d --> matches any digit
#\D --> matches anything other than digit
print("Matches:",len(re.findall(r"\d",randstr)))
print("Matches:",len(re.findall(r"\D",randstr)))

randstr = '123 1234 12345 123456 1234567'
match = re.findall(r"\d{5,7}",randstr) #matches digit ranging from 5 to 7
print("all matches:",match)

